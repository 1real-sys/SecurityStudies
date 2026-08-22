# Desofuscação

Agora que compreendemos como a ofuscação de código funciona, vamos começar nosso aprendizado sobre desofuscação. Assim como existem ferramentas para ofuscar código automaticamente, também existem ferramentas para formatar (*beautify*) e desofuscar código automaticamente.

## Beautify

Vemos que o código atual está todo escrito em uma única linha. Isso é conhecido como código JavaScript minificado. Para formatá-lo corretamente, precisamos aplicar *Beautify* ao código. O método mais básico para fazer isso é usar as ferramentas de desenvolvedor do navegador (Browser Dev Tools).

Por exemplo, se estivermos usando o Firefox, podemos abrir o depurador do navegador com **CTRL+SHIFT+Z** e clicar no script **secret.js**. Isso mostrará o script em sua formatação original, mas podemos clicar no botão **{ }**, na parte inferior, que aplicará **Pretty Print** ao script e o apresentará com a formatação JavaScript adequada.

Editor de código mostrando o arquivo JavaScript **secret.js** com código de substituição por expressão regular.

Além disso, podemos utilizar várias ferramentas online ou plugins de editores de código, como Prettier ou Beautifier. Vamos copiar o script **secret.js**:

~~~javascript
eval(function (p, a, c, k, e, d) { e = function (c) { return c.toString(36) }; if (!''.replace(/^/, String)) { while (c--) { d[c.toString(a)] = k[c] || c.toString(a) } k = [function (e) { return d[e] }]; e = function () { return '\\w+' }; c = 1 }; while (c--) { if (k[c]) { p = p.replace(new RegExp('\\b' + e(c) + '\\b', 'g'), k[c]) } } return p }('g 4(){0 5="6{7!}";0 1=8 a();0 2="/9.c";1.d("e",2,f);1.b(3)}', 17, 17, 'var|xhr|url|null|generateSerial|flag|HTB|flag|new|serial|XMLHttpRequest|send|php|open|POST|true|function'.split('|'), 0, {}))
~~~

Podemos ver que ambos os sites fazem um bom trabalho na formatação do código:

~~~text
https://prettier.io/playground/
~~~

Editor de código exibindo uma função JavaScript ofuscada que utiliza **eval**.

~~~text
https://beautifier.io/
~~~

Código JavaScript ofuscado que utiliza **eval** e substituição por expressão regular.

Entretanto, o código ainda não é muito fácil de ler. Isso acontece porque o código com o qual estamos lidando não foi apenas minificado, mas também ofuscado. Portanto, apenas formatar ou aplicar *beautify* ao código não será suficiente. Para isso, precisaremos de ferramentas que desofusquem o código.

## Desofuscar

Podemos encontrar muitas ferramentas online eficientes para desofuscar código JavaScript e transformá-lo em algo que possamos compreender. Uma boa ferramenta é o UnPacker. Vamos copiar o código ofuscado acima e executá-lo no UnPacker clicando no botão **UnPack**.

> **Dica:** certifique-se de não deixar linhas vazias antes do script, pois isso pode afetar o processo de desofuscação e produzir resultados imprecisos.

~~~text
https://matthewfl.com/unPacker.html
~~~

Código JavaScript ofuscado com funções para gerar e enviar números de série.

Podemos ver que essa ferramenta realiza um trabalho muito melhor na desofuscação do código JavaScript e nos fornece uma saída que conseguimos compreender:

~~~javascript
function generateSerial() {
  ...SNIP...
  var xhr = new XMLHttpRequest;
  var url = "/serial.php";
  xhr.open("POST", url, true);
  xhr.send(null);
};
~~~

Como mencionado anteriormente, o método de ofuscação utilizado acima é o *packing*. Outra maneira de desempacotar esse tipo de código é localizar o valor retornado ao final e usar **console.log** para imprimi-lo em vez de executá-lo.

## Engenharia reversa

Embora essas ferramentas estejam realizando um bom trabalho para tornar o código compreensível, à medida que ele se torna mais ofuscado e codificado, fica muito mais difícil para ferramentas automatizadas limpá-lo. Isso é especialmente verdadeiro quando o código foi ofuscado com uma ferramenta de ofuscação personalizada.

Nesses casos, precisamos realizar engenharia reversa manual do código para compreender como ele foi ofuscado e qual é sua funcionalidade. Se você tiver interesse em aprender mais sobre desofuscação avançada de JavaScript e engenharia reversa, poderá consultar o módulo **Secure Coding 101**, que aborda esse tópico detalhadamente.
