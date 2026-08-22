# Ofuscação básica

A ofuscação de código normalmente não é realizada manualmente, pois existem muitas ferramentas para diversas linguagens que automatizam esse processo. É possível encontrar muitas ferramentas online para essa finalidade, embora diversos agentes maliciosos e desenvolvedores profissionais criem seus próprios ofuscadores para tornar a desofuscação mais difícil.

## Executando código JavaScript

Vamos usar a seguinte linha de código como exemplo e tentar ofuscá-la:

```javascript
console.log('HTB JavaScript Deobfuscation Module');
```

Primeiro, vamos testar a execução desse código em texto claro para vê-lo funcionando. Podemos acessar o JSConsole, colar o código, pressionar Enter e observar sua saída:

```text
https://jsconsole.com
```

Saída do console mostrando a mensagem de log `HTB JavaScript Deobfuscation Module` e a versão 2.1.2.

Vemos que essa linha de código imprime `HTB JavaScript Deobfuscation Module`, o que é feito por meio da função `console.log()`.

## Minificando código JavaScript

Uma forma comum de reduzir a legibilidade de um trecho de código JavaScript e, ao mesmo tempo, mantê-lo totalmente funcional é a minificação de JavaScript. Minificar código significa colocar todo o código em uma única linha, que frequentemente é muito longa. A minificação é mais útil para códigos maiores, pois, se nosso código tiver apenas uma linha, sua aparência não será muito diferente depois de minificado.

Muitas ferramentas podem nos ajudar a minificar código JavaScript, como o `javascript-minifier`. Basta copiarmos nosso código, clicarmos em **Minify** e obteremos a saída minificada no lado direito:

```text
https://javascript-minifier.com/
```

<a href="../IMG/JSOBS2.png">
  <img src="../IMG/JSOBS2.png" alt="JavaScript Minifier mostrando o código de entrada e sua saída minificada">
</a>

Novamente, podemos copiar o código minificado para o JSConsole e executá-lo, verificando que ele funciona conforme esperado. Normalmente, códigos JavaScript minificados são salvos com a extensão `.min.js`.

> **Observação:** a minificação de código não é exclusiva do JavaScript e pode ser aplicada a muitas outras linguagens, como é possível observar no `javascript-minifier`.

## Empacotando código JavaScript

Agora, vamos ofuscar nossa linha de código para torná-la mais obscura e difícil de ler. Primeiro, utilizaremos o BeautifyTools para ofuscar nosso código:

```text
http://beautifytools.com/javascript-obfuscator.php
```

<a href="../IMG/JSOBS3.png">
  <img src="../IMG/JSOBS3.png" alt="JavaScript Obfuscator do BeautifyTools exibindo a saída empacotada">
</a>

```javascript
eval(function(p,a,c,k,e,d){e=function(c){return c};if(!''.replace(/^/,String)){while(c--){d[c]=k[c]||c}k=[function(e){return d[e]}];e=function(){return'\\w+'};c=1};while(c--){if(k[c]){p=p.replace(new RegExp('\\b'+e(c)+'\\b','g'),k[c])}}return p}('5.4(\'3 2 1 0\');',6,6,'Module|Deobfuscation|JavaScript|HTB|log|console'.split('|'),0,{}))
```

Vemos que nosso código ficou muito mais ofuscado e difícil de ler. Podemos copiá-lo para `https://jsconsole.com` e verificar se ele ainda executa sua função principal:

```text
https://jsconsole.com
```

<a href="../IMG/JSOBS4.png">
  <img src="../IMG/JSOBS4.png" alt="JSConsole executando o JavaScript empacotado e imprimindo a mensagem original">
</a>

Vemos que obtemos a mesma saída.

> **Observação:** o tipo de ofuscação acima é conhecido como *packing* (empacotamento), geralmente reconhecível pelos seis argumentos utilizados na função inicial: `function(p,a,c,k,e,d)`.

Uma ferramenta de ofuscação do tipo *packer* normalmente tenta converter todas as palavras e símbolos do código em uma lista ou um dicionário e, em seguida, referenciá-los por meio da função `(p,a,c,k,e,d)` para reconstruir o código original durante a execução. A sequência `(p,a,c,k,e,d)` pode variar de um *packer* para outro. Entretanto, ela normalmente contém determinada ordem na qual as palavras e os símbolos do código original foram empacotados, permitindo saber como ordená-los durante a execução.

Embora um *packer* seja muito eficiente para reduzir a legibilidade do código, ainda podemos ver suas principais strings escritas em texto claro, o que pode revelar parte de sua funcionalidade. Por isso, talvez seja necessário procurar maneiras melhores de ofuscar o código.
