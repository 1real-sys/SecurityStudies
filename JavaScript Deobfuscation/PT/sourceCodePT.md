# Código-fonte

Atualmente, a maioria dos sites utiliza JavaScript para executar suas funções. Enquanto o HTML é usado para determinar os principais campos e parâmetros do site e o CSS é usado para definir seu design, o JavaScript é usado para executar todas as funções necessárias ao funcionamento do site. Isso acontece em segundo plano, e vemos apenas o front-end visualmente agradável do site, com o qual interagimos.

Embora todo esse código-fonte esteja disponível no lado do cliente, ele é renderizado pelos navegadores, de modo que normalmente não prestamos atenção ao código-fonte HTML. Entretanto, se quisermos compreender as funcionalidades do lado do cliente de determinada página, geralmente começamos examinando o código-fonte dela. Esta seção mostrará como podemos revelar o código-fonte que contém tudo isso e compreender seu uso geral.

## HTML

Começaremos iniciando o exercício abaixo, abrindo o Firefox em nossa PwnBox e visitando a URL mostrada na questão:

```text
http://SERVER_IP:PORT
```

**Secret Serial Generator:** esta página gera números de série secretos.

Como podemos ver, o site exibe `Secret Serial Generator`, sem apresentar campos de entrada ou qualquer funcionalidade evidente. Portanto, nosso próximo passo é examinar seu código-fonte. Podemos fazer isso pressionando `[CTRL + U]`, o que deverá abrir a visualização do código-fonte do site:

```text
view-source:http://SERVER_IP:PORT
```

Trecho de código HTML de uma página intitulada `Secret Serial Generator`, com CSS para largura e altura de página inteira.

Como podemos ver, conseguimos visualizar o código-fonte HTML do site.

O código-fonte HTML pode conter várias informações, como comentários, que ajudam a compreender melhor o código. Desenvolvedores podem deixar informações sensíveis, das quais se pode tirar proveito posteriormente. Vale a pena ler os comentários HTML.

## CSS

O código CSS pode ser definido internamente no mesmo arquivo HTML, entre elementos `<style>`, ou externamente em um arquivo `.css` separado, referenciado pelo código HTML.

Neste caso, vemos que o CSS é definido internamente, conforme o trecho abaixo:

```HTML
    <style>
        *,
        html {
            margin: 0;
            padding: 0;
            border: 0;
        }
        ...SNIP...
        h1 {
            font-size: 144px;
        }
        p {
            font-size: 64px;
        }
    </style>
```

Se o estilo CSS de uma página for definido externamente, o arquivo `.css` externo será referenciado por meio da tag `<link>` dentro do `head` do HTML, da seguinte forma:

```HTML
<head>
    <link rel="stylesheet" href="style.css">
</head>
```

## JavaScript

O mesmo conceito se aplica ao JavaScript. Ele pode ser escrito internamente entre elementos `<script>` ou em um arquivo `.js` separado, referenciado pelo código HTML.

Podemos ver em nosso código-fonte HTML que o arquivo `.js` é referenciado externamente:

```HTML
<script src="secret.js"></script>
```

Podemos examinar o script clicando em `secret.js`, o que deverá nos levar diretamente a ele. Quando o visitamos, vemos que o código é muito complicado e não pode ser compreendido facilmente:

```javascript
eval(function (p, a, c, k, e, d) { e = function (c) { '...SNIP... |true|function'.split('|'), 0, {}))
```

O motivo disso é a ofuscação de código. O que ela é? Como é feita? Onde é utilizada?
