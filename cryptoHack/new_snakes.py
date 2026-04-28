#!/usr/bin/env python3

#Pagina 1

import sys
import base64
from Crypto.Util.number import *
# import this

if sys.version_info.major == 2:
    print("You are running Python 2, which is no longer supported. Please update to Python 3.")

ords = [81, 64, 75, 66, 70, 93, 73, 72, 1, 92, 109, 2, 84, 109, 66, 75, 70, 90, 2, 92, 79]

print("Here is your flag:")
# para cada número da lista:
# 1. faz XOR com 0x32 (50)
# 2. transforma o resultado em caractere (chr)
# 3. junta tudo em uma string (join)
# 4. imprime o resultado final
print("".join(chr(o ^ 0x32) for o in ords))


#Página 2 

ords2 = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
print("Here is your second flag:")
# para cada número da lista:
# 1. usa chr(o) para converter o número em caractere ASCII
# 2. gera uma sequência de caracteres
# 3. o join junta tudo em uma string única
print("".join(chr(o) for o in ords2))




"""
ASCII é um padrão de codificação de 7 bits que permite representar texto usando números inteiros de 0 a 127.

Usando o array de inteiros abaixo, converta os números para seus caracteres ASCII correspondentes para obter uma flag.

Em Python, a função chr() pode ser usada para converter um número ASCII (ordinal) em um caractere (a função ord() faz o contrário).

Cada letra, número ou símbolo tem um código numérico no ASCII.
Por exemplo: 65 = 'A', 97 = 'a', 48 = '0'.
O intervalo 0–127 cobre o ASCII básico (letras, números e símbolos comuns).
Quando você vê uma lista de números nessa faixa, muitas vezes é texto codificado diretamente.
Em desafios, isso costuma ser o passo mais simples: só converter número → caractere.

"""



#Página 3 

"""
Quando criptografamos algo, o texto cifrado resultante geralmente contém bytes que não são caracteres ASCII imprimíveis. Se quisermos compartilhar nossos dados criptografados, é comum codificá-los em algo mais amigável e portátil entre diferentes sistemas.

O hexadecimal pode ser usado dessa forma para representar strings ASCII. Primeiro, cada letra é convertida em um número ordinal de acordo com a tabela ASCII (como no desafio anterior). Em seguida, os números decimais são convertidos em números de base 16, também conhecidos como hexadecimal. Os números podem ser combinados em uma longa string hexadecimal.

Em Python, a função bytes.fromhex() pode ser usada para converter hexadecimal em bytes. O método .hex() pode ser chamado em objetos do tipo bytes para obter a representação hexadecimal.

Hexadecimal usa base 16: 0–9 e a–f.
Cada byte (8 bits) vira 2 caracteres hex (ex: ff, 2a, 7b).
Hex é só representação, não é criptografia.
Muito usado porque é fácil de transportar (texto puro, sem caracteres estranhos).
Você vai ver isso o tempo todo em segurança: hashes, payloads, dumps de memória.
"""
hexString = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"
bytesFlag= bytes.fromhex(hexString).decode() 
# converte o texto hexadecimal em bytes reais (dados binários) e depois decodifica esses bytes para obter a string legível (a flag).
print(bytesFlag)


#Página 4

"""
utro esquema comum de codificação é o Base64, que permite representar dados binários como uma string ASCII usando um alfabeto de 64 caracteres. Um caractere em Base64 representa 6 bits, e assim 4 caracteres em Base64 representam 3 bytes (24 bits).

O Base64 é muito usado na web, então dados binários como imagens podem ser facilmente incluídos em arquivos HTML ou CSS.

Em Python, após importar o módulo base64 com import base64, você pode usar a função base64.b64encode(). Lembre-se de decodificar o hexadecimal primeiro, como o enunciado pede.

🧠 Complemento (curto e direto)
Base64 não criptografa, só transforma dados binários em texto.
Usa um conjunto de 64 caracteres: letras, números, + e /.
O resultado pode ter = no final (padding).
Muito usado em APIs, tokens e arquivos embutidos (ex: imagens em HTML).
Sempre trabalha com bytes, então conversões são comuns (hex → bytes → base64).
"""

hexString2 = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
bytesFlag2 = bytes.fromhex(hexString2)
base64Flag2 = base64.b64encode(bytesFlag2)
print("".join(base64Flag2.decode()))


## Página 5

"""
Sistemas criptográficos como o RSA trabalham com números, mas as mensagens são feitas de caracteres. Como devemos converter nossas mensagens em números para que operações matemáticas possam ser aplicadas?

A forma mais comum é pegar os bytes ASCII da mensagem, convertê-los para hexadecimal e concatenar. Isso pode ser interpretado como um número em base 16 (hexadecimal) e também representado em base 10 (decimal).

Para ilustrar:

mensagem: HELLO
bytes ASCII: [72, 69, 76, 76, 79]
bytes em hex: [0x48, 0x45, 0x4c, 0x4c, 0x4f]
base-16: 0x48454c4c4f
base-10: 310400273487

A biblioteca PyCryptodome do Python implementa isso com os métodos bytes_to_long() e long_to_bytes(). Você precisa instalar e importar com:
from Crypto.Util.number import *

RSA só entende números grandes, não texto direto.
Converter texto → número é essencial pra criptografia funcionar.
bytes_to_long() junta vários bytes em um número gigante.
long_to_bytes() faz o caminho inverso (número → texto).
Isso é basicamente tratar a mensagem como um número em base 256.
"""
n = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
# converte o número grande de volta para bytes (dados binários)
data = long_to_bytes(n)
# converte os bytes para string (texto legível) e imprime
print(data.decode())

#Página 6
"""
XOR é um operador bit a bit que retorna 0 se os bits forem iguais, e 1 caso contrário. Em livros, o operador XOR é representado por ⊕, mas na maioria das linguagens e desafios você verá o símbolo ^ sendo usado.

Para números binários maiores, aplicamos XOR bit a bit:
0110 ^ 1010 = 1100

Podemos aplicar XOR em inteiros convertendo-os de decimal para binário. Também podemos aplicar XOR em strings convertendo cada caractere para seu valor numérico (Unicode/ASCII).

Dada a string label, aplique XOR com o número 13 em cada caractere. Depois converta de volta para string e envie no formato: crypto{new_string}.

A biblioteca pwntools do Python possui uma função xor() que facilita isso, mas você também pode implementar manualmente.

XOR funciona bit a bit (nível binário).
Muito usado em criptografia simples e CTF.
Aplicar XOR duas vezes com o mesmo número volta ao original.
ord() transforma letra → número.
chr() transforma número → letra.
"""
texto = "label"
resultado = ""

for letra in texto:
    # converte a letra para número (ASCII/Unicode)
    numero = ord(letra)
    # aplica XOR com 13
    xor1 = numero ^ 13
    # converte de volta para caractere e adiciona na string final
    resultado += chr(xor1)
print(resultado)