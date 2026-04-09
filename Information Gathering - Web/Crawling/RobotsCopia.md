# robots.txt

Imagine que você é convidado para uma grande festa em uma casa. Você pode circular pelos ambientes, mas alguns cômodos estão marcados como “Privado” e devem ser evitados. O `robots.txt` funciona de forma parecida no contexto de crawling: ele age como um guia de etiqueta para bots, indicando quais áreas de um site podem ser acessadas e quais estão fora de alcance.

## O que é robots.txt?

Tecnicamente, o `robots.txt` é um arquivo de texto simples colocado na raiz de um site (por exemplo: `www.example.com/robots.txt`). Ele segue o **Robots Exclusion Standard**, um conjunto de diretrizes sobre como crawlers devem se comportar ao visitar um site.  
Esse arquivo contém instruções (diretivas) que dizem aos bots quais partes do site podem e não podem ser rastreadas.

## Como o robots.txt funciona

As diretivas normalmente são aplicadas a **user-agents** específicos (identificadores de bots). Exemplo:

```txt
User-agent: *
Disallow: /private/
```

Esse bloco informa que todos os user-agents (`*`) não devem acessar URLs que começam com `/private/`.  
Outras diretivas podem permitir acesso a caminhos específicos, definir atraso entre requisições para reduzir carga no servidor ou indicar o sitemap.

## Estrutura do robots.txt

O `robots.txt` é um texto plano na raiz do site. Ele é organizado em blocos (registros), separados por linha em branco.

Cada bloco contém:

- **User-agent:** define para qual bot as regras se aplicam.
- **Diretivas:** regras de acesso para o user-agent definido.

Diretivas comuns:

| Diretiva | Descrição | Exemplo |
|---|---|---|
| `Disallow` | Define caminhos/padrões que o bot não deve rastrear. | `Disallow: /admin/` |
| `Allow` | Permite rastrear caminhos específicos, mesmo sob regra de bloqueio mais ampla. | `Allow: /public/` |
| `Crawl-delay` | Define intervalo (em segundos) entre requisições do bot. | `Crawl-delay: 10` |
| `Sitemap` | Indica a URL do sitemap XML para crawling mais eficiente. | `Sitemap: https://www.example.com/sitemap.xml` |

## Por que respeitar o robots.txt?

Embora não seja tecnicamente obrigatório (bots maliciosos podem ignorar), crawlers legítimos e mecanismos de busca normalmente respeitam o arquivo.

Isso é importante para:

- **Evitar sobrecarga no servidor:** limita tráfego automatizado em áreas específicas.
- **Reduzir exposição em indexação:** ajuda a evitar indexação de conteúdo privado.
- **Conformidade legal e ética:** ignorar diretivas pode violar termos de serviço e, dependendo do caso, gerar implicações legais.

## robots.txt em reconhecimento web

No reconhecimento web, o `robots.txt` é uma fonte útil de inteligência. Mesmo respeitando as diretivas, ele pode revelar pistas relevantes:

- **Diretórios ocultos:** caminhos bloqueados podem apontar para áreas sensíveis (`/admin/`, backups, etc.).
- **Estrutura do site:** caminhos permitidos e bloqueados ajudam a mapear seções não visíveis na navegação principal.
- **Possíveis armadilhas de crawler:** alguns sites publicam diretórios isca (*honeypots*) para detectar bots maliciosos.

## Analisando um robots.txt

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

Interpretação:

- Todos os bots estão bloqueados em `/admin/` e `/private/`.
- Todos os bots podem acessar `/public/`.
- O `Googlebot` deve aguardar 10 segundos entre requisições.
- O sitemap foi declarado para facilitar rastreamento e indexação.

Com essa análise, é razoável inferir que há um painel administrativo em `/admin/` e conteúdo sensível em `/private/`.
