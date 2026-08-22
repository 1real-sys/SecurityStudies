# Localizando código-fonte no navegador

## Visão geral

Aplicações web normalmente combinam três tecnologias principais:

| Tecnologia | Função predominante |
| --- | --- |
| HTML | Define a estrutura e o conteúdo da página. |
| CSS | Controla apresentação, cores, dimensões e layout. |
| JavaScript | Implementa comportamento, lógica e interação. |

Como HTML, CSS e JavaScript do front-end precisam ser entregues ao navegador, eles podem ser inspecionados pelo usuário. Isso não inclui necessariamente o código do back-end, que é executado no servidor e normalmente envia apenas o resultado ao cliente.

## Ponto de partida do laboratório

A página do exercício é acessada em:

```text
http://SERVER_IP:PORT
```

Ela apresenta apenas o texto `Secret Serial Generator`, sem campos ou funcionalidades evidentes. Essa ausência de controles visíveis não significa que a página não possua lógica: ela pode estar implementada em scripts carregados separadamente.

## Visualizando o HTML original

O atalho `[CTRL + U]` abre uma representação do código-fonte recebido pelo navegador. O mesmo pode ser expresso com:

```text
view-source:http://SERVER_IP:PORT
```

O HTML pode revelar:

- comentários de desenvolvedores;
- caminhos de arquivos CSS e JavaScript;
- endpoints, formulários e parâmetros;
- elementos ocultos;
- metadados e referências a recursos externos.

Comentários não devem conter senhas, tokens, chaves ou detalhes internos. Mesmo quando não são renderizados visualmente, continuam disponíveis no documento enviado ao cliente.

## Código-fonte recebido versus DOM atual

É importante diferenciar:

- **View Source:** mostra o HTML originalmente retornado pelo servidor;
- **Inspector/Elements:** mostra o DOM atual, incluindo alterações feitas pelo JavaScript depois do carregamento.

Se um script criar, remover ou modificar elementos dinamicamente, essas mudanças poderão aparecer no Inspector, mas não necessariamente em `view-source:`.

## CSS interno e externo

CSS interno é colocado entre tags `<style>`:

```HTML
    <style>
        *,
        html {
            margin: 0;
            padding: 0;
            border: 0;
        }
        ...SNIP...
        h1 {
            font-size: 144px;
        }
        p {
            font-size: 64px;
        }
    </style>
```

CSS externo é referenciado por uma tag `<link>` no `head`:

```HTML
<head>
    <link rel="stylesheet" href="style.css">
</head>
```

O atributo `href` indica o caminho do recurso. Quando o valor é relativo, como `style.css`, o navegador o resolve em relação à URL do documento ou à URL base configurada.

## JavaScript interno e externo

JavaScript interno aparece entre tags `<script>`. Um arquivo externo é carregado pelo atributo `src`:

```HTML
<script src="secret.js"></script>
```

Nesse exemplo:

- `script` informa ao navegador que há código JavaScript;
- `src="secret.js"` aponta para o arquivo externo;
- clicar no caminho pela visualização do código-fonte permite abrir o recurso diretamente.

Também é possível localizar scripts nas abas **Sources** e **Network** das ferramentas de desenvolvedor.

## Primeiro sinal de ofuscação

O arquivo `secret.js` contém uma estrutura semelhante a:

```javascript
eval(function (p, a, c, k, e, d) { e = function (c) { '...SNIP... |true|function'.split('|'), 0, {}))
```

Esse padrão indica que o código original foi transformado em uma representação difícil de ler. A função externa reconstrói outra porção de código, e `eval()` pode executá-la.

Pontos importantes:

- `eval()` executa uma string como JavaScript;
- arrays ou strings separadas por `|` podem funcionar como tabelas de palavras;
- nomes de parâmetros curtos dificultam a compreensão;
- o comportamento real pode surgir somente após uma etapa de desempacotamento.

## Abordagem inicial de análise

1. Abra o HTML original com `CTRL + U`.
2. Liste os arquivos carregados por `src` e `href`.
3. Abra cada JavaScript relevante sem executá-lo novamente fora do contexto necessário.
4. Salve uma cópia para análise e preserve o original.
5. Formate o código para visualizar blocos e funções.
6. Procure strings, URLs, endpoints e funções potencialmente importantes.
7. Identifique construções dinâmicas como `eval()` e `Function()`.
8. Desempacote ou decodifique uma camada de cada vez em ambiente controlado.

## Cuidados de segurança

Não execute JavaScript desconhecido diretamente em um sistema de uso pessoal. Código ofuscado pode realizar requisições, acessar dados disponíveis no navegador ou carregar outros estágios.

Em laboratórios e análises autorizadas:

- trabalhe em ambiente isolado;
- observe o tráfego de rede;
- não use credenciais reais;
- prefira análise estática antes da execução;
- substitua ou intercepte funções perigosas quando estiver estudando a saída produzida.

## Pontos-chave para revisão

- O front-end é entregue ao navegador e pode ser inspecionado.
- HTML estrutura, CSS apresenta e JavaScript implementa comportamento.
- `CTRL + U` mostra a resposta original; o Inspector mostra o DOM atual.
- Tags `<link>` e `<script>` revelam recursos externos.
- Comentários no cliente nunca devem ser considerados privados.
- Código difícil de ler, tabelas de strings e `eval()` são indícios comuns de ofuscação.
