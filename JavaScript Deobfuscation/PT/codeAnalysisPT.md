# Análise de código

Agora que desofuscamos o código, podemos começar a analisá-lo:

~~~javascript
'use strict';
function generateSerial() {
  ...SNIP...
  var xhr = new XMLHttpRequest;
  var url = "/serial.php";
  xhr.open("POST", url, true);
  xhr.send(null);
};
~~~

Vemos que o arquivo **secret.js** contém apenas uma função, **generateSerial**.

## Requisições HTTP

Vamos examinar cada linha da função **generateSerial**.

### Variáveis do código

A função começa definindo uma variável **xhr**, que cria um objeto **XMLHttpRequest**. Como talvez não saibamos exatamente o que **XMLHttpRequest** faz em JavaScript, podemos pesquisar por **XMLHttpRequest** no Google para descobrir sua finalidade.

Depois de lermos sobre ele, vemos que é uma função JavaScript que manipula requisições web.

A segunda variável definida é **url**, que contém a URL **/serial.php**. Como nenhum domínio foi especificado, esse caminho deverá estar no mesmo domínio.

### Funções do código

Em seguida, vemos que **xhr.open** é usado com **"POST"** e **url**. Podemos pesquisar novamente por essa função no Google e descobriremos que ela abre a requisição HTTP definida, **GET** ou **POST**, para a URL. A linha seguinte, **xhr.send**, envia a requisição.

Portanto, tudo o que **generateSerial** faz é simplesmente enviar uma requisição POST para **/serial.php**, sem incluir dados POST nem recuperar qualquer informação retornada.

Os desenvolvedores podem ter implementado essa função para quando precisarem gerar um número de série, como ao clicar em determinado botão **Generate Serial**, por exemplo. Entretanto, como não vimos nenhum elemento HTML semelhante que gere números de série, os desenvolvedores provavelmente ainda não utilizaram essa função e a mantiveram para uso futuro.

Com o uso de desofuscação e análise de código, conseguimos revelar essa função. Agora podemos tentar reproduzir sua funcionalidade para verificar se ela é tratada no lado do servidor quando enviamos uma requisição POST. Se a função estiver habilitada e for processada no servidor, poderemos revelar uma funcionalidade ainda não lançada, que geralmente tende a conter bugs e vulnerabilidades.
