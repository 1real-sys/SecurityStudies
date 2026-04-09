# robots.txt

`robots.txt` é um arquivo de texto na raiz do site (ex.: `www.example.com/robots.txt`) que orienta crawlers sobre quais áreas podem ou não ser rastreadas.

## Como funciona

As regras são aplicadas por **user-agent**:

```txt
User-agent: *
Disallow: /private/
```

Esse exemplo bloqueia todos os bots (`*`) de acessarem caminhos iniciados por `/private/`.

## Estrutura e diretivas

Cada bloco do arquivo contém:

- **User-agent:** bot alvo da regra.
- **Diretivas:** regras de acesso.

Diretivas comuns:

| Diretiva | Função | Exemplo |
|---|---|---|
| `Disallow` | Bloqueia caminhos | `Disallow: /admin/` |
| `Allow` | Permite caminhos específicos | `Allow: /public/` |
| `Crawl-delay` | Intervalo entre requisições | `Crawl-delay: 10` |
| `Sitemap` | URL do sitemap XML | `Sitemap: https://www.example.com/sitemap.xml` |

## Por que respeitar

- Reduz sobrecarga no servidor.
- Evita indexação indesejada de conteúdo sensível.
- Ajuda em conformidade legal e ética.

## Uso em reconhecimento web

- Pode revelar diretórios ocultos (`/admin/`, `/private/`).
- Ajuda a mapear estrutura não visível na navegação.
- Pode indicar armadilhas para bots (*honeypots*).

Exemplo:

```txt
User-agent: *
Disallow: /admin/
Disallow: /private/
Allow: /public/

User-agent: Googlebot
Crawl-delay: 10

Sitemap: https://www.example.com/sitemap.xml
```

Inferência: há forte indicação de área administrativa em `/admin/` e conteúdo sensível em `/private/`.
