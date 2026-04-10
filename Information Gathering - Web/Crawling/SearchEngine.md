# Descoberta com Motores de Busca

A descoberta com motores de busca (Search Engine Discovery), também chamada de coleta de **OSINT** (*Open Source Intelligence*), usa mecanismos de busca para encontrar informações públicas sobre sites, organizações e pessoas.

No reconhecimento web, essa abordagem ajuda a identificar documentos expostos, páginas de login, tecnologias em uso e outros dados úteis para análise de segurança.

## Por que isso importa

- **Fonte aberta:** os dados são públicos, o que torna a coleta legal e ética quando usada corretamente.
- **Ampla cobertura:** motores de busca indexam grande parte da web.
- **Facilidade de uso:** não exige conhecimento técnico avançado para começar.
- **Baixo custo:** é um recurso gratuito e amplamente disponível.

## Aplicações comuns

- **Avaliação de segurança:** identificar dados expostos e possíveis vetores de ataque.
- **Inteligência competitiva:** mapear produtos, serviços e estratégias de concorrentes.
- **Jornalismo investigativo:** descobrir conexões ocultas e práticas suspeitas.
- **Threat intelligence:** acompanhar atores maliciosos e tendências de ataque.

## Limitações

Nem tudo é indexado por mecanismos de busca. Parte das informações pode estar protegida, não indexada ou deliberadamente oculta.

## Operadores de busca

Operadores de busca aumentam a precisão das consultas e permitem filtrar resultados de forma mais estratégica.

| Operador | Descrição | Exemplo | O que retorna |
|---|---|---|---|
| `site:` | Limita resultados a um site ou domínio. | `site:example.com` | Páginas públicas de `example.com`. |
| `inurl:` | Busca termo específico na URL. | `inurl:login` | Páginas com “login” na URL. |
| `filetype:` | Filtra por tipo de arquivo. | `filetype:pdf` | Arquivos PDF disponíveis para download. |
| `intitle:` | Busca termo no título da página. | `intitle:"relatório confidencial"` | Páginas com esse título (ou variações próximas). |
| `intext:` / `inbody:` | Busca termo no corpo do texto. | `intext:"password reset"` | Páginas contendo “password reset”. |
| `cache:` | Exibe versão em cache de uma página. | `cache:example.com` | Conteúdo armazenado anteriormente no cache. |
| `link:` | Lista páginas que apontam para uma URL. | `link:example.com` | Sites que possuem links para `example.com`. |
| `related:` | Encontra sites semelhantes. | `related:example.com` | Domínios relacionados a `example.com`. |
| `info:` | Mostra resumo de uma página. | `info:example.com` | Detalhes básicos como título e descrição. |
| `define:` | Retorna definições de termos. | `define:phishing` | Definições de “phishing” em diferentes fontes. |
| `numrange:` | Busca números em intervalo específico. | `site:example.com numrange:1000-2000` | Páginas com números entre 1000 e 2000. |
| `allintext:` | Exige todos os termos no corpo do texto. | `allintext:admin password reset` | Páginas com “admin” e “password reset”. |
| `allinurl:` | Exige todos os termos na URL. | `allinurl:admin panel` | URLs contendo “admin” e “panel”. |
| `allintitle:` | Exige todos os termos no título. | `allintitle:confidential report 2023` | Títulos com “confidential”, “report” e “2023”. |
| `AND` | Obriga presença de todos os termos. | `site:example.com AND (inurl:admin OR inurl:login)` | Páginas de admin/login dentro de `example.com`. |
| `OR` | Retorna resultados com qualquer termo. | `"linux" OR "ubuntu" OR "debian"` | Páginas que mencionam qualquer um dos termos. |
| `NOT` | Exclui termo dos resultados. | `site:bank.com NOT inurl:login` | Páginas de `bank.com` sem URLs de login. |
| `*` (coringa) | Representa palavra/caractere variável. | `site:socialnetwork.com filetype:pdf user* manual` | Manuais de usuário em PDF (ex.: guide, handbook). |
| `..` (intervalo) | Limita busca por faixa numérica. | `site:ecommerce.com "price" 100..500` | Produtos entre 100 e 500. |
| `" "` (aspas) | Busca expressão exata. | `"information security policy"` | Páginas com a frase exata. |
| `-` (menos) | Remove termos da consulta. | `site:news.com -inurl:sports` | Notícias sem conteúdo de esportes na URL. |

## Google Dorking

**Google Dorking** (ou Google Hacking) é o uso avançado de operadores no Google para encontrar dados sensíveis, falhas de segurança e conteúdo oculto.

Exemplos comuns:

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

### Encontrar arquivos de configuração

```text
site:example.com inurl:config.php
site:example.com (ext:conf OR ext:cnf)
```

### Localizar backups de banco de dados

```text
site:example.com inurl:backup
site:example.com filetype:sql
```
