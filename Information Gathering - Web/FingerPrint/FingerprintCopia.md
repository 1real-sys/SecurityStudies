# Fingerprinting

Fingerprinting foca em extrair detalhes técnicos sobre as tecnologias que alimentam um site ou aplicação web. Similar à forma como uma impressão digital identifica unicamente uma pessoa, as assinaturas digitais de servidores web, sistemas operacionais e componentes de software podem revelar informações críticas sobre a infraestrutura de um alvo e potenciais fraquezas de segurança. Este conhecimento permite que atacantes personalizem ataques e explorem vulnerabilidades específicas das tecnologias identificadas.

Fingerprinting serve como pedra angular do reconhecimento web por várias razões:

- **Ataques Direcionados:** Ao conhecer as tecnologias específicas em uso, atacantes podem focar seus esforços em exploits e vulnerabilidades conhecidas por afetar esses sistemas. Isso aumenta significativamente as chances de um comprometimento bem-sucedido.
- **Identificação de Configurações Incorretas:** Fingerprinting pode expor software mal configurado ou desatualizado, configurações padrão ou outras fraquezas que podem não ser aparentes através de outros métodos de reconhecimento.
- **Priorização de Alvos:** Quando confrontado com múltiplos alvos potenciais, fingerprinting ajuda a priorizar esforços identificando sistemas mais propensos a serem vulneráveis ou conter informações valiosas.
- **Construção de Perfil Abrangente:** Combinar dados de fingerprint com outras descobertas de reconhecimento cria uma visão holística da infraestrutura do alvo, auxiliando na compreensão de sua postura geral de segurança e vetores de ataque potenciais.

## Técnicas de Fingerprinting

Existem várias técnicas usadas para fingerprinting de servidores web e tecnologias:

- **Banner Grabbing:** Envolve analisar os banners apresentados por servidores web e outros serviços. Esses banners frequentemente revelam o software do servidor, números de versão e outros detalhes.
- **Análise de Headers HTTP:** Headers HTTP transmitidos com cada requisição e resposta de página web contêm uma riqueza de informações. O header `Server` tipicamente divulga o software do servidor web, enquanto o header `X-Powered-By` pode revelar tecnologias adicionais como linguagens de script ou frameworks.
- **Sondagem por Respostas Específicas:** Enviar requisições especialmente elaboradas ao alvo pode provocar respostas únicas que revelam tecnologias ou versões específicas. Por exemplo, certas mensagens de erro ou comportamentos são característicos de servidores web ou componentes de software particulares.
- **Análise de Conteúdo da Página:** O conteúdo de uma página web, incluindo sua estrutura, scripts e outros elementos, frequentemente pode fornecer pistas sobre as tecnologias subjacentes. Pode haver um cabeçalho de copyright que indica software específico sendo usado, por exemplo.

## Ferramentas de Fingerprinting

Uma variedade de ferramentas existe para automatizar o processo de fingerprinting, combinando várias técnicas para identificar servidores web, sistemas operacionais, sistemas de gerenciamento de conteúdo e outras tecnologias:

| Ferramenta | Descrição | Recursos |
|------------|-----------|----------|
| Wappalyzer | Extensão de navegador e serviço online para perfil de tecnologia de sites. | Identifica uma ampla gama de tecnologias web, incluindo CMSs, frameworks, ferramentas de analytics e mais. |
| BuiltWith | Profiler de tecnologia web que fornece relatórios detalhados sobre a stack de tecnologia de um site. | Oferece planos gratuitos e pagos com níveis variados de detalhe. |
| WhatWeb | Ferramenta de linha de comando para fingerprinting de sites. | Usa um vasto banco de dados de assinaturas para identificar várias tecnologias web. |
| Nmap | Scanner de rede versátil que pode ser usado para várias tarefas de reconhecimento, incluindo fingerprinting de serviços e SO. | Pode ser usado com scripts (NSE) para realizar fingerprinting mais especializado. |
| Netcraft | Oferece uma gama de serviços de segurança web, incluindo fingerprinting de sites e relatórios de segurança. | Fornece relatórios detalhados sobre tecnologia, provedor de hospedagem e postura de segurança de um site. |
| wafw00f | Ferramenta de linha de comando especificamente projetada para identificar Web Application Firewalls (WAFs). | Ajuda a determinar se um WAF está presente e, se sim, seu tipo e configuração. |

## Fingerprinting na Prática (inlanefreight.com)

Vamos aplicar nosso conhecimento de fingerprinting para descobrir o DNA digital do nosso host de teste, inlanefreight.com. Usaremos técnicas manuais e automatizadas para coletar informações sobre seu servidor web, tecnologias e vulnerabilidades potenciais.

### Banner Grabbing

Nosso primeiro passo é coletar informações diretamente do próprio servidor web. Podemos fazer isso usando o comando curl com a flag `-I` (ou `--head`) para buscar apenas os headers HTTP, não o conteúdo inteiro da página.

```bash
curl -I inlanefreight.com

HTTP/1.1 301 Moved Permanently
Date: Fri, 31 May 2024 12:07:44 GMT
Server: Apache/2.4.41 (Ubuntu)
Location: https://inlanefreight.com/
Content-Type: text/html; charset=iso-8859-1
```

Neste caso, vemos que inlanefreight.com está rodando em **Apache/2.4.41**, especificamente a versão Ubuntu. Esta informação é nossa primeira pista, indicando a stack de tecnologia subjacente. Também está tentando redirecionar para https://inlanefreight.com/, então pegue esses banners também:

```bash
curl -I https://inlanefreight.com

HTTP/1.1 301 Moved Permanently
Date: Fri, 31 May 2024 12:12:12 GMT
Server: Apache/2.4.41 (Ubuntu)
X-Redirect-By: WordPress
Location: https://www.inlanefreight.com/
Content-Type: text/html; charset=UTF-8
```

