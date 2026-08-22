# Ofuscação avançada de JavaScript

## O que muda em relação à ofuscação básica

Na ofuscação básica por packing, a estrutura do programa fica difícil de ler, mas strings importantes podem continuar visíveis. Técnicas mais avançadas também transformam essas strings, alteram identificadores e adicionam funções auxiliares para reconstruir os valores somente durante a execução.

O objetivo é reduzir indícios imediatos da funcionalidade original, aumentando o esforço necessário para análise estática.

## Obfuscator.io

O material utiliza:

~~~text
https://obfuscator.io
~~~

A opção **String Array Encoding** é configurada como **Base64**:

<a href="../IMG/JSOBS5.png">
  <img src="../IMG/JSOBS5.png" alt="Configuração Base64 para o array de strings no Obfuscator.io">
</a>

Depois, o código original é inserido e processado:

<a href="../IMG/JSOBS6.png">
  <img src="../IMG/JSOBS6.png" alt="Código JavaScript original preparado para ofuscação">
</a>

## Estrutura da saída

O código gerado contém padrões importantes para análise:

- identificadores hexadecimais, como _0x1ec6;
- array de strings codificadas;
- rotação do array com push() e shift();
- função responsável por localizar e decodificar itens;
- alfabeto Base64 em texto claro;
- conversão por String.fromCharCode();
- uso de decodeURIComponent();
- cache de resultados já decodificados.

Trecho completo apresentado no material:

~~~javascript
var _0x1ec6=['Bg9N','sfrciePHDMfty3jPChqGrgvVyMz1C2nHDgLVBIbnB2r1Bgu='];(function(_0x13249d,_0x1ec6e5){var _0x14f83b=function(_0x3f720f){while(--_0x3f720f){_0x13249d['push'](_0x13249d['shift']());}};_0x14f83b(++_0x1ec6e5);}(_0x1ec6,0xb4));var _0x14f8=function(_0x13249d,_0x1ec6e5){_0x13249d=_0x13249d-0x0;var _0x14f83b=_0x1ec6[_0x13249d];if(_0x14f8['eOTqeL']===undefined){var _0x3f720f=function(_0x32fbfd){var _0x523045='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+/=',_0x4f8a49=String(_0x32fbfd)['replace'](/=+$/,'');var _0x1171d4='';for(var _0x44920a=0x0,_0x2a30c5,_0x443b2f,_0xcdf142=0x0;_0x443b2f=_0x4f8a49['charAt'](_0xcdf142++);~_0x443b2f&&(_0x2a30c5=_0x44920a%0x4?_0x2a30c5*0x40+_0x443b2f:_0x443b2f,_0x44920a++%0x4)?_0x1171d4+=String['fromCharCode'](0xff&_0x2a30c5>>(-0x2*_0x44920a&0x6)):0x0){_0x443b2f=_0x523045['indexOf'](_0x443b2f);}return _0x1171d4;};_0x14f8['oZlYBE']=function(_0x8f2071){var _0x49af5e=_0x3f720f(_0x8f2071);var _0x52e65f=[];for(var _0x1ed1cf=0x0,_0x79942e=_0x49af5e['length'];_0x1ed1cf<_0x79942e;_0x1ed1cf++){_0x52e65f+='%'+('00'+_0x49af5e['charCodeAt'](_0x1ed1cf)['toString'](0x10))['slice'](-0x2);}return decodeURIComponent(_0x52e65f);},_0x14f8['qHtbNC']={},_0x14f8['eOTqeL']=!![];}var _0x20247c=_0x14f8['qHtbNC'][_0x13249d];return _0x20247c===undefined?(_0x14f83b=_0x14f8['oZlYBE'](_0x14f83b),_0x14f8['qHtbNC'][_0x13249d]=_0x14f83b):_0x14f83b=_0x20247c,_0x14f83b;};console[_0x14f8('0x0')](_0x14f8('0x1'));
~~~

## Base64 não é criptografia

Base64 apenas representa bytes com outro conjunto de caracteres. A própria rotina de decodificação precisa acompanhar o JavaScript para que ele seja executado, permitindo que um analista recupere os valores.

Portanto, essa opção:

- oculta strings de uma inspeção superficial;
- pode evitar correspondências literais simples;
- não fornece confidencialidade;
- não substitui criptografia nem protege segredos no cliente.

## Rotação e resolução do array

A função autoexecutável rotaciona a tabela:

~~~javascript
_0x13249d['push'](_0x13249d['shift']());
~~~

Depois, chamadas como estas recuperam entradas por índice:

~~~javascript
_0x14f8('0x0')
_0x14f8('0x1')
~~~

Para analisar esse padrão, é necessário considerar a ordem final do array após a rotação, e não apenas sua ordem inicial.

## Ofuscação baseada em coerção de tipos

O segundo exemplo utiliza combinações como:

~~~javascript
![]
!![]
[]+[]
[][[]]
+[]
+!+[]
~~~

Em JavaScript, coerções implícitas convertem esses valores em booleanos, números e strings. Caracteres são extraídos de representações como false, true e undefined até que nomes de propriedades e instruções completas sejam construídos.

Esse estilo é associado a técnicas como JSFuck, que constroem JavaScript com um conjunto extremamente limitado de caracteres.

<a href="../IMG/JSOBS7.png">
  <img src="../IMG/JSOBS7.png" alt="Código baseado em coerção de tipos executado no JSConsole">
</a>

O original contém apenas uma versão cortada do código porque a expressão completa é muito extensa.

## Impacto no desempenho

Ofuscação avançada pode adicionar:

- loops para reorganizar tabelas;
- decodificação de strings durante a execução;
- chamadas indiretas;
- expressões muito maiores que o código original;
- consumo adicional de CPU e memória;
- tempo maior de parsing e compilação.

JJ Encode, AA Encode e técnicas semelhantes podem produzir código particularmente grande e lento. Essa sobrecarga deve ser considerada mesmo em usos legítimos.

## Estratégia de análise

1. Preserve a amostra original.
2. Formate o código sem executá-lo.
3. Identifique tabelas de strings e funções auxiliares.
4. Localize operações de rotação ou embaralhamento.
5. Isole a função de decodificação.
6. Substitua o ponto de execução por uma forma segura de registrar a saída.
7. Recupere strings e renomeie identificadores conforme seu papel.
8. Compare o comportamento antes e depois da desofuscação.

Código desconhecido deve ser analisado em ambiente isolado. A função de decodificação pode parecer inofensiva enquanto outra parte realiza ações maliciosas após reconstruir as strings.

## Pontos-chave para revisão

- Ofuscação avançada também busca ocultar strings.
- Base64 é codificação, não criptografia.
- Arrays podem ser rotacionados antes da resolução dos índices.
- Identificadores hexadecimais não possuem significado próprio.
- Coerções de tipos permitem construir código com poucos caracteres.
- Ofuscação mais complexa geralmente aumenta o custo de execução.
- O comportamento original precisa continuar funcionando após a transformação.
- Nenhuma ofuscação torna segredos do lado do cliente realmente inacessíveis.
