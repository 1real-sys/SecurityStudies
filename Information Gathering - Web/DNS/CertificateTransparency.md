# Logs de Transparência de Certificados (CT)

Logs CT são registros públicos append-only que registram a emissão de certificados SSL/TLS. Quando uma CA emite um certificado, ela deve submetê-lo a múltiplos logs CT.

## Por que são importantes?

| Benefício | Descrição |
|-----------|-----------|
| **Detecção de Certificados Fraudulentos** | Identificar rapidamente certificados suspeitos ou emitidos incorretamente |
| **Responsabilização das CAs** | Se uma CA violar regras, fica publicamente visível nos logs |
| **Fortalecimento da Web PKI** | Supervisão pública e verificação de certificados |

## Logs CT no Reconhecimento Web

Vantagens sobre força bruta ou wordlists:
- Registro **definitivo** de certificados emitidos para um domínio e subdomínios
- Visão **histórica e abrangente** dos subdomínios
- Revela subdomínios de certificados **antigos ou expirados** (potencialmente vulneráveis)

## Ferramentas para Pesquisar Logs CT

| Ferramenta | Recursos | Prós | Contras |
|------------|----------|------|---------|
| **crt.sh** | Interface web, busca por domínio, detalhes de certificado | Gratuito, sem registro | Filtragem limitada |
| **Censys** | Filtragem avançada por domínio/IP/atributos, API | Dados extensivos | Requer registro |

## Consulta via API (crt.sh)

Encontrar subdomínios 'dev' em facebook.com:

```bash
curl -s "https://crt.sh/?q=facebook.com&output=json" | jq -r '.[]
 | select(.name_value | contains("dev")) | .name_value' | sort -u
 
*.dev.facebook.com
*.newdev.facebook.com
*.secure.dev.facebook.com
dev.facebook.com
devvm1958.ftw3.facebook.com
facebook-amex-dev.facebook.com
newdev.facebook.com
secure.dev.facebook.com
```

| Parte do Comando | Função |
|------------------|--------|
| `curl -s "...&output=json"` | Busca JSON do crt.sh para o domínio |
| `jq -r '.[] \| select(.name_value \| contains("dev"))'` | Filtra entradas contendo "dev" |
| `sort -u` | Ordena e remove duplicatas |