# CSS - Cascading Style Sheets

CSS (Cascading Style Sheets) é uma linguagem de estilo utilizada para descrever a apresentação visual de documentos HTML. É responsável por definir cores, layouts, fontes, espaçamentos e toda a aparência visual de páginas web.

## O que é CSS

CSS separa o conteúdo (HTML) da apresentação visual, permitindo:
- **Reutilização**: Um arquivo CSS pode estilizar múltiplas páginas
- **Manutenção**: Alterações visuais centralizadas
- **Performance**: Redução de código repetitivo
- **Flexibilidade**: Diferentes estilos para diferentes dispositivos

## Estrutura Básica

### Sintaxe CSS
```css
seletor {
    propriedade: valor;
    outra-propriedade: outro-valor;
}
```

### Exemplo Prático
```css
h1 {
    color: blue;
    font-size: 24px;
    text-align: center;
}
```

## Principais Propriedades CSS

### **Texto e Fontes**
```css
.texto {
    font-family: Arial, sans-serif;
    font-size: 16px;
    font-weight: bold;
    color: #333;
    text-align: center;
    line-height: 1.5;
}
```

### **Box Model (Modelo de Caixa)**
```css
.caixa {
    width: 300px;
    height: 200px;
    padding: 20px;        /* Espaço interno */
    margin: 10px;         /* Espaço externo */
    border: 2px solid #000;
    background-color: #f0f0f0;
}
```

### **Layout e Posicionamento**
```css
.container {
    display: flex;
    position: relative;
    top: 10px;
    left: 20px;
    z-index: 1;
}
```

### **Cores e Backgrounds**
```css
.elemento {
    background-color: #3498db;
    background-image: url('imagem.jpg');
    background-size: cover;
    opacity: 0.8;
}
```

## Seletores CSS

### **Seletores Básicos**
```css
/* Por elemento */
p { color: red; }

/* Por classe */
.minha-classe { font-size: 18px; }

/* Por ID */
#meu-id { background: yellow; }

/* Por atributo */
input[type="text"] { border: 1px solid gray; }
```

### **Seletores Avançados**
```css
/* Descendente */
div p { margin: 10px; }

/* Filho direto */
ul > li { list-style: none; }

/* Pseudo-classes */
a:hover { color: blue; }
button:active { transform: scale(0.95); }

/* Pseudo-elementos */
p::first-letter { font-size: 2em; }
```

## Layouts Modernos

### **Flexbox**
```css
.flex-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
}

.flex-item {
    flex: 1;
    margin: 10px;
}
```

### **CSS Grid**
```css
.grid-container {
    display: grid;
    grid-template-columns: 1fr 2fr 1fr;
    grid-gap: 20px;
    grid-template-areas: 
        "header header header"
        "sidebar main main"
        "footer footer footer";
}
```

## Responsividade

### **Media Queries**
```css
/* Desktop */
.container { width: 1200px; }

/* Tablet */
@media (max-width: 768px) {
    .container { width: 100%; }
}

/* Mobile */
@media (max-width: 480px) {
    .container { 
        width: 100%;
        padding: 10px;
    }
}
```

## Animações e Transições

### **Transições**
```css
.botao {
    background-color: blue;
    transition: all 0.3s ease;
}

.botao:hover {
    background-color: red;
    transform: scale(1.1);
}
```

### **Animações**
```css
@keyframes slideIn {
    from { transform: translateX(-100%); }
    to { transform: translateX(0); }
}

.elemento {
    animation: slideIn 0.5s ease-in-out;
}
```

## Três Frameworks CSS Mais Populares

### **1. Bootstrap**
**O que é:** Framework CSS mais popular e amplamente usado no mundo.

**Características:**
- Grid system responsivo de 12 colunas
- Componentes pré-construídos (botões, cards, modals)
- Classes utilitárias extensivas
- JavaScript integrado para interatividade

**Por que é fácil:**
- Documentação excelente e abundante
- Comunidade gigantesca
- Muitos templates e exemplos gratuitos
- Compatibilidade com todos os browsers

**Uso típico:**
```html
<div class="container">
    <div class="row">
        <div class="col-md-6">Conteúdo</div>
        <div class="col-md-6">Conteúdo</div>
    </div>
</div>
```

### **2. Tailwind CSS**
**O que é:** Framework utility-first que fornece classes de baixo nível para construir designs customizados.

**Características:**
- Classes utilitárias para cada propriedade CSS
- Configuração altamente customizável
- Purge CSS automático (remove código não usado)
- Design system consistente

**Por que é fácil:**
- Não precisa escrever CSS personalizado
- Nomes de classes intuitivos
- Desenvolvimento mais rápido
- Fácil manutenção

**Uso típico:**
```html
<div class="bg-blue-500 text-white p-4 rounded-lg shadow-lg">
    <h1 class="text-2xl font-bold mb-2">Título</h1>
    <p class="text-gray-100">Conteúdo do card</p>
</div>
```

### **3. Bulma**
**O que é:** Framework CSS moderno baseado em Flexbox, sem JavaScript.

**Características:**
- 100% baseado em Flexbox
- Sintaxe simples e legível
- Sem JavaScript (apenas CSS)
- Componentes modulares

**Por que é fácil:**
- Sintaxe muito limpa e intuitiva
- Documentação clara com exemplos visuais
- Flexbox simplifica layouts complexos
- Sem dependências JavaScript

**Uso típico:**
```html
<div class="columns">
    <div class="column is-half">
        <div class="box">
            <h1 class="title">Título</h1>
            <p class="subtitle">Subtítulo</p>
        </div>
    </div>
</div>
```

## Boas Práticas CSS

### **Organização**
- Use metodologias como BEM (Block Element Modifier)
- Organize arquivos por componentes
- Mantenha especificidade baixa
- Use variáveis CSS para cores e medidas

### **Performance**
- Minimize e comprima arquivos CSS
- Use seletores eficientes
- Evite !important
- Otimize para Critical CSS

### **Manutenibilidade**
- Comente código complexo
- Use nomes de classes descritivos
- Mantenha consistência no código
- Utilize preprocessadores (Sass, Less) quando necessário

## Conclusão

CSS é fundamental para desenvolvimento web moderno, oferecendo controle total sobre a apresentação visual. Os frameworks como Bootstrap, Tailwind e Bulma aceleram o desenvolvimento fornecendo componentes e utilitários prontos, cada um com sua abordagem específica. A escolha entre eles depende das necessidades do projeto e preferências da equipe de desenvolvimento.