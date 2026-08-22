# Requisições HTTP com cURL

## Objetivo

O código analisado anteriormente usa **XMLHttpRequest** para enviar um POST vazio a **/serial.php**. Esta seção apresenta cURL como forma de reproduzir manualmente requisições HTTP e observar diretamente a resposta do servidor.

## Requisição GET básica

~~~shellsession
JLMreal@htb[/htb]$ curl http://SERVER_IP:PORT/
~~~

Sem outra opção, cURL utiliza GET e escreve o corpo da resposta no terminal. No laboratório, a resposta contém o HTML da página **Secret Serial Generator**:

~~~html
</html>
<!DOCTYPE html>

<head>
    <title>Secret Serial Generator</title>
    <style>
        *,
        html {
            margin: 0;
            padding: 0;
            border: 0;
...SNIP...
        <h1>Secret Serial Generator</h1>
        <p>This page generates secret serials!</p>
    </div>
</body>

</html>
~~~

Esse conteúdo corresponde ao código-fonte inspecionado no início do módulo.

## POST vazio

Comando original:

~~~shellsession
JLMreal@htb[/htb]$ curl -s http://SERVER_IP:PORT/ -X POST
~~~

Argumentos:

- **curl** → executa o cliente HTTP;
- **-s** → ativa o modo silencioso e remove barra de progresso e mensagens comuns;
- **http://SERVER_IP:PORT/** → define o destino;
- **-X POST** → seleciona explicitamente o método POST.

Para reproduzir exatamente a função analisada anteriormente, o endpoint deverá ser **/serial.php**:

~~~bash
curl -s http://SERVER_IP:PORT/serial.php -X POST
~~~

Esse é um exemplo complementar derivado do comportamento de **generateSerial()**.

## POST com dados

Comando original:

~~~shellsession
JLMreal@htb[/htb]$ curl -s http://SERVER_IP:PORT/ -X POST -d "param1=sample"
~~~

A opção **-d** envia os dados no corpo da requisição. Por padrão, cURL usa um formato equivalente a:

~~~http
Content-Type: application/x-www-form-urlencoded

param1=sample
~~~

Ao utilizar **-d**, cURL já seleciona POST automaticamente. Portanto, este comando adicional é equivalente para o caso básico:

~~~bash
curl -s http://SERVER_IP:PORT/ -d "param1=sample"
~~~

O uso explícito de **-X POST** continua sendo útil didaticamente para deixar o método evidente.

## Visualizando detalhes da resposta

O modo **-s** reduz ruído, mas também pode ocultar mensagens de erro do cURL. Durante análise, algumas opções úteis são:

~~~bash
curl -i http://SERVER_IP:PORT/
curl -v http://SERVER_IP:PORT/
curl -sS http://SERVER_IP:PORT/
~~~

- **-i** → inclui os headers HTTP da resposta;
- **-v** → mostra detalhes da conexão e da requisição;
- **-sS** → mantém o modo silencioso, mas ainda exibe erros.

Esses são exemplos adicionais para facilitar a observação em laboratório.

## Relação com XMLHttpRequest

O JavaScript:

~~~javascript
var xhr = new XMLHttpRequest;
var url = "/serial.php";
xhr.open("POST", url, true);
xhr.send(null);
~~~

Pode ser representado, em essência, por:

~~~bash
curl -s http://SERVER_IP:PORT/serial.php -X POST
~~~

A comparação não é perfeita em todos os detalhes: o navegador pode incluir automaticamente headers como **Origin**, **Referer** e cookies da sessão, enquanto cURL só enviará cookies se eles forem fornecidos ou previamente armazenados.

## Comparação rápida

| Ação | JavaScript | cURL |
| --- | --- | --- |
| Definir método e URL | xhr.open("POST", url, true) | -X POST URL |
| Enviar sem corpo | xhr.send(null) | POST sem -d |
| Enviar dados | xhr.send(dados) | -d "param1=sample" |
| Inspecionar resposta | handlers e propriedades de XHR | saída, -i ou -v |

## Inconsistência no nome do arquivo

O último parágrafo do original menciona **server.js**, mas o restante do módulo analisa **secret.js**. Pelo contexto, provavelmente se trata de um erro de nomenclatura e a intenção era dizer:

~~~text
replicar o que secret.js está fazendo
~~~

O nome original foi preservado na tradução; esta observação apresenta separadamente a provável correção.

## Pontos-chave para revisão

- cURL permite reproduzir requisições sem depender da interface web.
- Uma URL sem opções adicionais normalmente gera GET.
- **-X POST** define explicitamente o método POST.
- **-d** envia dados e normalmente já implica POST.
- **-s** reduz a saída; **-sS** mantém a exibição de erros.
- O endpoint observado no JavaScript é **/serial.php**.
- Requisições feitas pelo navegador e pelo cURL podem diferir em headers, cookies e contexto de sessão.
