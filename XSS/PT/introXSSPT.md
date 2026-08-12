# Introdução

À medida que as aplicações web se tornam mais avançadas e mais comuns, o mesmo ocorre com as vulnerabilidades em aplicações web. Entre os tipos mais comuns estão as vulnerabilidades de Cross-Site Scripting (XSS). As vulnerabilidades XSS exploram uma falha na sanitização da entrada do usuário para "escrever" código JavaScript na página e executá-lo no lado do cliente, possibilitando diversos tipos de ataque.

## O que é XSS

Uma aplicação web típica funciona recebendo o código HTML do servidor de back-end e renderizando-o no navegador de internet do lado do cliente. Quando uma aplicação web vulnerável não sanitiza corretamente a entrada do usuário, um usuário mal-intencionado pode injetar código JavaScript adicional em um campo de entrada (por exemplo, comentário/resposta). Assim, quando outro usuário visualiza a mesma página, ele executa o código JavaScript malicioso sem perceber.

As vulnerabilidades XSS são executadas exclusivamente no lado do cliente e, portanto, não afetam diretamente o servidor de back-end. Elas só podem afetar o usuário que executa a vulnerabilidade. O impacto direto das vulnerabilidades XSS sobre o servidor de back-end pode ser relativamente baixo, mas elas são encontradas com muita frequência em aplicações web. Isso resulta em um risco médio (baixo impacto + alta probabilidade = risco médio), o qual devemos sempre tentar reduzir detectando, corrigindo e prevenindo proativamente esses tipos de vulnerabilidade.

Matriz de risco com os eixos: Probabilidade (de baixa a alta) e Impacto (de baixo a alto), mostrando as estratégias: Reduzir, Evitar, Aceitar e Transferir.

<a href="../xss1.png">
  <img src="../xss1.png" alt="Matriz de risco com os eixos Probabilidade e Impacto e as estratégias Reduzir, Evitar, Aceitar e Transferir">
</a>

## Ataques XSS

As vulnerabilidades XSS podem viabilizar uma ampla variedade de ataques, abrangendo qualquer ação que possa ser executada por meio de código JavaScript no navegador. Um exemplo básico de ataque XSS consiste em fazer com que o usuário-alvo envie, sem perceber, seu cookie de sessão para o servidor web do atacante. Outro exemplo é fazer o navegador do alvo executar chamadas de API que levem a uma ação maliciosa, como alterar a senha do usuário para uma senha escolhida pelo atacante. Existem muitos outros tipos de ataque XSS, desde mineração de Bitcoin até a exibição de anúncios.

Como os ataques XSS executam código JavaScript dentro do navegador, eles ficam limitados ao motor JavaScript do navegador (por exemplo, o V8 no Chrome). Eles não podem executar código JavaScript em todo o sistema para realizar algo como execução de código em nível de sistema. Nos navegadores modernos, também ficam limitados ao mesmo domínio do site vulnerável. Ainda assim, a capacidade de executar JavaScript no navegador de um usuário pode possibilitar uma grande variedade de ataques, como mencionado anteriormente. Além disso, se um pesquisador qualificado identificar uma vulnerabilidade binária em um navegador web (por exemplo, um heap overflow no Chrome), ele poderá utilizar uma vulnerabilidade XSS para executar um exploit JavaScript no navegador do alvo, o qual, por fim, escapa da sandbox do navegador e executa código na máquina do usuário.

Vulnerabilidades XSS podem ser encontradas em quase todas as aplicações web modernas e têm sido exploradas ativamente nas últimas duas décadas. Um exemplo conhecido de XSS é o Samy Worm, um worm baseado em navegador que explorou uma vulnerabilidade de XSS armazenado no site de rede social MySpace, em 2005. Ele era executado ao visualizar uma página web infectada e publicava uma mensagem na página do MySpace da vítima com o texto: "Samy is my hero." A própria mensagem também continha o mesmo payload JavaScript para republicá-la quando fosse visualizada por outras pessoas. Em um único dia, mais de um milhão de usuários do MySpace tiveram essa mensagem publicada em suas páginas. Embora esse payload específico não tenha causado danos reais, a vulnerabilidade poderia ter sido utilizada para fins muito mais maliciosos, como roubar informações de cartão de crédito dos usuários, instalar keyloggers em seus navegadores ou até mesmo explorar uma vulnerabilidade binária nos navegadores web dos usuários (algo que era mais comum nos navegadores daquela época).

Em 2014, um pesquisador de segurança identificou acidentalmente uma vulnerabilidade XSS no painel TweetDeck do Twitter. Essa vulnerabilidade foi explorada para criar um tweet que retuitava a si próprio no Twitter, o que fez com que ele fosse retuitado mais de 38 mil vezes em menos de dois minutos. Por fim, isso obrigou o Twitter a desativar temporariamente o TweetDeck enquanto corrigia a vulnerabilidade.

Até hoje, mesmo as aplicações web de maior destaque apresentam vulnerabilidades XSS que podem ser exploradas. Até mesmo a página do mecanismo de busca do Google teve várias vulnerabilidades XSS em sua barra de pesquisa, sendo que a mais recente ocorreu em 2019, quando uma vulnerabilidade XSS foi encontrada na biblioteca XML. Além disso, o Apache Server, o servidor web mais utilizado na internet, certa vez relatou uma vulnerabilidade XSS que estava sendo explorada ativamente para roubar senhas de usuários de determinadas empresas. Tudo isso demonstra que as vulnerabilidades XSS devem ser levadas a sério e que uma quantidade significativa de esforço deve ser dedicada à sua detecção e prevenção.

## Tipos de XSS

Existem três tipos principais de vulnerabilidades XSS:

| Tipo | Descrição |
| --- | --- |
| XSS armazenado (persistente) | O tipo mais crítico de XSS, que ocorre quando a entrada do usuário é armazenada no banco de dados do back-end e depois exibida ao ser recuperada (por exemplo, publicações ou comentários). |
| XSS refletido (não persistente) | Ocorre quando a entrada do usuário é exibida na página após ser processada pelo servidor de back-end, mas sem ser armazenada (por exemplo, resultado de pesquisa ou mensagem de erro). |
| XSS baseado em DOM | Outro tipo de XSS não persistente, que ocorre quando a entrada do usuário é exibida diretamente no navegador e processada inteiramente no lado do cliente, sem chegar ao servidor de back-end (por exemplo, por meio de parâmetros HTTP processados no lado do cliente ou fragmentos de URL/âncoras). |

Abordaremos cada um desses tipos nas próximas seções e realizaremos exercícios para observar como cada um deles ocorre. Depois, também veremos como eles podem ser utilizados em ataques.
