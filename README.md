# Blog noticias.semwhere

Site estático do noticias.semwhere, com notícias, fichas das falhas e dicas de segurança. É publicado no GitHub Pages, de graça. Sempre que se envia um ficheiro novo para o repositório, o GitHub gera e publica o site sozinho.

## Publicar pela primeira vez (cerca de 10 minutos)

1. Crie uma conta em https://github.com, por exemplo com o nome `noticias-semwhere`.
2. Crie um repositório novo e **público**. Se lhe chamar `noticias-semwhere.github.io` (o nome da conta seguido de `.github.io`), o site fica em https://noticias-semwhere.github.io. Com outro nome, fica em `https://<conta>.github.io/<repositório>/`.
3. No repositório, escolha **Add file → Upload files** e arraste **todo o conteúdo** desta pasta, incluindo a pasta `.github`. Não precisa de enviar a pasta `docs`, porque o GitHub gera-a.
4. Vá a **Settings → Pages** e, em **Source**, escolha **GitHub Actions**.
5. No separador **Actions**, espere que o processo "Publicar o blog" fique verde (2 a 4 minutos). O site fica online.
6. Abra o `site.yaml` no GitHub (lápis para editar) e confirme:
   - `url`: o endereço do site;
   - `caminho_base`: `/` se o repositório for `<conta>.github.io`, ou `/<repositório>/` no outro caso;
   - `canal_whatsapp`: o link de convite do Canal, para aparecerem os botões "Seguir o Canal".

## Domínio próprio (opcional)

Depois de comprar um domínio (por exemplo `noticiassemwhere.com`), escreva-o em `dominio:` no `site.yaml` e siga as instruções de **Settings → Pages → Custom domain** para configurar o DNS.

## Acrescentar conteúdo

Cada artigo é um ficheiro de texto em `content/`. Para publicar, basta acrescentar o ficheiro ao repositório.

- Notícias: `content/noticias/AAAA-MM-DD-titulo-curto.md`
- Fichas das falhas: `content/fichas/AAAA-MM-DD-nome.md`
- Dicas: `content/dicas/AAAA-MM-DD-titulo-curto.md`
- Página "Sobre": `content/sobre.md`

Modelo de notícia:

```markdown
---
titulo: Título da notícia (máx. 60 caracteres)
resumo: Duas frases que resumem a notícia.
data: 2026-11-19
nivel: ALTO          # CRÍTICO, ALTO, MÉDIO, INFO ou NOVIDADE
tema: ciberseguranca # ciberseguranca, tecnologia, gaming, fintech, emprego, angola, startups
ilustracao: cadeia   # cripto, firewall, vpn, cadeia, fuga-dados, conta, grafico, portatil, cloud, phishing, telemovel, ia, gaming, escudo
caixa: O QUE FAZER   # ou PORQUE IMPORTA
acao: O conselho ou a consequência para o leitor.
fontes:
  - nome: "Nome da fonte: título do artigo"
    url: https://...
---
Texto do artigo em Markdown, com subtítulos "## ...".
```

## Ver o site no computador (opcional)

```
pip install -r requirements.txt
python3 build.py --og
python3 -m http.server -d docs
```

Depois abra http://localhost:8000.
