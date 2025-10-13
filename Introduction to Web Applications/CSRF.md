# CSRF - Cross-Site Request Forgery

CSRF é uma vulnerabilidade que permite a atacantes executar ações não autorizadas em aplicações web onde a vítima está autenticada. O ataque explora a confiança que uma aplicação web tem no navegador do usuário, forçando requisições maliciosas usando a sessão ativa da vítima.

## Como Funciona o CSRF

### Mecanismo do Ataque
1. **Vítima autenticada**: Usuário logado em aplicação legítima
2. **Payload malicioso**: Atacante injeta código que executa ações
3. **Execução automática**: Código usa sessão ativa para realizar ações
4. **Ações não autorizadas**: Mudança de senha, transferências, etc.

### Exemplo Prático
```html
<!-- Payload CSRF para mudança de senha -->
<script src="//www.example.com/exploit.js"></script>
```

O arquivo `exploit.js` conteria:
```javascript
// Código que replica a API de mudança de senha
fetch('/api/change-password', {
    method: 'POST',
    credentials: 'include', // Inclui cookies de sessão
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
        newPassword: 'senhaDoAtacante123'
    })
});
```

## Tipos de Ataques CSRF

### **1. CSRF via XSS**
- Utiliza vulnerabilidades XSS para injetar payloads
- JavaScript malicioso executa em contexto da aplicação
- Acesso total às funcionalidades da sessão

### **2. CSRF via Parâmetros HTTP**
```html
<!-- GET request malicioso -->
<img src="https://bank.com/transfer?to=attacker&amount=1000">

<!-- POST via formulário oculto -->
<form action="https://bank.com/transfer" method="POST" id="csrf">
    <input type="hidden" name="to" value="attacker">
    <input type="hidden" name="amount" value="1000">
</form>
<script>document.getElementById('csrf').submit();</script>
```

### **3. CSRF contra Administradores**
- Alvos de alto valor com privilégios elevados
- Acesso a funções sensíveis do sistema
- Potencial comprometimento do backend

## Impactos do CSRF

### **Usuários Comuns**
- Mudança de credenciais
- Alteração de dados pessoais
- Transações financeiras não autorizadas

### **Administradores**
- Criação de contas privilegiadas
- Modificação de configurações críticas
- Comprometimento total da aplicação

## Prevenção e Defesas

### **1. Tokens Anti-CSRF**
```html
<!-- Token único por sessão/requisição -->
<input type="hidden" name="csrf_token" value="abc123xyz789">
```

```javascript
// Validação no backend
if (token !== session.csrf_token) {
    return res.status(403).send('CSRF token inválido');
}
```

### **2. SameSite Cookies**
```http
Set-Cookie: sessionId=abc123; SameSite=Strict
Set-Cookie: sessionId=abc123; SameSite=Lax
```

### **3. Validação de Referer/Origin**
```javascript
// Verificar origem da requisição
const allowedOrigins = ['https://myapp.com'];
if (!allowedOrigins.includes(req.headers.origin)) {
    return res.status(403).send('Origem não autorizada');
}
```

### **4. Sanitização e Validação**

| Tipo | Descrição | Exemplo |
|------|-----------|---------|
| **Sanitização** | Remove caracteres especiais | `<script>` → `&lt;script&gt;` |
| **Validação** | Verifica formato esperado | Email: `/^[^\s@]+@[^\s@]+\.[^\s@]+$/` |

### **5. Confirmação de Ações Críticas**
```html
<!-- Requerer senha atual para mudanças -->
<input type="password" name="currentPassword" required>
```

### **6. Web Application Firewall (WAF)**
- Detecção automática de padrões maliciosos
- Bloqueio de requisições suspeitas
- **Atenção**: Pode ser bypassado, não é solução única

## Defesas Modernas

### **Proteções de Navegador**
- Bloqueio automático de JavaScript suspeito
- Políticas de Same-Origin mais rigorosas
- Content Security Policy (CSP)

### **Frameworks e Bibliotecas**
```javascript
// Express.js com csurf
const csrf = require('csurf');
app.use(csrf({ cookie: true }));
```

## Limitações das Defesas

### **Cenários de Bypass**
- Subdomain takeover
- XSS em domínios confiáveis
- Configurações incorretas de SameSite
- Vulnerabilidades em bibliotecas

### **Considerações Importantes**
- Defesas devem ser **camadas múltiplas**
- **Não depender apenas** de uma proteção
- **Aplicação segura por design**, não apenas proteções reativas

## Melhores Práticas

1. **Implementar tokens CSRF** em todas as ações state-changing
2. **Usar SameSite cookies** apropriadamente
3. **Validar Origin/Referer** headers
4. **Requerer reautenticação** para ações críticas
5. **Implementar rate limiting** em endpoints sensíveis
6. **Monitorar** tentativas de CSRF
7. **Educar usuários** sobre phishing e sites maliciosos

## Conclusão

CSRF permanece uma ameaça significativa mesmo com defesas modernas. A prevenção efetiva requer implementação de múltiplas camadas de segurança e design seguro desde o desenvolvimento. Desenvolvedores devem tratar as defesas como proteções adicionais, não primárias, garantindo que suas aplicações sejam inerentemente seguras contra ataques CSRF.

Source 
https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html