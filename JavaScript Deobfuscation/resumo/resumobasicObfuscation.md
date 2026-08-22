# Ofuscação básica de JavaScript

## Visão geral

Ofuscação normalmente é aplicada por ferramentas automáticas. O exemplo do material parte de um código JavaScript simples, confirma seu comportamento, aplica minificação e depois utiliza um *packer* para dificultar sua leitura.

Código original:

```javascript
console.log('HTB JavaScript Deobfuscation Module');
```

Ao ser executado, `console.log()` escreve a mensagem no console do navegador. Essa saída conhecida serve como referência para verificar se as transformações preservam o comportamento.

## Minificação

Minificação reduz o tamanho e a legibilidade superficial do código por meio de transformações como:

- remoção de espaços e quebras de linha;
- remoção de comentários;
- compactação de expressões;
- em algumas ferramentas, encurtamento de identificadores locais.

O laboratório utiliza:

```text
https://javascript-minifier.com/
```

<a href="../IMG/JSOBS2.png">
  <img src="../IMG/JSOBS2.png" alt="Ferramenta apresentando JavaScript original e sua versão minificada">
</a>

Arquivos JavaScript minificados normalmente usam o sufixo `.min.js`, como em `jquery.min.js`. A extensão é apenas uma convenção de nome; o navegador continua interpretando JavaScript normal.

### Minificação versus ofuscação

| Aspecto | Minificação | Ofuscação |
| --- | --- | --- |
| Objetivo principal | Reduzir tamanho e melhorar entrega | Dificultar compreensão e engenharia reversa |
| Legibilidade | Diminui como efeito colateral | Diminui deliberadamente |
| Sobrecarga em execução | Normalmente baixa ou inexistente | Pode exigir reconstrução dinâmica |
| Reversibilidade prática | Um beautifier recupera boa parte da estrutura | Pode exigir análise de tabelas, funções e fluxo |

## Packing

O material utiliza o JavaScript Obfuscator do BeautifyTools:

```text
http://beautifytools.com/javascript-obfuscator.php
```

<a href="../IMG/JSOBS3.png">
  <img src="../IMG/JSOBS3.png" alt="BeautifyTools mostrando JavaScript transformado por packing">
</a>

Saída preservada do exemplo:

```javascript
eval(function(p,a,c,k,e,d){e=function(c){return c};if(!''.replace(/^/,String)){while(c--){d[c]=k[c]||c}k=[function(e){return d[e]}];e=function(){return'\\w+'};c=1};while(c--){if(k[c]){p=p.replace(new RegExp('\\b'+e(c)+'\\b','g'),k[c])}}return p}('5.4(\'3 2 1 0\');',6,6,'Module|Deobfuscation|JavaScript|HTB|log|console'.split('|'),0,{}))
```

Esse padrão é conhecido como *packer*. Ele armazena componentes do código em uma tabela e utiliza uma função para reconstruir a expressão original. O padrão `function(p,a,c,k,e,d)` é uma assinatura visual comum desse tipo de empacotamento, embora os nomes dos parâmetros possam variar.

## Leitura conceitual do código empacotado

No exemplo, a tabela contém:

```text
Module|Deobfuscation|JavaScript|HTB|log|console
```

A chamada `.split('|')` converte a string em uma lista de palavras. Os números presentes na expressão empacotada funcionam como referências aos itens dessa lista. A função externa substitui as referências e retorna o JavaScript reconstruído, que então é executado por `eval()`.

De forma conceitual:

```text
5.4('3 2 1 0');
↓ substituição pelo dicionário
console.log('HTB JavaScript Deobfuscation Module');
```

## Verificação funcional

O código empacotado é executado novamente em:

```text
https://jsconsole.com
```

<a href="../IMG/JSOBS4.png">
  <img src="../IMG/JSOBS4.png" alt="JSConsole comprovando que o código empacotado mantém a saída original">
</a>

A mesma mensagem confirma que, apesar da mudança de representação, a funcionalidade principal foi preservada.

## Limitações do packing

Embora o código fique difícil de ler, strings importantes podem continuar expostas em texto claro. No exemplo, palavras como `console`, `log`, `HTB` e `JavaScript` aparecem no dicionário.

Isso pode revelar:

- APIs utilizadas;
- mensagens e nomes internos;
- URLs e domínios;
- comandos ou parâmetros;
- indícios da finalidade do script.

Por esse motivo, ferramentas podem combinar packing com codificação de strings, alterações de fluxo e outras camadas.

## Abordagem de desofuscação

1. Reconheça a estrutura `eval(function(p,a,c,k,e,d)...)`.
2. Preserve o código original.
3. Evite executar conteúdo desconhecido diretamente.
4. Intercepte ou substitua `eval()` para observar a string reconstruída.
5. Examine a tabela criada por `.split('|')`.
6. Formate a saída desempacotada.
7. Compare seu comportamento com o código original.

Em código desconhecido, executar o *packer* pode acionar sua carga final. A análise deve ocorrer em ambiente isolado e autorizado.

## Pontos-chave para revisão

- Minificação e ofuscação têm objetivos diferentes.
- `.min.js` é uma convenção para arquivos minificados.
- Packing reconstrói o código durante a execução.
- `function(p,a,c,k,e,d)` é um padrão comum de packers JavaScript.
- `eval()` executa a string reconstruída.
- Strings em texto claro podem revelar a funcionalidade mesmo antes da desofuscação completa.
- O comportamento deve permanecer igual antes e depois da transformação.
