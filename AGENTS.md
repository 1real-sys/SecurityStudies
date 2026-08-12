# AGENTS.md

## Objetivo

Este repositório é usado para estudos de Cyber Security, principalmente conteúdos provenientes do Hack The Box (HTB).

O fluxo de trabalho consiste em receber arquivos Markdown em inglês contendo o conteúdo original de uma página de estudo e gerar automaticamente:

1. Uma tradução completa para português.
2. Um resumo didático em português.
3. Conteúdo complementar relevante ao tema, quando isso agregar valor ao estudo.

O conteúdo original **nunca deve ser alterado**.

---

## Estrutura esperada

Cada tema pode possuir sua própria pasta.

Exemplo:

```text
XSS/
├── arquivosoriginais.md
├── PT/
│   └── arquivosoriginaisPT.md
└── resumo/
    └── resumoarquivooriginal.md
```

Outro exemplo:

```text
SQL-Injection/
├── authentication-bypass.md
├── union-clause.md
├── PT/
│   ├── authentication-bypassPT.md
│   └── union-clausePT.md
└── resumo/
    ├── resumoauthentication-bypass.md
    └── resumounion-clause.md
```

---

## Arquivo de entrada

Considere como arquivo de entrada qualquer arquivo `.md` localizado diretamente dentro da pasta do tema.

Arquivos existentes dentro das pastas:

```text
PT/
resumo/
```

não são arquivos de entrada e não devem ser processados novamente.

Exemplo:

```text
XSS/reflected-xss.md
```

é um arquivo original.

Já:

```text
XSS/PT/reflected-xssPT.md
XSS/resumo/resumoreflected-xss.md
```

são arquivos gerados.

---

## Tradução

Para cada arquivo original:

```text
<nome>.md
```

crie:

```text
PT/<nome>PT.md
```

Exemplo:

```text
reflected-xss.md
```

gera:

```text
PT/reflected-xssPT.md
```

### Regras da tradução

A tradução deve:

* Ser escrita em português do Brasil.
* Preservar fielmente o sentido técnico do conteúdo original.
* Não resumir o conteúdo.
* Não remover informações.
* Não simplificar conceitos importantes.
* Manter títulos, subtítulos e estrutura lógica do documento.
* Manter blocos de código.
* Manter comandos de terminal.
* Manter payloads.
* Manter URLs.
* Manter nomes de ferramentas.
* Manter nomes de funções, métodos, parâmetros, headers HTTP e tecnologias.
* Manter termos técnicos em inglês quando a tradução puder causar perda de significado.
* Quando útil, usar o formato português + termo original.

Exemplo:

```text
falsificação de requisição entre sites (Cross-Site Request Forgery — CSRF)
```

Não traduzir comandos ou código.

Exemplo:

```bash
curl -X POST https://example.com
```

deve permanecer exatamente como código.

Payloads também devem permanecer intactos.

Exemplo:

```html
<script>alert(document.domain)</script>
```

não deve ser modificado.

---

## Resumo

Para cada arquivo original:

```text
<nome>.md
```

crie também:

```text
resumo/resumo<nome>.md
```

Exemplo:

```text
reflected-xss.md
```

gera:

```text
resumo/resumoreflected-xss.md
```

O resumo deve ser escrito em português do Brasil.

Ele não deve ser apenas uma versão menor da tradução.

O objetivo é criar um material de revisão e estudo.

---

## Estrutura recomendada do resumo

Adapte a estrutura ao conteúdo, mas prefira algo semelhante a:

```markdown
# Nome do tema

## O que é

Explicação curta e clara.

## Como funciona

Descrição do funcionamento técnico.

## Pontos importantes

- Conceito importante
- Conceito importante
- Conceito importante

## Exemplo

Exemplo técnico relevante.

## Como identificar

Formas comuns de reconhecer ou testar o comportamento.

## Impacto

Possíveis consequências da vulnerabilidade ou técnica.

## Mitigação

Quando aplicável, explique como o problema pode ser prevenido.

## Observações adicionais

Informações complementares úteis para estudo.
```

Não force todas essas seções quando elas não fizerem sentido para o conteúdo.

---

## Conteúdo adicional no resumo

É permitido adicionar conhecimento que não esteja explicitamente presente no arquivo original quando isso ajudar no entendimento do tema.

Exemplos de conteúdo complementar permitido:

* Explicação de um conceito mencionado superficialmente.
* Exemplo adicional.
* Contexto sobre HTTP.
* Contexto sobre navegador.
* Contexto sobre Linux.
* Explicação de um comando.
* Explicação de uma ferramenta.
* Diferença entre conceitos semelhantes.
* Técnicas comuns relacionadas ao tema.
* Mitigações.
* Armadilhas comuns.
* Observações úteis para CTFs e laboratórios.
* Relações com outras vulnerabilidades.

