# HTTPS - HyperText Transfer Protocol Secure

HTTPS é uma extensão segura do protocolo HTTP que utiliza criptografia TLS/SSL para proteger a comunicação entre cliente e servidor. Foi desenvolvido para combater ataques como Man-in-the-Middle (MitM), interceptação de dados sensíveis e falsificação de identidade.

## Como Funciona o HTTPS

### 1. Handshake TLS/SSL
O processo de estabelecimento de conexão segura:

1. **Client Hello**: Cliente inicia conexão enviando protocolos suportados
2. **Server Hello**: Servidor responde com protocolo escolhido e certificado
3. **Verificação do Certificado**: Cliente valida certificado com CA
4. **Troca de Chaves**: Estabelecimento de chaves simétricas para criptografia
5. **Comunicação Segura**: Dados criptografados com chaves estabelecidas

### 2. Criptografia Híbrida
- **Assimétrica (RSA/ECDSA)**: Para troca inicial de chaves
- **Simétrica (AES)**: Para criptografia dos dados (mais eficiente)
- **Hash (SHA-256)**: Para integridade e autenticação

## Certificados SSL/TLS

### Tipos de Certificados
- **Domain Validated (DV)**: Validação básica do domínio
- **Organization Validated (OV)**: Validação da organização
- **Extended Validation (EV)**: Validação rigorosa (barra verde)
- **Wildcard**: Cobre subdomínios (*.exemplo.com)
- **Multi-Domain (SAN)**: Múltiplos domínios em um certificado

### Autoridades Certificadoras (CA)
- **Root CAs**: Let's Encrypt, DigiCert, GlobalSign
- **Intermediate CAs**: Certificados intermediários na cadeia
- **Self-Signed**: Certificados auto-assinados (não confiáveis por padrão)

### Estrutura do Certificado
```
Subject: CN=exemplo.com, O=Empresa, C=BR
Issuer: CN=Let's Encrypt Authority X3
Valid From: 2024-01-01
Valid To: 2024-04-01
Public Key: RSA 2048 bits
Signature Algorithm: SHA256withRSA
```

## Configurações de Segurança

### Protocolos TLS
- **TLS 1.3**: Mais recente e seguro (2018)
- **TLS 1.2**: Amplamente suportado (2008)
- **TLS 1.1/1.0**: Obsoletos e inseguros
- **SSL 3.0/2.0**: Completamente inseguros

### Cipher Suites Seguros
```
TLS_AES_256_GCM_SHA384                 (TLS 1.3)
TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384  (TLS 1.2)
TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256  (TLS 1.2)
```

### Configurações Recomendadas
- **Perfect Forward Secrecy (PFS)**: ECDHE/DHE
- **OCSP Stapling**: Verificação rápida de revogação
- **HSTS**: Força uso de HTTPS
- **Certificate Pinning**: Fixa certificados específicos

## Cabeçalhos de Segurança HTTPS

### HTTP Strict Transport Security (HSTS)
```http
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
```

### Certificate Transparency
```http
Expect-CT: max-age=86400, enforce, report-uri="https://example.com/ct-report"
```

### Public Key Pinning (Descontinuado)
```http
Public-Key-Pins: pin-sha256="base64+hash"; max-age=5184000
```

## Ferramentas para Análise HTTPS

### OpenSSL - Teste de Conexão
```bash
# Testar conexão TLS
openssl s_client -connect exemplo.com:443

# Verificar certificado
openssl x509 -in cert.pem -text -noout

# Testar protocolos específicos
openssl s_client -connect exemplo.com:443 -tls1_2

# Verificar cadeia de certificados
openssl s_client -connect exemplo.com:443 -showcerts
```

### SSLyze - Análise Abrangente
```bash
# Instalação
pip install sslyze

# Análise completa
sslyze exemplo.com

# Verificar protocolos suportados
sslyze --tlsv1 --tlsv1_1 --tlsv1_2 --tlsv1_3 exemplo.com
```

### Testssl.sh - Script de Teste
```bash
# Download e uso
wget https://github.com/drwetter/testssl.sh/archive/v3.0.8.tar.gz
./testssl.sh exemplo.com
```

