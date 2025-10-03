# HTML - HyperText Markup Language

## O que é HTML?

**HTML** (HyperText Markup Language) é a linguagem de marcação padrão para criar páginas web. É a base fundamental de qualquer site, definindo a estrutura e o conteúdo das páginas através de elementos e tags.

## Para que serve?

- **Estruturação de conteúdo**: Organiza texto, imagens, links e outros elementos
- **Criação de páginas web**: Base para todos os sites da internet
- **Semântica**: Define o significado dos elementos (cabeçalhos, parágrafos, listas, etc.)
- **Acessibilidade**: Permite que tecnologias assistivas interpretem o conteúdo
- **SEO**: Ajuda motores de busca a entender e indexar o conteúdo

## Estrutura Básica

```html
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Título da Página</title>
</head>
<body>
    <h1>Conteúdo principal</h1>
</body>
</html>
```

## Principais Tags e Exemplos

### Cabeçalhos
```html
<h1>Título Principal</h1>
<h2>Subtítulo</h2>
<h3>Título Secundário</h3>
```

### Texto e Parágrafos
```html
<p>Este é um parágrafo de texto.</p>
<strong>Texto em negrito</strong>
<em>Texto em itálico</em>
<br> <!-- Quebra de linha -->
```

### Links e Imagens
```html
<a href="https://exemplo.com">Link para site</a>
<img src="imagem.jpg" alt="Descrição da imagem">
```

### Listas
```html
<!-- Lista não ordenada -->
<ul>
    <li>Item 1</li>
    <li>Item 2</li>
</ul>

<!-- Lista ordenada -->
<ol>
    <li>Primeiro item</li>
    <li>Segundo item</li>
</ol>
```

### Formulários
```html
<form action="/submit" method="POST">
    <label for="nome">Nome:</label>
    <input type="text" id="nome" name="nome" required>
    
    <label for="email">Email:</label>
    <input type="email" id="email" name="email" required>
    
    <button type="submit">Enviar</button>
</form>
```

### Tabelas
```html
<table>
    <thead>
        <tr>
            <th>Nome</th>
            <th>Idade</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>João</td>
            <td>25</td>
        </tr>
    </tbody>
</table>
```

### Divisões e Seções
```html
<div class="container">
    <header>Cabeçalho</header>
    <main>Conteúdo principal</main>
    <footer>Rodapé</footer>
</div>
```

### Elementos Multimídia
```html
<!-- Vídeo -->
<video controls width="400">
    <source src="video.mp4" type="video/mp4">
    Seu navegador não suporta vídeo.
</video>

<!-- Áudio -->
<audio controls>
    <source src="audio.mp3" type="audio/mpeg">
    Seu navegador não suporta áudio.
</audio>
```

### Elementos Semânticos HTML5
```html
<article>
    <header>
        <h2>Título do Artigo</h2>
        <time datetime="2025-10-02">2 de outubro de 2025</time>
    </header>
    <section>
        <p>Conteúdo do artigo...</p>
    </section>
    <aside>
        <p>Informação relacionada</p>
    </aside>
</article>

<nav>
    <ul>
        <li><a href="#home">Home</a></li>
        <li><a href="#sobre">Sobre</a></li>
        <li><a href="#contato">Contato</a></li>
    </ul>
</nav>
```

### Atributos Importantes
```html
<!-- Atributos de dados customizados -->
<div data-user-id="123" data-role="admin">Usuário</div>

<!-- Atributos de acessibilidade -->
<img src="logo.png" alt="Logo da empresa" role="img">
<button aria-label="Fechar modal" aria-expanded="false">×</button>

<!-- Atributos de formulário -->
<input type="password" 
       placeholder="Digite sua senha"
       pattern="^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$"
       title="Mínimo 8 caracteres, pelo menos uma letra e um número">
```

### Meta Tags Importantes
```html
<head>
    <!-- SEO -->
    <meta name="description" content="Descrição da página">
    <meta name="keywords" content="html, web, desenvolvimento">
    <meta name="author" content="Seu Nome">
    
    <!-- Open Graph (redes sociais) -->
    <meta property="og:title" content="Título da Página">
    <meta property="og:description" content="Descrição para redes sociais">
    <meta property="og:image" content="imagem-preview.jpg">
    
    <!-- Viewport para responsividade -->
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
```

### Tipos de Input Modernos
```html
<form>
    <input type="email" placeholder="email@exemplo.com">
    <input type="tel" placeholder="(11) 99999-9999">
    <input type="url" placeholder="https://exemplo.com">
    <input type="date" min="2025-01-01" max="2025-12-31">
    <input type="time" step="300">
    <input type="number" min="1" max="100" step="1">
    <input type="range" min="0" max="100" value="50">
    <input type="color" value="#ff0000">
    <input type="file" accept=".pdf,.doc,.docx" multiple>
</form>
```

### Canvas e SVG
```html
<!-- Canvas para gráficos dinâmicos -->
<canvas id="myCanvas" width="400" height="200">
    Seu navegador não suporta canvas.
</canvas>

<!-- SVG para gráficos vetoriais -->
<svg width="100" height="100">
    <circle cx="50" cy="50" r="40" fill="blue"/>
    <text x="50" y="55" text-anchor="middle" fill="white">SVG</text>
</svg>
```

