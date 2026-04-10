# Descoberta com Motores de Busca

Os motores de busca funcionam como guias em meio ao enorme volume de informação da internet. Além de responder pesquisas do dia a dia, eles também concentram dados valiosos para reconhecimento web e coleta de informações.

Essa prática, conhecida como **Search Engine Discovery** ou coleta de **OSINT** (*Open Source Intelligence*), consiste em usar mecanismos de busca para descobrir informações sobre sites-alvo, organizações e indivíduos.

Na prática, a descoberta com motores de busca aproveita o poder dos algoritmos de indexação para extrair dados que nem sempre estão visíveis de forma direta dentro de um site. Profissionais de segurança e pesquisadores podem usar operadores avançados, técnicas e ferramentas para encontrar desde informações de colaboradores e documentos sensíveis até páginas de login ocultas e credenciais expostas.

## Por que a descoberta com motores de busca importa

A descoberta via motores de busca é um componente essencial do reconhecimento web por vários motivos:

- **Código aberto (Open Source):** as informações coletadas são públicas, o que torna essa prática um meio legal e ético de obter inteligência sobre um alvo.
- **Amplitude de informação:** motores de busca indexam uma porção significativa da web, oferecendo grande variedade de fontes.
- **Facilidade de uso:** são ferramentas acessíveis e não exigem habilidades técnicas avançadas para uso básico.
- **Custo-benefício:** é um recurso gratuito e prontamente disponível.

As informações extraídas também podem ser aplicadas em diferentes contextos:

- **Avaliação de segurança:** identificação de vulnerabilidades, dados expostos e possíveis vetores de ataque.
- **Inteligência competitiva:** coleta de dados sobre produtos, serviços e estratégias de concorrentes.
- **Jornalismo investigativo:** descoberta de conexões ocultas, movimentações financeiras e práticas antiéticas.
- **Threat intelligence:** identificação de ameaças emergentes, rastreamento de atores maliciosos e previsão de ataques.

Mesmo assim, existem limitações: mecanismos de busca não indexam tudo, e parte dos dados pode estar protegida ou deliberadamente oculta.

## Operadores de busca

Operadores de busca funcionam como “códigos secretos” dos mecanismos de pesquisa. Esses comandos especiais aumentam a precisão das consultas e permitem localizar tipos específicos de informação dentro da web indexada.

Embora a sintaxe possa variar ligeiramente entre buscadores, os princípios gerais permanecem os mesmos.

| Operador | Descrição do operador | Exemplo | Descrição do exemplo |
|---|---|---|---|
| `site:` | Limita os resultados a um site ou domínio específico. | `site:example.com` | Encontra páginas públicas de `example.com`. |
| `inurl:` | Encontra páginas com um termo específico na URL. | `inurl:login` | Procura páginas de login em qualquer site. |
| `filetype:` | Busca arquivos de um tipo específico. | `filetype:pdf` | Localiza documentos PDF disponíveis para download. |
| `intitle:` | Busca páginas com um termo específico no título. | `intitle:"confidential report"` | Localiza documentos com título “confidential report” ou variações semelhantes. |
| `intext:` ou `inbody:` | Busca termo no corpo do texto da página. | `intext:"password reset"` | Identifica páginas que contenham o termo “password reset”. |
| `cache:` | Exibe a versão em cache de uma página (quando disponível). | `cache:example.com` | Mostra conteúdo anterior de `example.com` salvo em cache. |
| `link:` | Encontra páginas que apontam para uma URL específica. | `link:example.com` | Identifica sites que possuem links para `example.com`. |
| `related:` | Encontra sites relacionados a uma página específica. | `related:example.com` | Descobre sites semelhantes a `example.com`. |
| `info:` | Exibe um resumo de informações sobre uma página. | `info:example.com` | Mostra detalhes básicos, como título e descrição de `example.com`. |
| `define:` | Retorna definições de uma palavra ou expressão. | `define:phishing` | Obtém definições de “phishing” em múltiplas fontes. |
| `numrange:` | Busca números dentro de um intervalo específico. | `site:example.com numrange:1000-2000` | Encontra páginas de `example.com` com números entre 1000 e 2000. |
| `allintext:` | Encontra páginas que contenham todos os termos no corpo do texto. | `allintext:admin password reset` | Busca páginas com “admin” e “password reset” no corpo do texto. |
| `allinurl:` | Encontra páginas que contenham todos os termos na URL. | `allinurl:admin panel` | Procura páginas com “admin” e “panel” na URL. |
| `allintitle:` | Encontra páginas que contenham todos os termos no título. | `allintitle:confidential report 2023` | Busca páginas com “confidential”, “report” e “2023” no título. |
| `AND` | Restringe os resultados exigindo todos os termos. | `site:example.com AND (inurl:admin OR inurl:login)` | Encontra páginas de admin/login especificamente em `example.com`. |
| `OR` | Amplia os resultados incluindo qualquer um dos termos. | `"linux" OR "ubuntu" OR "debian"` | Busca páginas que mencionem Linux, Ubuntu ou Debian. |
| `NOT` | Exclui resultados com o termo especificado. | `site:bank.com NOT inurl:login` | Encontra páginas de `bank.com`, excluindo páginas de login. |
| `*` (coringa) | Representa qualquer palavra ou caractere. | `site:socialnetwork.com filetype:pdf user* manual` | Procura manuais de usuário em PDF (ex.: *user guide*, *user handbook*). |
| `..` (busca por intervalo) | Encontra resultados em uma faixa numérica específica. | `site:ecommerce.com "price" 100..500` | Procura produtos entre 100 e 500 em um e-commerce. |
| `" "` (aspas) | Busca uma frase exata. | `"information security policy"` | Encontra documentos com a frase exata “information security policy”. |
| `-` (sinal de menos) | Exclui termos dos resultados. | `site:news.com -inurl:sports` | Busca notícias em `news.com`, excluindo conteúdo esportivo na URL. |

## Google Dorking

**Google Dorking** (também chamado de Google Hacking) é uma técnica que usa operadores de busca no Google para localizar informações sensíveis, vulnerabilidades de segurança ou conteúdo oculto em sites.

Alguns exemplos comuns de Google Dorks:

### Encontrar páginas de login

```text
site:example.com inurl:login
site:example.com (inurl:login OR inurl:admin)
```

### Identificar arquivos expostos

```text
site:example.com filetype:pdf
site:example.com (filetype:xls OR filetype:docx)
```

### Descobrir arquivos de configuração

```text
site:example.com inurl:config.php
site:example.com (ext:conf OR ext:cnf) (extensões comuns de arquivos de configuração)
```

### Localizar backups de banco de dados

```text
site:example.com inurl:backup
site:example.com filetype:sql
```

Para mais exemplos, consulte a **Google Hacking Database (GHDB)**.