Esse conteúdo deve ser tecnicamente correto e diretamente relacionado ao assunto estudado.

Não adicionar informações apenas para aumentar o tamanho do documento.

---

## Foco didático

Os arquivos em `resumo/` devem servir como material de revisão futura.

Priorize:

* clareza;
* precisão técnica;
* exemplos;
* entendimento do motivo pelo qual algo funciona;
* conceitos importantes para pentest;
* relações entre vulnerabilidades;
* detalhes que ajudem em máquinas HTB e laboratórios.

Sempre que possível, explique não apenas **o que fazer**, mas também **por que funciona**.

---

## Comandos

Quando houver comandos importantes, preserve-os em blocos de código.

Exemplo:

```bash
ffuf -u http://target/FUZZ -w wordlist.txt
```

Quando ajudar no estudo, explique os argumentos principais:

```text
-u → URL alvo
-w → wordlist utilizada
FUZZ → posição que será substituída pelas entradas da wordlist
```

Não alterar o comando original sem necessidade.

---

## Payloads

Payloads de segurança devem ser preservados exatamente quando vierem do conteúdo original.

Se forem adicionados payloads extras no resumo, deixe claro que são exemplos adicionais.

Exemplo:

```html
<script>alert(1)</script>
```

Nunca substituir silenciosamente um payload do material original por outro.

---

## Código

Não modificar código apresentado pelo material original, exceto quando houver um erro evidente e a correção for necessária para explicar o conceito.

Nesse caso:

1. Preserve o código original.
2. Explique o problema.
3. Apresente separadamente uma possível correção.

---

## Criação automática de diretórios

Caso não existam, crie automaticamente:

```text
PT/
resumo/
```

Não é necessário pedir autorização.

---

## Arquivos existentes

Se o arquivo de tradução ou resumo já existir, atualize-o somente quando o arquivo original correspondente tiver sido solicitado novamente para processamento.

Não modificar outros arquivos sem necessidade.

Nunca apagar:

* arquivos originais;
* anotações do usuário;
* outros materiais existentes no diretório.

---

## Regra de escopo

Ao receber uma solicitação para processar um arquivo específico, trabalhe somente nele e nos arquivos derivados dele.

Exemplo:

```text
XSS/reflected-xss.md
```

deve resultar somente em alterações relacionadas a:

```text
XSS/PT/reflected-xssPT.md
XSS/resumo/resumoreflected-xss.md
```

Não processe automaticamente todos os outros arquivos do diretório, salvo quando isso for solicitado explicitamente.

---

## Segurança e contexto de laboratório

O conteúdo deste repositório é voltado para:

* estudo;
* Hack The Box;
* CTFs;
* laboratórios;
* ambientes autorizados;
* aprendizado de Cyber Security.

Ao trabalhar com técnicas ofensivas presentes no material, preserve o conteúdo técnico necessário para que o conceito possa ser estudado corretamente.

Não descaracterize comandos, payloads ou técnicas presentes no material original.

---

## Fluxo padrão

Quando solicitado a processar um arquivo:

1. Leia completamente o arquivo `.md` original.
2. Identifique o diretório do tema.
3. Crie `PT/` caso não exista.
4. Crie `resumo/` caso não exista.
5. Gere a tradução completa.
6. Salve em:

```text
PT/<nome>PT.md
```

7. Gere o resumo didático.
8. Adicione conteúdo complementar relevante quando apropriado.
9. Salve em:

```text
resumo/resumo<nome>.md
```

10. Verifique se blocos de código, comandos e payloads foram preservados corretamente.
11. Não modifique o arquivo original.

---

## Exemplo completo

Entrada:

```text
XSS/xss-basics.md
```

Saídas:

```text
XSS/PT/xss-basicsPT.md
XSS/resumo/resumoxss-basics.md
```

Estrutura final:

```text
XSS/
├── xss-basics.md
├── PT/
│   └── xss-basicsPT.md
└── resumo/
    └── resumoxss-basics.md
```

---

## Comportamento esperado

Quando o usuário pedir algo como:

```text
processe xss-basics.md
```

ou:

```text
traduza e faça o resumo desse arquivo
```

execute diretamente o fluxo definido neste documento.

Não peça confirmação para criar `PT/` ou `resumo/`.

Não altere o arquivo original.

Ao terminar, informe de forma curta quais arquivos foram criados ou atualizados.
