# Introdução ao Web Gathering

O **Web Gathering** (ou *Web Reconnaissance*) é a etapa inicial de uma avaliação de segurança.
Seu objetivo é coletar informações sobre o alvo (site, aplicação, domínio e infraestrutura) antes de qualquer teste mais profundo.

## Onde essa etapa entra no pentest

Fluxo simplificado:

**Pré-engajamento → Coleta de informações → Avaliação de vulnerabilidades → Exploração → Pós-exploração**

## Objetivos principais

- **Identificar ativos expostos:** páginas, subdomínios, IPs, serviços e tecnologias.
- **Descobrir informações sensíveis:** arquivos de backup, configurações e dados públicos úteis.
- **Mapear a superfície de ataque:** possíveis pontos de entrada e fraquezas técnicas.
- **Gerar inteligência de contexto:** dados que apoiem análises técnicas e cenários de engenharia social.

Essas informações podem ser usadas tanto por atacantes (para personalizar ataques) quanto por defensores (para corrigir riscos antes de incidentes).

## Tipos de reconhecimento

### Reconhecimento ativo

Há interação direta com o alvo.
Gera dados mais detalhados, porém com **maior risco de detecção**.

Exemplos:
- Varredura de portas e serviços (`nmap`, `masscan`)
- Varredura de vulnerabilidades (`nessus`, `openvas`, `nikto`)
- Enumeração de versões e banners (`nmap -sV`, `curl`, `netcat`)
- Spider/crawling de aplicações (`Burp`, `OWASP ZAP`)

### Reconhecimento passivo

Não há interação direta com o alvo.
Usa fontes públicas e tem **baixo risco de detecção**, mas pode trazer menos profundidade.

Exemplos:
- Buscas em mecanismos de pesquisa
- Consultas `WHOIS`
- Levantamento de registros DNS (`dig`, `nslookup`)
- Wayback Machine e outros arquivos web
- Redes sociais e repositórios públicos (GitHub/GitLab)

## Resumo prático

| Tipo | Interação direta | Profundidade | Risco de detecção |
|---|---|---|---|
| Ativo | Sim | Alta | Médio/Alto |
| Passivo | Não | Média | Baixo |

## Conclusão

Web Gathering é a base de qualquer teste de segurança web bem feito.
Neste módulo, o próximo passo é começar por **WHOIS**, que ajuda a entender propriedade de domínio, contatos e estrutura inicial do alvo.
