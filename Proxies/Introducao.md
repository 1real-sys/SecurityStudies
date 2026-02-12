# Introdução aos Proxies Web

## O que são Proxies Web?

Os proxies web são ferramentas especializadas configuradas entre um navegador/aplicativo e um servidor back-end para capturar e visualizar requisições web, funcionando como ferramentas de ataque man-in-the-middle (MITM). Operam principalmente com portas web HTTP/80 e HTTPS/443.

## Função Principal

- Capturar e reproduzir requisições HTTP entre aplicações e servidores
- Visualizar requisições e respostas
- Interceptar e modificar requisições para fins de teste
- Ferramenta essencial para pentests web

## Usos de Proxies Web

- Análise de vulnerabilidades de aplicações web
- Fuzzing na Web
- Rastreamento da Web
- Mapeamento de aplicativos da Web
- Análise de requisições web
- Teste de configuração da Web
- Revisões de código

## Principais Ferramentas

### Burp Suite
- Proxy web mais comum para testes de penetração
- Interface de usuário excelente
- Navegador Chromium integrado
- **Versão gratuita:** recursos básicos suficientes para maioria dos testes
- **Versão paga (Pro/Enterprise):** Scanner ativo, Burp Intruder rápido, extensões

### OWASP ZAP
- Ferramenta gratuita e de código aberto
- Mantida pelo OWASP e comunidade
- Sem limitações de recursos pagos
- Comunidade crescente de colaboradores
- Principal alternativa de código aberto ao Burp

## Considerações

Ambas as ferramentas são similares de usar e oferecem opções para diferentes situações. A escolha entre elas depende das necessidades específicas do teste: ZAP para experiência gratuita completa, Burp Pro para recursos avançados em ambientes corporativos.
