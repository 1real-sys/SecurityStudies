# Decodificação de dados em código ofuscado

## Visão geral

Código ofuscado frequentemente armazena strings em representações codificadas e as recupera somente durante a execução. Isso pode esconder URLs, mensagens, nomes de funções e outros indicadores de uma inspeção superficial.

Os três formatos abordados são:

| Formato | Caracteres típicos | Característica útil |
| --- | --- | --- |
| Base64 | A-Z, a-z, 0-9, +, / e = | Comprimento múltiplo de 4 e padding frequente |
| Hex | 0-9 e a-f | Geralmente dois dígitos por byte |
| ROT13 | Letras | Preserva pontuação e é simétrico |

## Exercício inicial

Requisição apresentada no material:

~~~shellsession
JLMreal@htb[/htb]$ curl http://SERVER_IP:PORT/serial.php -X POST -d "param1=sample"

ZG8gdGhlIGV4ZXJjaXNlLCBkb24ndCBjb3B5IGFuZCBwYXN0ZSA7KQo=
~~~

A resposta possui aparência de Base64. Ela pode ser decodificada com:

~~~bash
echo ZG8gdGhlIGV4ZXJjaXNlLCBkb24ndCBjb3B5IGFuZCBwYXN0ZSA7KQo= | base64 -d
~~~

Resultado:

~~~text
do the exercise, don't copy and paste ;)
~~~

## Base64

Base64 converte bytes em caracteres imprimíveis. É útil para transportar dados binários ou evitar caracteres incompatíveis com determinado meio, mas não oferece confidencialidade.

### Como reconhecer

- alfabeto limitado a letras, números, **+** e **/** no formato clássico;
- comprimento normalmente múltiplo de 4;
- pode terminar em **=** ou **==**;
- blocos longos frequentemente apresentam aparência alfanumérica uniforme.

O padding não aparece obrigatoriamente em todas as variantes ou implementações, portanto sua ausência não descarta Base64.

### Codificar

~~~shellsession
JLMreal@htb[/htb]$ echo https://www.hackthebox.eu/ | base64

aHR0cHM6Ly93d3cuaGFja3RoZWJveC5ldS8K
~~~

### Decodificar

~~~shellsession
JLMreal@htb[/htb]$ echo aHR0cHM6Ly93d3cuaGFja3RoZWJveC5ldS8K | base64 -d

https://www.hackthebox.eu/
~~~

O sufixo decodificado inclui uma quebra de linha porque **echo** adiciona newline por padrão. O byte correspondente aparece codificado como parte do resultado.

Para codificar sem newline, um exemplo adicional é:

~~~bash
printf %s 'https://www.hackthebox.eu/' | base64
~~~

## Hexadecimal

Hex representa cada byte por dois caracteres de 0 a 9 e de a a f. A tabela ASCII pode ser consultada com:

~~~bash
man ascii
~~~

### Codificar

~~~shellsession
JLMreal@htb[/htb]$ echo https://www.hackthebox.eu/ | xxd -p

68747470733a2f2f7777772e6861636b746865626f782e65752f0a
~~~

O final **0a** representa a quebra de linha adicionada por **echo**.

### Decodificar

~~~shellsession
JLMreal@htb[/htb]$ echo 68747470733a2f2f7777772e6861636b746865626f782e65752f0a | xxd -p -r

https://www.hackthebox.eu/
~~~

Argumentos:

- **xxd -p** → produz hexadecimal simples, sem endereços;
- **xxd -p -r** → reverte hexadecimal simples para bytes.

## ROT13 e cifra de César

A cifra de César desloca letras por um número fixo de posições. ROT13 aplica deslocamento de 13 posições ao alfabeto latino.

Como existem 26 letras, aplicar ROT13 duas vezes recupera o texto original:

~~~text
texto → ROT13 → texto codificado → ROT13 → texto
~~~

Pontuação, números e barras permanecem inalterados. Por isso, uma URL ainda pode conservar uma estrutura reconhecível:

~~~text
http://www → uggc://jjj
~~~

### Codificar

~~~shellsession
JLMreal@htb[/htb]$ echo https://www.hackthebox.eu/ | tr 'A-Za-z' 'N-ZA-Mn-za-m'

uggcf://jjj.unpxgurobk.rh/
~~~

### Decodificar

~~~shellsession
JLMreal@htb[/htb]$ echo uggcf://jjj.unpxgurobk.rh/ | tr 'A-Za-z' 'N-ZA-Mn-za-m'

https://www.hackthebox.eu/
~~~

O comando **tr** substitui cada caractere do primeiro conjunto pelo correspondente no segundo. O mesmo mapeamento serve para codificar e decodificar ROT13.

## Identificação prática

Antes de decodificar:

1. observe o conjunto de caracteres;
2. verifique comprimento e padding;
3. procure estruturas preservadas, como **://**;
4. considere se cada par pode representar um byte hexadecimal;
5. tente uma camada de cada vez;
6. examine se a saída obtida parece outro formato codificado.

Ferramentas como Cipher Identifier podem sugerir formatos, mas a identificação automática não é infalível.

## Codificação versus criptografia

O original descreve criptografia como codificação com uma chave, mas tecnicamente há uma distinção importante:

- **Codificação:** muda a representação e não depende de segredo;
- **Criptografia:** busca confidencialidade e utiliza um algoritmo com chave;
- **Hashing:** produz um resumo normalmente não reversível;
- **Ofuscação:** dificulta a compreensão sem garantir confidencialidade.

Se o código precisa descriptografar dados localmente, a chave ou um meio de obtê-la pode estar presente durante a execução. Ainda assim, criptografia bem aplicada é conceitualmente diferente de Base64, hex ou ROT13.

## Pontos-chave para revisão

- Base64, hex e ROT13 são reversíveis sem chave.
- Base64 pode ser reconhecido pelo alfabeto, tamanho e padding.
- Hex normalmente usa dois caracteres por byte.
- ROT13 é simétrico e preserva caracteres não alfabéticos.
- **echo** adiciona uma quebra de linha que também é codificada.
- Código ofuscado pode aplicar várias camadas sucessivas.
- Codificação não fornece confidencialidade.
- Resultados automáticos devem ser confirmados manualmente.