### Nmap Scripts SSL
```bash
# Scripts SSL do Nmap
nmap --script ssl-enum-ciphers -p 443 exemplo.com
nmap --script ssl-cert -p 443 exemplo.com
nmap --script ssl-heartbleed -p 443 exemplo.com
```

## Vulnerabilidades Comuns

### 1. Certificados Inválidos
- **Expirados**: Certificado fora da validade
- **Self-Signed**: Não assinado por CA confiável
- **Nome Incorreto**: CN não confere com domínio
- **Cadeia Quebrada**: Certificados intermediários ausentes

### 2. Configurações Fracas
- **Protocolos Antigos**: SSLv3, TLS 1.0/1.1
- **Cipher Suites Fracos**: RC4, DES, exportáveis
- **Chaves Pequenas**: RSA < 2048 bits
- **Ausência de PFS**: Sem ECDHE/DHE

### 3. Vulnerabilidades Específicas
- **Heartbleed**: CVE-2014-0160 (OpenSSL)
- **POODLE**: SSLv3 padding attack
- **BEAST**: TLS 1.0 cipher block chaining
- **CRIME/BREACH**: Compressão TLS/HTTP
- **Sweet32**: Ataques a cifras de 64 bits

### 4. Mixed Content
- **Active Mixed Content**: Scripts/CSS via HTTP
- **Passive Mixed Content**: Imagens/vídeos via HTTP
- **Impacto**: Degrada segurança da página HTTPS

## Bypass e Ataques

### SSL Stripping
```bash
# Ettercap + sslstrip
ettercap -T -M arp:remote /192.168.1.1// /192.168.1.100//
sslstrip -l 8080
```

### Certificate Pinning Bypass (Mobile)
```bash
# Frida script para bypass
frida -U -f com.app.target -l ssl-kill-switch.js
```

### SNI (Server Name Indication) Issues
```bash
# Teste sem SNI
openssl s_client -connect IP:443

# Teste com SNI específico
openssl s_client -connect IP:443 -servername exemplo.com
```

## Monitoramento e Logs

### Certificate Transparency Logs
- **Monitoramento**: crt.sh, censys.io
- **Detecção**: Certificados não autorizados
- **Alertas**: Emissão de certificados suspeitos

### Análise de Logs
```bash
# Grep para erros SSL em logs Apache
grep "SSL.*error" /var/log/apache2/error.log

# Análise de handshakes falhados
grep "TLS handshake failure" /var/log/nginx/error.log
```

## Implementação Segura

### Configuração Apache
```apache
# Protocolos seguros apenas
SSLProtocol -all +TLSv1.2 +TLSv1.3

# Cipher suites seguras
SSLCipherSuite ECDHE+AESGCM:ECDHE+CHACHA20:DHE+AESGCM:DHE+CHACHA20:!aNULL:!MD5:!DSS

# HSTS
Header always set Strict-Transport-Security "max-age=63072000; includeSubDomains; preload"
```

### Configuração Nginx
```nginx
# Protocolos TLS
ssl_protocols TLSv1.2 TLSv1.3;

# Ciphers seguros
ssl_ciphers ECDHE-RSA-AES256-GCM-SHA512:DHE-RSA-AES256-GCM-SHA512;

# Perfect Forward Secrecy
ssl_prefer_server_ciphers off;
ssl_ecdh_curve secp384r1;
```

## Compliance e Padrões

### PCI DSS Requirements
- **TLS 1.2+**: Obrigatório para dados de cartão
- **Strong Cryptography**: AES-256, RSA-2048+
- **Certificate Management**: Renovação automática

### OWASP Guidelines
- **A02:2021**: Falhas criptográficas
- **Transport Layer Protection**: Proteção em trânsito
- **Certificate Validation**: Validação adequada

## Tendências e Futuro

### TLS 1.3 Advantages
- **Handshake Reduzido**: 1-RTT vs 2-RTT
- **Forward Secrecy**: Obrigatório por padrão
- **Cipher Suites Simplificados**: Apenas algoritmos seguros

### Post-Quantum Cryptography
- **Preparação**: Algoritmos resistentes a computação quântica
- **NIST Standards**: Novos algoritmos padronizados
- **Migração**: Planejamento para transição futura

### Certificate Automation
- **ACME Protocol**: Automatização Let's Encrypt
- **Certificate Lifecycle**: Renovação e revogação automática
- **DevSecOps Integration**: Certificados como código