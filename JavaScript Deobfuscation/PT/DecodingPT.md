# Decodificação

Depois de realizarmos o exercício da seção anterior, obtivemos um estranho bloco de texto que parece estar codificado:

~~~shellsession
JLMreal@htb[/htb]$ curl http://SERVER_IP:PORT/serial.php -X POST -d "param1=sample"

ZG8gdGhlIGV4ZXJjaXNlLCBkb24ndCBjb3B5IGFuZCBwYXN0ZSA7KQo=
~~~

Esse é outro aspecto importante da ofuscação ao qual nos referimos em **More Obfuscation**, na seção **Advanced Obfuscation**. Muitas técnicas podem ofuscar ainda mais o código, tornando-o menos legível para humanos e menos detectável por sistemas. Por esse motivo, encontraremos com muita frequência códigos ofuscados que contêm blocos de texto codificado, os quais são decodificados durante a execução. Abordaremos três dos métodos de codificação de texto mais utilizados:

- base64
- hex
- rot13

## Base64

A codificação base64 normalmente é utilizada para reduzir o uso de caracteres especiais, pois quaisquer caracteres codificados em base64 serão representados apenas por caracteres alfanuméricos, além de **+** e **/**. Independentemente da entrada, mesmo que ela esteja em formato binário, a string resultante codificada em base64 utilizará apenas esses caracteres.

### Identificando Base64

Strings codificadas em base64 são facilmente identificadas porque contêm apenas caracteres alfanuméricos. Entretanto, a característica mais distintiva do base64 é seu preenchimento (*padding*) com caracteres **=**. O comprimento das strings codificadas em base64 precisa ser múltiplo de 4. Se a saída resultante tiver apenas três caracteres, por exemplo, um **=** adicional será acrescentado como preenchimento, e assim por diante.

### Codificação em Base64

Para codificar qualquer texto em base64 no Linux, podemos passá-lo com **echo** por um pipe **|** para o comando **base64**:

~~~shellsession
JLMreal@htb[/htb]$ echo https://www.hackthebox.eu/ | base64

aHR0cHM6Ly93d3cuaGFja3RoZWJveC5ldS8K
~~~

### Decodificação de Base64

Se quisermos decodificar qualquer string codificada em base64, podemos usar **base64 -d**, da seguinte forma:

~~~shellsession
JLMreal@htb[/htb]$ echo aHR0cHM6Ly93d3cuaGFja3RoZWJveC5ldS8K | base64 -d

https://www.hackthebox.eu/
~~~

## Hex

Outro método comum é a codificação hexadecimal, que codifica cada caractere de acordo com seu valor hexadecimal na tabela ASCII. Por exemplo, **a** é **61** em hexadecimal, **b** é **62**, **c** é **63**, e assim por diante. Podemos consultar a tabela ASCII completa no Linux usando o comando **man ascii**.

### Identificando Hex

Qualquer string codificada em hexadecimal será composta somente por caracteres hexadecimais, que formam um conjunto de 16 caracteres: **0-9** e **a-f**. Isso torna as strings hexadecimais tão fáceis de identificar quanto strings codificadas em base64.

### Codificação em Hex

Para codificar qualquer string em hexadecimal no Linux, podemos usar o comando **xxd -p**:

~~~shellsession
JLMreal@htb[/htb]$ echo https://www.hackthebox.eu/ | xxd -p

68747470733a2f2f7777772e6861636b746865626f782e65752f0a
~~~

### Decodificação de Hex

Para decodificar uma string codificada em hexadecimal, podemos usar o comando **xxd -p -r**:

~~~shellsession
JLMreal@htb[/htb]$ echo 68747470733a2f2f7777772e6861636b746865626f782e65752f0a | xxd -p -r

https://www.hackthebox.eu/
~~~

## Caesar/Rot13

Outra técnica de codificação comum — e muito antiga — é a cifra de César, que desloca cada letra por uma quantidade fixa. Por exemplo, um deslocamento de um caractere transforma **a** em **b**, **b** em **c**, e assim por diante. Muitas variações da cifra de César utilizam quantidades diferentes de deslocamentos. A mais comum é rot13, que desloca cada caractere 13 posições para a frente.

### Identificando Caesar/Rot13

Embora esse método faça qualquer texto parecer aleatório, ainda é possível identificá-lo porque cada caractere é mapeado para um caractere específico. Por exemplo, em rot13, **http://www** torna-se **uggc://jjj**, o que ainda preserva algumas semelhanças e pode ser reconhecido.

### Codificação em Rot13

Não existe um comando específico no Linux para codificação rot13. Entretanto, é bastante fácil criar nosso próprio comando para realizar o deslocamento de caracteres:

~~~shellsession
JLMreal@htb[/htb]$ echo https://www.hackthebox.eu/ | tr 'A-Za-z' 'N-ZA-Mn-za-m'

uggcf://jjj.unpxgurobk.rh/
~~~

### Decodificação de Rot13

Também podemos usar o mesmo comando anterior para decodificar rot13:

~~~shellsession
JLMreal@htb[/htb]$ echo uggcf://jjj.unpxgurobk.rh/ | tr 'A-Za-z' 'N-ZA-Mn-za-m'

https://www.hackthebox.eu/
~~~

Outra opção para codificar ou decodificar rot13 é utilizar uma ferramenta online, como rot13.

## Outros tipos de codificação

Existem centenas de outros métodos de codificação disponíveis online. Embora esses sejam os mais comuns, às vezes encontraremos outros métodos que poderão exigir alguma experiência para serem identificados e decodificados.

Se você encontrar tipos semelhantes de codificação, primeiro tente determinar qual é o método e depois procure ferramentas online para decodificá-lo.

Algumas ferramentas podem nos ajudar a determinar automaticamente o tipo de codificação, como o Cipher Identifier. Experimente as strings codificadas acima no Cipher Identifier para verificar se ele consegue identificar corretamente o método utilizado.

Além de codificação, muitas ferramentas de ofuscação utilizam criptografia, isto é, codificam uma string usando uma chave, o que pode tornar o código ofuscado muito difícil de submeter a engenharia reversa e desofuscar, especialmente se a chave de descriptografia não estiver armazenada no próprio script.
