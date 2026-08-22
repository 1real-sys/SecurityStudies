# Ofuscação de código

Antes de começarmos a aprender sobre desofuscação, devemos primeiro aprender sobre ofuscação de código. Sem compreender como o código é ofuscado, talvez não consigamos desofuscá-lo com sucesso, especialmente se ele tiver sido ofuscado com um ofuscador personalizado.

## O que é ofuscação

Ofuscação é uma técnica usada para tornar um script mais difícil de ser lido por humanos, mas que permite que ele continue funcionando da mesma forma do ponto de vista técnico, embora seu desempenho possa ser mais lento. Isso geralmente é feito automaticamente por meio de uma ferramenta de ofuscação, que recebe o código como entrada e tenta reescrevê-lo de uma maneira muito mais difícil de ler, dependendo de seu projeto.

Por exemplo, ofuscadores de código frequentemente transformam o código em um dicionário contendo todas as palavras e símbolos utilizados e, durante a execução, tentam reconstruir o código original referenciando cada palavra e símbolo desse dicionário. A imagem a seguir mostra um exemplo de um código JavaScript simples sendo ofuscado:

<a href="../IMG/JSOBS1.png">
  <img src="../IMG/JSOBS1.png" alt="Exemplo de código JavaScript simples antes e depois da ofuscação">
</a>

Códigos escritos em muitas linguagens interpretadas, como Python, PHP e JavaScript, são publicados e executados sem serem compilados. Enquanto Python e PHP normalmente residem no lado do servidor e, portanto, ficam ocultos dos usuários finais, JavaScript geralmente é utilizado nos navegadores, no lado do cliente, e o código é enviado ao usuário e executado em texto claro. É por isso que a ofuscação é utilizada com muita frequência em JavaScript.

## Casos de uso

Existem muitas razões pelas quais desenvolvedores podem considerar ofuscar seu código. Uma razão comum é ocultar o código original e suas funções para impedir que ele seja reutilizado ou copiado sem a permissão do desenvolvedor, tornando mais difícil realizar engenharia reversa de sua funcionalidade original. Outra razão é fornecer uma camada de segurança ao lidar com autenticação ou criptografia, buscando impedir ataques contra vulnerabilidades que possam ser encontradas no código.

É importante observar que realizar autenticação ou criptografia no lado do cliente não é recomendado, pois dessa forma o código fica mais sujeito a ataques.

Entretanto, o uso mais comum da ofuscação é em ações maliciosas. É comum que atacantes e agentes maliciosos ofusquem seus scripts para impedir que sistemas de detecção e prevenção de intrusões (Intrusion Detection and Prevention Systems) os detectem. Na próxima seção, aprenderemos a ofuscar um código JavaScript simples e tentaremos executá-lo antes e depois da ofuscação para observar possíveis diferenças.
