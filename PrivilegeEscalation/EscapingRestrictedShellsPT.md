# Escapando de Shells Restritos

Um shell restrito é um tipo de shell que limita a capacidade do usuário de executar comandos. Em um shell restrito, o usuário só pode executar um conjunto específico de comandos ou apenas comandos em diretórios específicos. Shells restritos são usados com frequência para fornecer um ambiente seguro para usuários que possam, de forma acidental ou intencional, danificar o sistema, ou para permitir acesso apenas a recursos específicos. Exemplos comuns incluem o `rbash` no Linux e o "Restricted-access Shell" no Windows.

## RBASH

Restricted Bourne shell (`rbash`) é uma versão restrita do Bourne shell, um interpretador de linha de comando padrão no Linux. Ele limita recursos como troca de diretórios, definição/modificação de variáveis de ambiente e execução de comandos em outros diretórios. É frequentemente usado para oferecer um ambiente seguro e controlado.

## RKSH

Restricted Korn shell (`rksh`) é uma versão restrita do Korn shell. O `rksh` limita recursos como execução de comandos em outros diretórios, criação/modificação de funções de shell e modificação do ambiente do shell.

## RZSH

Restricted Z shell (`rzsh`) é uma versão restrita do Z shell, um interpretador bastante flexível e poderoso. O `rzsh` limita ações como executar scripts, definir aliases e modificar o ambiente do shell.

Por exemplo, administradores costumam usar shells restritos em redes corporativas para fornecer um ambiente seguro e controlado para usuários que possam danificar o sistema. Ao limitar a execução de certos comandos ou o acesso a determinados diretórios, os administradores garantem que os usuários não realizem ações que possam prejudicar o sistema ou comprometer a segurança da rede. Além disso, shells restritos permitem conceder acesso apenas a recursos específicos, controlando quais funções ficam disponíveis para cada usuário.

Imagine uma empresa com uma rede de servidores Linux hospedando aplicações e serviços críticos. Muitos usuários — funcionários, contratados e parceiros externos — acessam a rede. Para proteger a segurança e a integridade do ambiente, o time de TI decide implementar shells restritos para todos.

Para isso, o time configura vários shells `rbash`, `rksh` e `rzsh` e atribui cada usuário a um shell específico. Parceiros externos, que precisam acessar apenas recursos como e-mail e compartilhamento de arquivos, recebem `rbash`. Contratados, que precisam de recursos mais avançados, como servidores web e banco de dados, recebem `rksh`, com mais flexibilidade, mas ainda com limitações. Funcionários, que precisam executar aplicações ou scripts específicos, recebem `rzsh`, com maior flexibilidade, porém ainda com restrições.

Existem vários métodos para escapar de um shell restrito. Alguns exploram vulnerabilidades no próprio shell; outros usam técnicas criativas para contornar as limitações. Abaixo estão alguns exemplos.

## Escaping

Em alguns casos, é possível escapar de um shell restrito injetando comandos na linha de comando ou em outras entradas aceitas pelo shell. Por exemplo, se o shell permite executar comandos passando argumentos para um comando interno, pode ser possível injetar comandos adicionais nesse argumento.

## Injeção de comandos

Imagine que estamos em um shell restrito que permite executar comandos passando argumentos ao comando `ls`. Esse shell permite apenas alguns argumentos específicos (`ls -l`, `ls -a` etc.), mas bloqueia outros comandos. Nesse cenário, podemos usar injeção para escapar do shell adicionando comandos ao argumento de `ls`.

Por exemplo, podemos usar o comando abaixo para injetar `pwd` como parte do argumento de `ls`:

```bash
JLMreal@htb[/htb]$ ls -l `pwd`
```

Esse comando faz com que `ls` seja executado com `-l`, seguido da saída de `pwd`. Como `pwd` não está restrito nesse caso, conseguimos executar `pwd` e ver o diretório atual mesmo que o shell não permita chamar `pwd` diretamente.

## Substituição de comando

Outro método para escapar de shell restrito é usar substituição de comando. Isso envolve a sintaxe de substituição do shell para executar um comando. Por exemplo, se o shell permite comandos entre crases (`` ` ``), pode ser possível escapar executando, nessa substituição, um comando que não esteja bloqueado.

## Encadeamento de comandos

Em alguns casos, também é possível escapar com encadeamento de comandos. Isso consiste em usar múltiplos comandos na mesma linha, separados por metacaracteres do shell, como ponto e vírgula (`;`) ou pipe (`|`). Se o shell permitir comandos separados por `;`, pode ser possível executar dois comandos, sendo que um deles não está restrito.

## Variáveis de ambiente

Outra forma envolve modificar ou criar variáveis de ambiente usadas pelo shell para executar comandos não restritos. Por exemplo, se o shell usa uma variável para definir o diretório de execução, alterar esse valor pode permitir escapar das restrições.

## Funções de shell

Em alguns casos, é possível escapar usando funções de shell. Podemos definir e chamar funções que executem comandos não restritos. Se o shell permitir definição e chamada de funções, pode ser possível criar uma função que execute um comando liberado.

