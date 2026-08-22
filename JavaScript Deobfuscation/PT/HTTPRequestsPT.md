# Requisições HTTP

Na seção anterior, descobrimos que a função principal de **secret.js** envia uma requisição POST vazia para **/serial.php**. Nesta seção, tentaremos fazer o mesmo usando cURL para enviar uma requisição POST a **/serial.php**. Para aprender mais sobre cURL e requisições web, você pode consultar o módulo **Web Requests**.

## cURL

cURL é uma poderosa ferramenta de linha de comando utilizada em distribuições Linux, macOS e até nas versões mais recentes do Windows PowerShell. Podemos requisitar qualquer site simplesmente fornecendo sua URL e receberemos seu conteúdo em formato de texto, da seguinte forma:

~~~shellsession
JLMreal@htb[/htb]$ curl http://SERVER_IP:PORT/

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

Esse é o mesmo HTML que examinamos quando verificamos o código-fonte na primeira seção.

## Requisição POST

Para enviar uma requisição POST, devemos adicionar a flag **-X POST** ao comando, e ele deverá enviar uma requisição POST:

~~~shellsession
JLMreal@htb[/htb]$ curl -s http://SERVER_IP:PORT/ -X POST
~~~

> **Dica:** adicionamos a flag **"-s"** para reduzir a quantidade de dados desnecessários exibidos na resposta.

Entretanto, requisições POST normalmente contêm dados POST. Para enviar dados, podemos usar a flag **"-d "param1=sample""** e incluir nossos dados para cada parâmetro, da seguinte forma:

~~~shellsession
JLMreal@htb[/htb]$ curl -s http://SERVER_IP:PORT/ -X POST -d "param1=sample"
~~~

Agora que sabemos como usar cURL para enviar requisições POST básicas, na próxima seção utilizaremos esse conhecimento para reproduzir o que **server.js** está fazendo e compreender melhor sua finalidade.
