# Well-Known URIs

O padrão `.well-known`, definido na **RFC 8615**, estabelece um diretório padronizado na raiz de um site. Esse local, normalmente acessível por `/.well-known/`, centraliza metadados críticos, como arquivos de configuração e informações sobre serviços, protocolos e mecanismos de segurança.

Ao definir um ponto consistente para esses dados, o `.well-known` facilita descoberta e acesso por navegadores, aplicações e ferramentas de segurança. Assim, clientes podem localizar arquivos específicos montando a URL apropriada. Exemplo: para obter a política de segurança de um site, o cliente pode consultar `https://example.com/.well-known/security.txt`.

A **IANA** mantém um registro de URIs `.well-known`, cada uma com finalidade específica definida por normas e especificações.

| Sufixo URI | Descrição | Status | Referência |
|---|---|---|---|
| `security.txt` | Contém contato para pesquisadores reportarem vulnerabilidades. | Permanente | RFC 9116 |
| `change-password` | URL padrão para direcionar usuários à troca de senha. | Provisório | https://w3c.github.io/webappsec-change-password-url/#the-change-password-well-known-uri |
| `openid-configuration` | Define parâmetros de configuração do OpenID Connect (camada de identidade sobre OAuth 2.0). | Permanente | http://openid.net/specs/openid-connect-discovery-1_0.html |
| `assetlinks.json` | Verifica propriedade de ativos digitais (ex.: apps) associados ao domínio. | Permanente | https://github.com/google/digitalassetlinks/blob/master/well-known/specification.md |
| `mta-sts.txt` | Define política de SMTP MTA Strict Transport Security (MTA-STS). | Permanente | RFC 8461 |

Esses exemplos representam apenas uma parte do registro da IANA. Cada entrada traz requisitos e orientações próprias para implementação padronizada do mecanismo `.well-known`.

## Reconhecimento Web e `.well-known`

Em reconhecimento web, URIs `.well-known` são valiosas para descobrir endpoints e detalhes de configuração que podem ser avaliados durante um pentest. Um exemplo muito útil é `openid-configuration`.

Essa URI faz parte do protocolo **OpenID Connect Discovery**. Quando uma aplicação cliente deseja usar OpenID Connect para autenticação, ela pode obter a configuração do provedor acessando:

`https://example.com/.well-known/openid-configuration`

Esse endpoint retorna um JSON com metadados sobre endpoints, métodos de autenticação suportados, emissão de tokens e outros detalhes:

```json
{
  "issuer": "https://example.com",
  "authorization_endpoint": "https://example.com/oauth2/authorize",
  "token_endpoint": "https://example.com/oauth2/token",
  "userinfo_endpoint": "https://example.com/oauth2/userinfo",
  "jwks_uri": "https://example.com/oauth2/jwks",
  "response_types_supported": ["code", "token", "id_token"],
  "subject_types_supported": ["public"],
  "id_token_signing_alg_values_supported": ["RS256"],
  "scopes_supported": ["openid", "profile", "email"]
}
```

As informações desse endpoint permitem:

- **Descoberta de endpoints:** autorização, token e userinfo.
- **Localização de chaves criptográficas:** via `jwks_uri`.
- **Mapeamento de escopos e tipos de resposta suportados:** para entender capacidades e limitações.
- **Análise de algoritmos de assinatura:** para avaliar postura de segurança.

Explorar o registro da IANA e testar URIs `.well-known` é uma abordagem eficaz para descobrir novas oportunidades de reconhecimento. Como no caso de `openid-configuration`, essas URIs fornecem acesso estruturado a metadados críticos e ajudam profissionais de segurança a mapear o panorama de segurança de um alvo com mais profundidade.
