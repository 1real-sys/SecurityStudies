# Fingerprinting

Extração de detalhes técnicos sobre as tecnologias que alimentam um site. As assinaturas digitais de servidores web, sistemas operacionais e componentes de software revelam informações críticas sobre a infraestrutura e potenciais fraquezas de segurança.

## Por que é importante?

| Razão | Descrição |
|-------|-----------|
| **Ataques Direcionados** | Conhecer tecnologias permite focar em exploits específicos |
| **Identificar Configurações Incorretas** | Expõe software desatualizado ou configurações padrão |
| **Priorizar Alvos** | Identifica sistemas mais propensos a vulnerabilidades |
| **Perfil Abrangente** | Visão holística da postura de segurança |

## Técnicas de Fingerprinting

| Técnica | Descrição |
|---------|-----------|
| **Banner Grabbing** | Analisa banners de servidores (software, versão) |
| **Análise de Headers HTTP** | Headers `Server`, `X-Powered-By` revelam tecnologias |
| **Sondagem por Respostas** | Requisições especiais provocam respostas únicas |
| **Análise de Conteúdo** | Estrutura, scripts, copyrights indicam tecnologias |

## Ferramentas

| Ferramenta | Descrição | Tipo |
|------------|-----------|------|
| **Wappalyzer** | Extensão de navegador para perfil de tecnologias | Passivo |
| **BuiltWith** | Relatórios detalhados da stack de tecnologia | Passivo |
| **WhatWeb** | Fingerprinting via linha de comando | Ativo |
| **Nmap** | Scanner versátil com scripts NSE | Ativo |
| **Netcraft** | Serviços de segurança e relatórios | Passivo |
| **wafw00f** | Detecta Web Application Firewalls (WAFs) | Ativo |
| **Nikto** | Scanner de vulnerabilidades e fingerprinting | Ativo |

---

## Banner Grabbing com curl

```bash
# Buscar apenas headers HTTP
curl -I dominio.com

# Seguir redirecionamentos
curl -I https://dominio.com
curl -I https://www.dominio.com
```

**Exemplo de saída:**
```
HTTP/1.1 200 OK
Server: Apache/2.4.41 (Ubuntu)
X-Redirect-By: WordPress
Link: <https://www.dominio.com/index.php/wp-json/>; rel="https://api.w.org/"
```

**O que observar:**
- `Server:` → Software e versão do servidor
- `X-Powered-By:` → Linguagem/framework (PHP, ASP.NET)
- `X-Redirect-By:` → CMS fazendo redirecionamento
- Paths com `wp-` → WordPress

---

## Detecção de WAF com wafw00f

```bash
# Instalação
pip3 install git+https://github.com/EnableSecurity/wafw00f

# Uso
wafw00f dominio.com
```

**Saída:**
```
[+] The site https://dominio.com is behind Wordfence (Defiant) WAF.
```

> **Importante:** Se um WAF estiver presente, pode bloquear requisições de reconhecimento. Adapte técnicas conforme necessário.

---

## Nikto - Scanner de Servidor Web

```bash
# Instalação
sudo apt update && sudo apt install -y nikto
# ou
git clone https://github.com/sullo/nikto && cd nikto/program && chmod +x ./nikto.pl

# Apenas fingerprinting (módulos de identificação de software)
nikto -h dominio.com -Tuning b

# Scan completo
nikto -h dominio.com
```

**Parâmetros:**
- `-h`: Host alvo
- `-Tuning b`: Apenas módulos de identificação de software

**Informações obtidas:**
- IPs (IPv4 e IPv6)
- Certificado SSL (emissor, domínios)
- Servidor e versão
- CMS detectado
- Arquivos expostos (license.txt, readme.html)
- Headers de segurança ausentes
- Software desatualizado

---

## Exemplo Prático - Descobertas

| Descoberta | Detalhes | Implicação |
|------------|----------|------------|
| **Servidor** | Apache/2.4.41 (Ubuntu) | Versão desatualizada (atual: 2.4.59) |
| **CMS** | WordPress | Alvo para exploits comuns de WP |
| **WAF** | Wordfence | Pode bloquear ataques |
| **Arquivos expostos** | license.txt, wp-login.php | Divulgação de informações |
| **Headers ausentes** | Strict-Transport-Security | Falha de configuração |