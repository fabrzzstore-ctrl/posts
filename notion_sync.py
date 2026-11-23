"""Ponte Notion -> blog.

Vai buscar à base de dados "Blog noticias.semwhere" do Notion as páginas com Estado = Publicar,
grava o artigo (o bloco de código Markdown da página) em content/<Ficheiro>.md e, depois de
publicado, muda o Estado para Publicado e preenche o Link.
A página com Ficheiro "dados/ataques" leva um bloco de código YAML com os dados da página
"Ataques em curso" e é gravada em content/ataques.yaml.

Uso (no GitHub Actions, com o segredo NOTION_TOKEN):
    python3 notion_sync.py buscar    # grava os ficheiros novos e a lista em .notion_pendentes.json
    python3 notion_sync.py marcar    # marca as páginas gravadas como Publicado
Só usa a biblioteca padrão do Python.
"""
import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

import yaml

ROOT = Path(__file__).parent
SITE = yaml.safe_load((ROOT / "site.yaml").read_text(encoding="utf-8"))
TOKEN = os.environ.get("NOTION_TOKEN", "").strip()
DB = str(SITE.get("notion_db", "")).replace("-", "")
PENDENTES = ROOT / ".notion_pendentes.json"
CAMINHO = re.compile(r"^(noticias|fichas|dicas)/(\d{4}-\d{2}-\d{2})-([a-z0-9]+(?:-[a-z0-9]+)*)$")
DADOS = {"dados/ataques": ("ataques.yaml", "ataques/")}  # Ficheiro -> (ficheiro em content/, página do site)


def api(metodo, caminho, dados=None):
    req = urllib.request.Request(
        "https://api.notion.com/v1/" + caminho,
        method=metodo,
        data=json.dumps(dados).encode() if dados is not None else None,
        headers={"Authorization": "Bearer " + TOKEN, "Notion-Version": "2022-06-28",
                 "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode())


def texto(rich):
    return "".join(t.get("plain_text", "") for t in rich or [])


def conteudo_da_pagina(pid):
    partes, cursor = [], None
    while True:
        q = "?page_size=100" + (f"&start_cursor={cursor}" if cursor else "")
        r = api("GET", f"blocks/{pid}/children{q}")
        for b in r.get("results", []):
            if b.get("type") == "code":
                partes.append(texto(b["code"].get("rich_text")))
        if not r.get("has_more"):
            break
        cursor = r.get("next_cursor")
    md = ""
    for p in partes:
        if md and not md.endswith("\n") and not p.startswith("\n"):
            md += "\n"
        md += p
    return md.strip() + "\n"


def link(caminho):
    if caminho in DADOS:
        return SITE["url"].rstrip("/") + "/" + DADOS[caminho][1]
    tipo, _data, slug = CAMINHO.match(caminho).groups()
    return SITE["url"].rstrip("/") + f"/{tipo}/{slug}/"


def marcar_erro(pid, motivo):
    print("ERRO:", pid, motivo)
    try:
        api("PATCH", f"pages/{pid}", {"properties": {"Estado": {"select": {"name": "Erro"}}}})
    except Exception as e:  # noqa: BLE001
        print("  não foi possível marcar o erro:", e)


def buscar():
    if not TOKEN or not DB:
        print("Sem NOTION_TOKEN ou notion_db: nada a fazer.")
        PENDENTES.write_text("[]")
        return
    paginas, cursor = [], None
    while True:
        corpo = {"filter": {"property": "Estado", "select": {"equals": "Publicar"}}, "page_size": 100}
        if cursor:
            corpo["start_cursor"] = cursor
        r = api("POST", f"databases/{DB}/query", corpo)
        paginas += r.get("results", [])
        if not r.get("has_more"):
            break
        cursor = r.get("next_cursor")
    gravadas = []
    for p in paginas:
        pid = p["id"]
        caminho = texto(p["properties"]["Ficheiro"]["title"]).strip()
        caminho = re.sub(r"\.(md|ya?ml)$", "", caminho)
        if caminho in DADOS:
            texto_yaml = conteudo_da_pagina(pid)
            try:
                dados = yaml.safe_load(texto_yaml)
            except yaml.YAMLError as e:
                marcar_erro(pid, f"{caminho}: YAML inválido ({e})")
                continue
            if not isinstance(dados, dict) or not isinstance(dados.get("ataques"), list):
                marcar_erro(pid, f"{caminho}: o YAML tem de ter a lista 'ataques'")
                continue
            destino = ROOT / "content" / DADOS[caminho][0]
            destino.write_text(texto_yaml, encoding="utf-8")
            gravadas.append({"id": pid, "caminho": caminho})
            print("Gravado:", destino.relative_to(ROOT))
            continue
        if not CAMINHO.match(caminho):
            marcar_erro(pid, f"caminho inválido: {caminho!r}")
            continue
        md = conteudo_da_pagina(pid)
        if not md.startswith("---\n") or "\n---\n" not in md[4:]:
            marcar_erro(pid, f"{caminho}: o bloco de código não começa com o cabeçalho ---")
            continue
        try:
            yaml.safe_load(md[4:].split("\n---\n", 1)[0])
        except yaml.YAMLError as e:
            marcar_erro(pid, f"{caminho}: cabeçalho YAML inválido ({e})")
            continue
        destino = ROOT / "content" / f"{caminho}.md"
        destino.parent.mkdir(parents=True, exist_ok=True)
        destino.write_text(md, encoding="utf-8")
        gravadas.append({"id": pid, "caminho": caminho})
        print("Gravado:", destino.relative_to(ROOT))
    PENDENTES.write_text(json.dumps(gravadas))
    print(f"{len(gravadas)} artigo(s) novo(s) do Notion.")


def marcar():
    if not PENDENTES.exists():
        return
    for g in json.loads(PENDENTES.read_text()):
        api("PATCH", f"pages/{g['id']}", {"properties": {
            "Estado": {"select": {"name": "Publicado"}},
            "Link": {"url": link(g["caminho"])},
        }})
        print("Publicado:", g["caminho"])
    PENDENTES.unlink()


MOTIVOS = {
    401: "a chave do Notion (segredo NOTION_TOKEN ou NOTION_SECRET) não é válida. Copie de novo o "
         "'Internal Integration Secret' da integração e cole-o no segredo do GitHub.",
    403: "a integração do Notion não tem permissão para ler esta base de dados.",
    404: "a integração não encontra a base de dados. Abra a base 'Blog noticias.semwhere' no Notion, "
         "menu ··· > Ligações (Connections) e adicione a integração.",
}

if __name__ == "__main__":
    try:
        {"buscar": buscar, "marcar": marcar}[sys.argv[1]]()
    except urllib.error.HTTPError as e:
        # Um problema no Notion não pode impedir a publicação do resto do site.
        print(f"::warning::Notion respondeu {e.code}: {MOTIVOS.get(e.code, e.reason)}")
        if sys.argv[1] == "buscar":
            PENDENTES.write_text("[]")
    except urllib.error.URLError as e:
        print(f"::warning::Não foi possível ligar ao Notion: {e.reason}")
        if sys.argv[1] == "buscar":
            PENDENTES.write_text("[]")