Agora temos um header realmente interessante - o servidor está tentando nos redirecionar novamente, mas desta vez vemos que é o **WordPress** que está fazendo o redirecionamento para https://www.inlanefreight.com/

```bash
curl -I https://www.inlanefreight.com

HTTP/1.1 200 OK
Date: Fri, 31 May 2024 12:12:26 GMT
Server: Apache/2.4.41 (Ubuntu)
Link: <https://www.inlanefreight.com/index.php/wp-json/>; rel="https://api.w.org/"
Link: <https://www.inlanefreight.com/index.php/wp-json/wp/v2/pages/7>; rel="alternate"; type="application/json"
Link: <https://www.inlanefreight.com/>; rel=shortlink
Content-Type: text/html; charset=UTF-8
```

Mais alguns headers interessantes, incluindo um caminho interessante que contém `wp-json`. O prefixo `wp-` é comum ao WordPress.

### Wafw00f - Detecção de WAF

Web Application Firewalls (WAFs) são soluções de segurança projetadas para proteger aplicações web de vários ataques. Antes de prosseguir com mais fingerprinting, é crucial determinar se o alvo emprega um WAF, pois ele pode interferir com nossas sondagens ou potencialmente bloquear nossas requisições.

**Instalação:**
```bash
pip3 install git+https://github.com/EnableSecurity/wafw00f
```

**Uso:**
```bash
wafw00f inlanefreight.com

                ______
               /      \
              (  W00f! )
               \  ____/
               ,,    __            404 Hack Not Found
           |`-.__   / /                      __     __
           /"  _/  /_/                       \ \   / /
          *===*    /                          \ \_/ /  405 Not Allowed
         /     )__//                           \   /
    /|  /     /---`                        403 Forbidden
    \\/`   \ |                                 / _ \
    `\    /_\\_              502 Bad Gateway  / / \ \  500 Internal Error
      `_____``-`                             /_/   \_\

                        ~ WAFW00F : v2.2.0 ~
        The Web Application Firewall Fingerprinting Toolkit
    
[*] Checking https://inlanefreight.com
[+] The site https://inlanefreight.com is behind Wordfence (Defiant) WAF.
[~] Number of requests: 2
```

O scan do wafw00f revela que o site está protegido pelo **Wordfence Web Application Firewall (WAF)**, desenvolvido pela Defiant.

Isso significa que o site tem uma camada adicional de segurança que pode bloquear ou filtrar nossas tentativas de reconhecimento. Em um cenário real, seria crucial manter isso em mente ao prosseguir com investigação adicional, pois você pode precisar adaptar técnicas para contornar ou evadir os mecanismos de detecção do WAF.

### Nikto - Scanner de Servidor Web

Nikto é um poderoso scanner de servidor web open-source. Além de sua função primária como ferramenta de avaliação de vulnerabilidades, as capacidades de fingerprinting do Nikto fornecem insights sobre a stack de tecnologia de um site.

**Instalação:**
```bash
sudo apt update && sudo apt install -y perl
git clone https://github.com/sullo/nikto
cd nikto/program
chmod +x ./nikto.pl
```

**Uso (apenas módulos de fingerprinting):**
```bash
nikto -h inlanefreight.com -Tuning b
```

- A flag `-h` especifica o host alvo
- A flag `-Tuning b` diz ao Nikto para rodar apenas os módulos de Identificação de Software

**Saída de Exemplo:**
```
- Nikto v2.5.0
---------------------------------------------------------------------------
+ Multiple IPs found: 134.209.24.248, 2a03:b0c0:1:e0::32c:b001
+ Target IP:          134.209.24.248
+ Target Hostname:    www.inlanefreight.com
+ Target Port:        443
---------------------------------------------------------------------------
+ SSL Info:        Subject:  /CN=inlanefreight.com
                   Altnames: inlanefreight.com, www.inlanefreight.com
                   Ciphers:  TLS_AES_256_GCM_SHA384
                   Issuer:   /C=US/O=Let's Encrypt/CN=R3
+ Start Time:         2024-05-31 13:35:54 (GMT0)
---------------------------------------------------------------------------
+ Server: Apache/2.4.41 (Ubuntu)
+ /: The site uses TLS and the Strict-Transport-Security HTTP header is not defined.
+ /: The X-Content-Type-Options header is not set.
+ /index.php?: Uncommon header 'x-redirect-by' found, with contents: WordPress.
+ Apache/2.4.41 appears to be outdated (current is at least 2.4.59).
+ /license.txt: License file found may identify site software.
+ /: A Wordpress installation was found.
+ /wp-login.php: Wordpress login found.
+ 1316 requests: 0 error(s) and 12 item(s) reported on remote host
+ End Time:           2024-05-31 13:47:27 (GMT0) (693 seconds)
---------------------------------------------------------------------------
```

### Resumo das Descobertas

O scan de reconhecimento em inlanefreight.com revela várias descobertas chave:

| Descoberta | Detalhes |
|------------|----------|
| **IPs** | O site resolve para IPv4 (134.209.24.248) e IPv6 (2a03:b0c0:1:e0::32c:b001) |
| **Tecnologia do Servidor** | Apache/2.4.41 (Ubuntu) |
| **Presença de WordPress** | Instalação WordPress identificada, incluindo página de login (/wp-login.php) |
| **WAF** | Protegido por Wordfence (Defiant) |
| **Divulgação de Informações** | Presença de arquivo license.txt que pode revelar detalhes adicionais |
| **Headers** | Vários headers não-padrão ou inseguros encontrados, incluindo header Strict-Transport-Security ausente |
