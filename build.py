"""Gerador do blog noticias.semwhere (site estático para GitHub Pages).

Uso:
    python3 build.py            # gera o site em docs/
    python3 build.py --og       # gera também as imagens de pré-visualização (WhatsApp/Facebook)

Conteúdo em content/:
    noticias/AAAA-MM-DD-slug.md   artigos (front matter YAML + texto em Markdown)
    fichas/AAAA-MM-DD-slug.md     fichas de falhas (CVE)
    dicas/AAAA-MM-DD-slug.md      dicas de segurança
    sobre.md                      página "Sobre"
"""
import datetime as dt
import html
import math
import re
import shutil
import sys
from email.utils import format_datetime
from pathlib import Path

import markdown
import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape

from ilustracoes import svg as ilustracao

ROOT = Path(__file__).parent
CONTENT = ROOT / "content"
OUT = ROOT / "docs"
SITE = yaml.safe_load((ROOT / "site.yaml").read_text(encoding="utf-8"))

MESES = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto",
         "Setembro", "Outubro", "Novembro", "Dezembro"]
NIVEIS = {  # nivel -> (rótulo, cor)  — iguais aos cartões do Status
    "CRÍTICO": ("Alerta crítico", "#d63c3c"),
    "ALTO": ("Alerta", "#d9822b"),
    "MÉDIO": ("Atenção", "#c8a227"),
    "INFO": ("Análise", "#4a8fd4"),
    "NOVIDADE": ("Novidade", "#8d7ad6"),
    "DICA": ("Dica de segurança", "#2e9e6a"),
}
SEVERIDADE = {"CRÍTICA": "#d63c3c", "ALTA": "#d9822b", "MÉDIA": "#c8a227", "BAIXA": "#4a8fd4"}
SECCOES = {  # tema -> nome visível
    "ciberseguranca": "Cibersegurança", "tecnologia": "Tecnologia", "gaming": "Gaming",
    "fintech": "Pagamentos", "emprego": "Emprego", "angola": "Angola", "startups": "Startups",
}


def data_pt(d):
    return f"{d.day} de {MESES[d.month - 1]} de {d.year}"


def data_curta(d):
    return f"{d.day} {MESES[d.month - 1][:3].lower()}. {d.year}"


def dominio(url):
    from urllib.parse import urlparse
    return urlparse(url).netloc.removeprefix("www.")


def ler(pasta):
    itens = []
    for f in sorted((CONTENT / pasta).glob("*.md")):
        txt = f.read_text(encoding="utf-8")
        m = re.match(r"^---\n(.*?)\n---\n(.*)$", txt, re.S)
        if not m:
            raise SystemExit(f"Falta o cabeçalho --- em {f}")
        meta = yaml.safe_load(m.group(1)) or {}
        corpo = m.group(2).strip()
        data = meta.get("data")
        if isinstance(data, str):
            data = dt.date.fromisoformat(data)
        if isinstance(data, dt.datetime):
            data = data.date()
        meta["data"] = data
        meta["data_pt"] = data_pt(data)
        meta["data_curta"] = data_curta(data)
        meta["iso"] = data.isoformat()
        for fonte in meta.get("fontes") or []:
            fonte["dominio"] = dominio(fonte["url"])
        meta["slug"] = meta.get("slug") or re.sub(r"^\d{4}-\d{2}-\d{2}-", "", f.stem)
        meta["corpo_html"] = markdown.markdown(corpo, extensions=["extra", "sane_lists"])
        palavras = len(re.findall(r"\w+", corpo))
        meta["leitura"] = max(1, math.ceil(palavras / 200))
        meta["palavras"] = palavras
        itens.append(meta)
    itens.sort(key=lambda x: (x["data"], x.get("hora", "00:00")), reverse=True)
    return itens


def preparar_noticia(n):
    rot, cor = NIVEIS.get(n.get("nivel", "INFO"), NIVEIS["INFO"])
    n["rotulo"], n["cor"] = rot, cor
    n["arte"] = ilustracao(n.get("ilustracao", "escudo"), cor)
    n["seccao"] = SECCOES.get(n.get("tema", "tecnologia"), "Tecnologia")
    n["url"] = f"noticias/{n['slug']}/"
    n["caixa"] = n.get("caixa", "O QUE FAZER")
    return n


def env():
    e = Environment(loader=FileSystemLoader(ROOT / "templates"), autoescape=select_autoescape(["html", "xml"]))
    e.globals.update(site=SITE, ano=dt.date.today().year, seccoes=SECCOES)
    return e


def escrever(caminho, conteudo):
    p = OUT / caminho
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(conteudo, encoding="utf-8")


def render(e, tpl, destino, **ctx):
    profundidade = destino.count("/")
    ctx.setdefault("root", "../" * profundidade)
    ctx.setdefault("caminho", destino.replace("index.html", ""))
    escrever(destino, e.get_template(tpl).render(**ctx))


def gerar_og(itens):
    """Imagens 1200x630 para a pré-visualização dos links (WhatsApp, Facebook, X)."""
    from playwright.sync_api import sync_playwright
    tpl = env().get_template("og.html")
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1200, "height": 630})
        for it in itens:
            destino = OUT / it["og"]
            destino.parent.mkdir(parents=True, exist_ok=True)
            pg.set_content(tpl.render(it=it))
            pg.wait_for_timeout(150)
            pg.screenshot(path=str(destino))
        b.close()


