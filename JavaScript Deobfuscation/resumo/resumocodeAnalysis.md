# Análise do código desofuscado

## Objetivo

Depois da desofuscação, o próximo passo é interpretar o comportamento do código. Torná-lo legível não encerra a análise: é necessário identificar entradas, operações, comunicações externas e possíveis funcionalidades ocultas.

O código estudado é:

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

## Leitura linha por linha

### Modo estrito

~~~javascript
'use strict';
~~~

O modo estrito faz o JavaScript aplicar regras mais rigorosas, evitando alguns comportamentos silenciosos e ajudando a revelar determinados erros. Ele não indica ofuscação nem comportamento malicioso.

### Criação do objeto de requisição

~~~javascript
var xhr = new XMLHttpRequest;
~~~

**XMLHttpRequest** é uma API do navegador para realizar requisições HTTP. Embora o nome contenha XML, ela também pode trabalhar com texto, JSON, HTML e outros formatos.

A forma sem parênteses é válida quando o construtor não recebe argumentos:

~~~javascript
new XMLHttpRequest
~~~

Ela equivale, nesse caso, a:

~~~javascript
new XMLHttpRequest()
~~~

### URL relativa

~~~javascript
var url = "/serial.php";
~~~

A barra inicial indica um caminho relativo à origem:

~~~text
https://example.com/pasta/pagina
          + /serial.php
          ↓
https://example.com/serial.php
~~~

O navegador reutiliza esquema, host e porta da página atual. Portanto, a requisição está destinada à mesma origem, salvo influência de mecanismos como redirecionamentos ou uma configuração diferente de URL base.

### Preparação da requisição

~~~javascript
xhr.open("POST", url, true);
~~~

Os argumentos são:

- **"POST"** → método HTTP;
- **url** → destino definido como **/serial.php**;
- **true** → requisição assíncrona.

O método **open()** configura a requisição, mas ainda não a envia.

### Envio

~~~javascript
xhr.send(null);
~~~

**send()** transmite a requisição. O argumento **null** indica que nenhum corpo é enviado.

O trecho também não registra manipuladores como **onload**, **readystatechange** ou **onerror**. Assim, a parte visível envia o POST, mas não processa explicitamente a resposta.

## Comportamento reconstruído

~~~text
generateSerial()
      ↓
cria XMLHttpRequest
      ↓
configura POST assíncrono
      ↓
destino /serial.php
      ↓
envia requisição sem corpo
~~~

Essa é a funcionalidade essencial escondida pelo código ofuscado.

## Como reproduzir no laboratório

Exemplo adicional equivalente com cURL:

~~~bash
curl -i -X POST http://SERVER_IP:PORT/serial.php
~~~

Argumentos:

- **-i** → inclui headers da resposta;
- **-X POST** → seleciona explicitamente o método POST;
- a ausência de **-d** mantém a requisição sem dados de formulário.

Também é possível usar a aba **Network** das ferramentas de desenvolvedor para observar status HTTP, headers, corpo da resposta, redirecionamentos e tempo de execução.

## Hipótese de funcionalidade não exposta

O nome **generateSerial** e o endpoint **/serial.php** sugerem uma função de geração de número de série. Como não existe um botão correspondente no HTML analisado, algumas possibilidades são:

- funcionalidade planejada e ainda não conectada à interface;
- recurso antigo removido apenas do front-end;
- endpoint interno chamado por outro fluxo;
- código não utilizado;
- funcionalidade condicionada a estado, perfil ou configuração.

O nome da função é um indício, não uma prova. A resposta real do servidor deve ser examinada.

## Por que funcionalidades ocultas merecem atenção

Remover um botão da interface não desabilita o endpoint no servidor. Se a rota continuar acessível, poderá apresentar:

- validação incompleta;
- ausência de autorização;
- mensagens de erro detalhadas;
- parâmetros não documentados;
- comportamento diferente conforme método ou sessão.

Todo teste deve permanecer no escopo do laboratório ou de uma autorização explícita.

## Checklist de análise

1. Identifique funções e quando são chamadas.
2. Liste URLs e métodos HTTP.
3. Determine se os caminhos são relativos ou absolutos.
4. Observe parâmetros, headers e corpo enviados.
5. Verifique como a resposta é processada.
6. Reproduza a requisição com as mesmas condições.
7. Compare comportamento autenticado e não autenticado, quando autorizado.
8. Registre códigos de status, conteúdo e redirecionamentos.

## Pontos-chave para revisão

- Desofuscação revela a estrutura; análise explica a finalidade.
- **XMLHttpRequest** permite comunicação HTTP pelo navegador.
- **open()** configura e **send()** envia.
- O terceiro argumento **true** torna a requisição assíncrona.
- **/serial.php** aponta para a mesma origem.
- **send(null)** envia a requisição sem corpo.
- O código não mostra processamento explícito da resposta.
- Uma funcionalidade ausente da interface ainda pode existir no back-end.