### Elementos de Citação e Código
```html
<blockquote cite="https://exemplo.com">
    "Esta é uma citação importante."
</blockquote>

<p>Use <code>console.log()</code> para debug em JavaScript.</p>

<pre>
<code>
function exemplo() {
    return "Código formatado";
}
</code>
</pre>

<kbd>Ctrl</kbd> + <kbd>C</kbd> para copiar
```

## Hierarquia e Estrutura de Tags HTML

### Conceito de Hierarquia
HTML segue uma estrutura hierárquica em árvore, onde elementos são organizados em níveis pai-filho. Esta organização é fundamental para:
- **Semântica**: Define o significado e importância do conteúdo
- **Estilização CSS**: Permite seleção e herança de propriedades
- **Acessibilidade**: Ajuda tecnologias assistivas a navegar
- **SEO**: Motores de busca entendem a estrutura do conteúdo

### Estrutura Básica da Hierarquia
```
html (raiz)
├── head (metadados)
│   ├── meta
│   ├── title
│   └── link
└── body (conteúdo visível)
    ├── header
    ├── main
    │   ├── section
    │   │   ├── h2
    │   │   └── p
    │   └── article
    └── footer
```

### Hierarquia de Cabeçalhos (h1-h6)
```html
<h1>Título Principal da Página</h1>          <!-- Nível 1 - Único por página -->
  <h2>Seção Principal</h2>                   <!-- Nível 2 -->
    <h3>Subseção</h3>                        <!-- Nível 3 -->
      <h4>Sub-subseção</h4>                  <!-- Nível 4 -->
        <h5>Tópico Específico</h5>           <!-- Nível 5 -->
          <h6>Detalhe</h6>                   <!-- Nível 6 -->
```

**Regras importantes:**
- Sempre começar com `<h1>` (único por página)
- Não pular níveis (h1 → h3 ❌, h1 → h2 ✅)
- Usar hierarquia lógica, não por aparência visual

### Elementos de Bloco vs Inline

**Elementos de Bloco** (ocupam toda largura):
```html
<div>Container genérico</div>
<p>Parágrafo</p>
<header>Cabeçalho</header>
<section>Seção</section>
<ul><li>Lista</li></ul>
```

**Elementos Inline** (ocupam apenas o necessário):
```html
<span>Texto inline</span>
<a href="#">Link</a>
<strong>Negrito</strong>
<em>Itálico</em>
<code>Código</code>
```

### Aninhamento Correto
```html
<!-- ✅ Correto -->
<article>
    <header>
        <h2>Título do Artigo</h2>
        <p>Subtítulo ou descrição</p>
    </header>
    <section>
        <p>Primeiro parágrafo com <strong>texto importante</strong>.</p>
        <p>Segundo parágrafo com <a href="#">link</a>.</p>
    </section>
</article>

<!-- ❌ Incorreto -->
<p><div>Bloco dentro de inline</div></p>
<h2><h3>Cabeçalho dentro de cabeçalho</h3></h2>
```

### Regras de Aninhamento
- **Elementos inline** não podem conter elementos de bloco
- **Elementos de formulário** têm regras específicas de aninhamento
- **Links** (`<a>`) não podem conter outros links
- **Botões** (`<button>`) não podem conter elementos interativos

## Boas Práticas

### Estrutura e Semântica
- Use elementos semânticos apropriados (`<header>`, `<main>`, `<footer>`)
- Mantenha hierarquia correta de cabeçalhos (h1 → h6)
- Sempre inclua atributo `alt` em imagens
- Use `<label>` associado aos campos de formulário

### Acessibilidade
- Forneça texto alternativo para conteúdo não textual
- Use contraste adequado de cores
- Estruture o conteúdo de forma lógica
- Teste com leitores de tela

### Performance
- Otimize imagens (formato, tamanho, compressão)
- Use lazy loading: `<img loading="lazy">`
- Minifique HTML em produção
- Valide o código com ferramentas como W3C Validator

## Relevância para Segurança Web

### Vulnerabilidades Comuns
- **XSS (Cross-Site Scripting)**: Vulnerabilidade que permite a execução de scripts maliciosos no navegador de outros usuários através de entrada não sanitizada. Ocorre quando dados não confiáveis são inseridos em páginas web sem validação adequada
- **CSRF (Cross-Site Request Forgery)**: Requisições não autorizadas executadas em nome de um usuário autenticado
- **Clickjacking**: Sobreposição de elementos invisíveis para enganar usuários
- **HTML Injection**: Inserção de código HTML malicioso que pode alterar a estrutura da página

### Medidas de Proteção
- **Sanitização de entrada**: Filtrar dados de formulários
- **Content Security Policy (CSP)**: Controlar recursos carregados
- **HTTPS**: Criptografar comunicação
- **Validação no servidor**: Nunca confiar apenas na validação client-side

### Headers de Segurança
```html
<meta http-equiv="Content-Security-Policy" 
      content="default-src 'self'; script-src 'self'">
<meta http-equiv="X-Frame-Options" content="DENY">
<meta http-equiv="X-Content-Type-Options" content="nosniff">
```

HTML é fundamental para entender como aplicações web funcionam e onde vulnerabilidades podem surgir.