def main():
    com_og = "--og" in sys.argv
    og_antigas = {}
    if OUT.exists():  # guarda as imagens de pré-visualização já geradas
        for f in (OUT / "og").glob("*.png") if (OUT / "og").exists() else []:
            og_antigas[f.name] = f.read_bytes()
        shutil.rmtree(OUT)
    OUT.mkdir()
    shutil.copytree(ROOT / "static", OUT / "static")
    (OUT / ".nojekyll").write_text("")
    if SITE.get("dominio"):
        (OUT / "CNAME").write_text(SITE["dominio"] + "\n")

    e = env()
    noticias = [preparar_noticia(n) for n in ler("noticias")]
    fichas = ler("fichas")
    for f in fichas:
        f["cor"] = SEVERIDADE.get(f.get("severidade", "ALTA"), "#d9822b")
        f["pct"] = round(float(str(f.get("nota", "0")).replace(",", ".")) * 10)
        f["url"] = f"fichas/{f['slug']}/"
    dicas = ler("dicas")
    for d in dicas:
        d["cor"] = NIVEIS["DICA"][1]
        d["arte"] = ilustracao(d.get("ilustracao", "escudo"), d["cor"])
        d["url"] = f"dicas/{d['slug']}/"
    e.globals["seccoes"] = {k: v for k, v in SECCOES.items() if any(n.get("tema") == k for n in noticias)}

    for n in noticias:
        n["og"] = f"og/{n['slug']}.png"
    for f in fichas:
        f["og"] = f"og/ficha-{f['slug']}.png"
    for d in dicas:
        d["og"] = f"og/dica-{d['slug']}.png"

    # páginas
    render(e, "index.html", "index.html", noticias=noticias, fichas=fichas, dicas=dicas, menu="inicio")
    render(e, "lista.html", "noticias/index.html", titulo="Notícias", itens=noticias,
           descricao="Todas as notícias de cibersegurança, tecnologia e vida digital, explicadas com mais detalhe.")
    for chave, nome in SECCOES.items():
        sel = [n for n in noticias if n.get("tema") == chave]
        if sel:
            render(e, "lista.html", f"seccao/{chave}/index.html", titulo=nome, itens=sel,
                   descricao=f"Notícias da secção {nome}.")
    for n in noticias:
        rel = [x for x in noticias if x is not n and x.get("tema") == n.get("tema")][:3] or \
              [x for x in noticias if x is not n][:3]
        ficha = next((f for f in fichas if f.get("noticia") == n["slug"]), None)
        render(e, "artigo.html", f"{n['url']}index.html", it=n, relacionados=rel, ficha=ficha, og=n["og"])
    render(e, "fichas.html", "fichas/index.html", itens=fichas)
    for f in fichas:
        noticia = next((n for n in noticias if n["slug"] == f.get("noticia")), None)
        render(e, "ficha.html", f"{f['url']}index.html", it=f, noticia=noticia, og=f["og"])
    render(e, "dicas.html", "dicas/index.html", itens=dicas)
    for d in dicas:
        render(e, "dica.html", f"{d['url']}index.html", it=d, outras=[x for x in dicas if x is not d][:4], og=d["og"])
    sobre = (CONTENT / "sobre.md").read_text(encoding="utf-8")
    render(e, "pagina.html", "sobre/index.html", titulo="Sobre",
           corpo_html=markdown.markdown(sobre, extensions=["extra"]))
    render(e, "404.html", "404.html", root=SITE.get("caminho_base", "/"))

    # RSS e sitemap
    base = SITE.get("url", "").rstrip("/") + "/"
    todos = sorted(noticias + fichas + dicas, key=lambda x: x["data"], reverse=True)
    for it in todos:
        it["rfc822"] = format_datetime(dt.datetime.combine(it["data"], dt.time(8, 0), dt.timezone(dt.timedelta(hours=1))))
    escrever("feed.xml", e.get_template("feed.xml").render(itens=todos[:30], base=base))
    urls = ["", "noticias/", "fichas/", "dicas/", "sobre/"] + [it["url"] for it in todos]
    escrever("sitemap.xml", "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<urlset xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\">\n"
             + "".join(f"  <url><loc>{html.escape(base + u)}</loc></url>\n" for u in urls) + "</urlset>\n")
    escrever("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {base}sitemap.xml\n")

    # imagens de pré-visualização
    (OUT / "og").mkdir(exist_ok=True)
    for nome, dados in og_antigas.items():
        (OUT / "og" / nome).write_bytes(dados)
    falta = [it for it in todos if not (OUT / it["og"]).exists()]
    if com_og and falta:
        for it in falta:
            it.setdefault("arte", ilustracao(it.get("ilustracao", "escudo"), it["cor"]))
            it.setdefault("rotulo", "Ficha da falha" if it in fichas else NIVEIS["DICA"][0] if it in dicas else "")
        gerar_og(falta)
    print(f"Site gerado em {OUT}: {len(noticias)} notícias, {len(fichas)} fichas, {len(dicas)} dicas"
          + (f", {len(falta)} imagens de pré-visualização novas" if com_og else ""))


if __name__ == "__main__":
    main()
