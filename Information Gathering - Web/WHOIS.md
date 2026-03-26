# WHOIS

O **WHOIS** é um protocolo de consulta usado para obter dados de registro de domínios, blocos de IP e sistemas autônomos.
Na prática, ele ajuda a entender **quem administra** um ativo na internet e **quais dados técnicos** estão vinculados a ele.

## Exemplo rápido de saída

```bash
Domain Name: example.com
Registrar: Example Registrar, Inc.
Creation Date: 2015-05-10T12:00:00Z
Expiration Date: 2027-05-10T12:00:00Z
Name Server: ns1.exampledns.com
Name Server: ns2.exampledns.com
```

## Informações comuns em um registro WHOIS (com exemplos)

| Campo | O que mostra | Exemplo |
|---|---|---|
| `Domain Name` | Nome do domínio consultado | `example.com` |
| `Registrar` | Empresa onde o domínio foi registrado | `Namecheap, GoDaddy, Registro.br` |
| `Registrant Contact` | Dono legal (pessoa/empresa) | `Example Corp` |
| `Administrative Contact` | Responsável administrativo | `admin@example.com` |
| `Technical Contact` | Responsável técnico | `noc@example.com` |
| `Creation Date` | Data de criação do domínio | `2019-08-05` |
| `Expiration Date` | Data de expiração do domínio | `2027-08-05` |
| `Name Server` | Servidores DNS autoritativos | `ns1.exampledns.com` |
| `Updated Date` | Última atualização do registro | `2026-01-15` |

## Por que isso importa em segurança web

Durante o reconhecimento, WHOIS ajuda a:

- **Mapear responsáveis e contexto organizacional**.
- **Levantar pistas de infraestrutura** (DNS, provedor, padrões de registro).
- **Analisar histórico de mudanças** (propriedade, contatos e configuração).

## Resumo prático

WHOIS não confirma vulnerabilidades sozinho, mas é uma fonte inicial valiosa para orientar as próximas etapas da coleta de informações.
