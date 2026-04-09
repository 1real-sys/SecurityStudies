# Well-Known URIs

O padrão `.well-known` (RFC 8615) define um diretório padronizado na raiz do site (`/.well-known/`) para expor metadados e configurações importantes de serviços, protocolos e segurança.

Essa padronização facilita a descoberta automática por navegadores, aplicações e ferramentas de segurança. Exemplo: `https://example.com/.well-known/security.txt`.

A IANA mantém o registro oficial dessas URIs.

| Sufixo URI | Descrição | Status | Referência |
|---|---|---|---|
| `security.txt` | Contato para reporte de vulnerabilidades. | Permanente | RFC 9116 |
| `change-password` | URL padrão para troca de senha. | Provisório | https://w3c.github.io/webappsec-change-password-url/#the-change-password-well-known-uri |
| `openid-configuration` | Configuração do OpenID Connect sobre OAuth 2.0. | Permanente | http://openid.net/specs/openid-connect-discovery-1_0.html |
| `assetlinks.json` | Verificação de propriedade de ativos digitais associados ao domínio. | Permanente | https://github.com/google/digitalassetlinks/blob/master/well-known/specification.md |
| `mta-sts.txt` | Política de MTA-STS para segurança de e-mail SMTP. | Permanente | RFC 8461 |

## Reconhecimento Web e `.well-known`

Essas URIs são úteis em reconhecimento web para identificar endpoints e detalhes de configuração relevantes para testes.

Um endpoint chave é:

`https://example.com/.well-known/openid-configuration`

Ele retorna um JSON com endpoints de autenticação, emissão de token, `userinfo`, `jwks_uri`, escopos suportados e algoritmos de assinatura.

Exemplo:

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