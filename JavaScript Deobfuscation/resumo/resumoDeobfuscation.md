# Desofuscação de JavaScript

## Objetivo

Desofuscar significa recuperar uma representação compreensível do código e explicar seu comportamento. O processo normalmente passa por duas etapas diferentes:

1. **Beautification:** reorganiza indentação e quebras de linha.
2. **Deobfuscation:** desfaz transformações que ocultam a lógica.

Formatar melhora a aparência, mas não necessariamente recupera nomes, strings ou o fluxo original.

## Pretty Print no navegador

Quando um arquivo está minificado em uma única linha, o depurador do navegador pode aplicar **Pretty Print**. No Firefox, o material orienta:

1. abrir o debugger com **CTRL+SHIFT+Z**;
2. selecionar **secret.js**;
3. clicar no botão **{ }**.

Isso reorganiza blocos, funções e expressões. O código continua semanticamente igual e ainda pode permanecer ofuscado.

## Ferramentas de formatação

As ferramentas citadas são:

~~~text
https://prettier.io/playground/
https://beautifier.io/
~~~

Prettier e Beautifier ajudam a:

- separar instruções;
- aplicar indentação consistente;
- revelar blocos e escopos;
- facilitar a localização de funções e expressões;
- preparar o código para análise manual.

Elas não desfazem automaticamente todas as tabelas, substituições ou construções dinâmicas.

## Código empacotado do exercício

~~~javascript
eval(function (p, a, c, k, e, d) { e = function (c) { return c.toString(36) }; if (!''.replace(/^/, String)) { while (c--) { d[c.toString(a)] = k[c] || c.toString(a) } k = [function (e) { return d[e] }]; e = function () { return '\\w+' }; c = 1 }; while (c--) { if (k[c]) { p = p.replace(new RegExp('\\b' + e(c) + '\\b', 'g'), k[c]) } } return p }('g 4(){0 5="6{7!}";0 1=8 a();0 2="/9.c";1.d("e",2,f);1.b(3)}', 17, 17, 'var|xhr|url|null|generateSerial|flag|HTB|flag|new|serial|XMLHttpRequest|send|php|open|POST|true|function'.split('|'), 0, {}))
~~~

Elementos importantes:

- **eval(...)** executa o código reconstruído;
- a string iniciada por **g 4()** contém referências compactadas;
- o valor **17** informa parâmetros usados pelo packer;
- **.split('|')** produz um dicionário de palavras;
- expressões regulares substituem os índices pelos termos originais.

## UnPacker

O material utiliza:

~~~text
https://matthewfl.com/unPacker.html
~~~

Não devem existir linhas vazias antes do script, pois elas podem afetar o reconhecimento do formato pelo UnPacker.

Resultado legível:

~~~javascript
function generateSerial() {
  ...SNIP...
  var xhr = new XMLHttpRequest;
  var url = "/serial.php";
  xhr.open("POST", url, true);
  xhr.send(null);
};
~~~

## O que o código faz

O trecho desofuscado revela:

- uma função chamada **generateSerial**;
- criação de um objeto **XMLHttpRequest**;
- destino **/serial.php**;
- uso do método HTTP **POST**;
- execução assíncrona, indicada por **true**;
- envio de uma requisição sem corpo com **xhr.send(null)**.

Essa informação não era evidente na representação empacotada, embora palavras importantes estivessem presentes no dicionário.

## Desempacotamento sem executar a carga

Packers frequentemente terminam retornando a string reconstruída para **eval()**. Uma técnica de análise consiste em capturar esse retorno com **console.log()** em vez de executá-lo.

Fluxo conceitual:

~~~text
packer → reconstrói string → eval executa
                         ↓
                  console.log exibe
~~~

Essa alteração deve ser feita em uma cópia e dentro de ambiente controlado. Nem todo ofuscador usa o mesmo padrão, e executar parcialmente código desconhecido ainda pode apresentar riscos.

## Quando ferramentas automáticas falham

Automação pode falhar quando há:

- ofuscador personalizado;
- várias camadas de packing e codificação;
- valores dependentes do ambiente;
- verificações contra debugging;
- código automodificável;
- strings recuperadas por rede;
- funções de decodificação misturadas à lógica principal.

Nesses casos, é necessário rastrear manualmente entradas, transformações e efeitos.

## Estratégia de engenharia reversa

1. Preserve a amostra original e calcule seu hash.
2. Trabalhe em uma cópia isolada.
3. Formate o código.
4. Identifique o ponto inicial de execução.
5. Localize **eval()**, **Function()** e funções decodificadoras.
6. Intercepte a saída antes da execução dinâmica.
7. Remova uma camada por vez.
8. Renomeie variáveis conforme sua finalidade se tornar clara.
9. Registre URLs, métodos HTTP, parâmetros e indicadores.
10. Compare o comportamento da versão desofuscada com o original.

## Pontos-chave para revisão

- Beautify não é o mesmo que desofuscar.
- Pretty Print recupera estrutura visual, não a lógica original.
- O padrão **function(p,a,c,k,e,d)** indica packing comum.
- UnPacker automatiza a reconstrução desse formato.
- Substituir a execução pela impressão do retorno pode revelar a carga.
- O código analisado realiza uma requisição POST para **/serial.php**.
- Ofuscadores personalizados frequentemente exigem engenharia reversa manual.
- Código desconhecido deve ser manipulado somente em ambiente isolado e autorizado.
