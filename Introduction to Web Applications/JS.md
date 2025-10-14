# JavaScript - JS

JavaScript é uma linguagem de programação interpretada e dinâmica, essencial para desenvolvimento web. Responsável pela interatividade em páginas web, executa no navegador (client-side) e também no servidor com Node.js.

## O que é JavaScript

Criado em 1995, JavaScript é a linguagem padrão para web:
- **Interpretada**: Execução direta sem compilação
- **Dinamicamente tipada**: Tipos definidos em runtime
- **Event-driven**: Baseada em eventos
- **Multi-paradigma**: Funcional e orientada a objetos

## Sintaxe Básica

### **Variáveis e Tipos**
```javascript
let nome = "João";              // String
let idade = 30;                 // Number
let ativo = true;               // Boolean
const PI = 3.14;                // Constante

let frutas = ["maçã", "banana"];
let pessoa = { nome: "Ana", idade: 25 };
```

### **Operadores e Estruturas**
```javascript
// Comparação
5 === "5"       // false (estrito)
5 == "5"        // true (coerção)

// Condicional
if (idade >= 18) {
    console.log("Maior de idade");
}

// Loop
for (let i = 0; i < 5; i++) {
    console.log(i);
}
```

## Funções

```javascript
// Tradicional
function saudacao(nome) {
    return "Olá, " + nome;
}

// Arrow function
const multiplicar = (a, b) => a * b;

// Parâmetro padrão
function cumprimentar(nome = "Visitante") {
    return `Bem-vindo, ${nome}!`;
}
```

## Objetos e Arrays

```javascript
// Objeto
let carro = {
    marca: "Toyota",
    ligar: function() { return "Ligado!"; }
};
console.log(carro.marca);

// Arrays - métodos úteis
let numeros = [1, 2, 3, 4, 5];
numeros.push(6);                           // Adiciona
let pares = numeros.filter(n => n % 2 === 0);
let dobrados = numeros.map(n => n * 2);
let soma = numeros.reduce((acc, n) => acc + n, 0);
```

## DOM Manipulation

```javascript
// Seleção
const elemento = document.getElementById('meuId');
const classe = document.querySelector('.minha-classe');

// Manipulação
elemento.textContent = "Novo texto";
elemento.innerHTML = "<strong>Negrito</strong>";
elemento.classList.add('ativa');

// Eventos
button.addEventListener('click', () => {
    console.log('Clicado!');
});

input.addEventListener('input', (e) => {
    console.log('Valor:', e.target.value);
});
```

## Programação Assíncrona

```javascript
// Promise
function buscarDados() {
    return new Promise((resolve, reject) => {
        setTimeout(() => resolve("Dados"), 1000);
    });
}

// Async/Await
async function obterDados() {
    try {
        const dados = await buscarDados();
        console.log(dados);
    } catch (error) {
        console.error("Erro:", error);
    }
}

// Fetch API
async function buscarUsuarios() {
    const response = await fetch('/api/usuarios');
    return await response.json();
}

// POST
async function criarUsuario(dados) {
    const response = await fetch('/api/usuarios', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(dados)
    });
    return response.json();
}
```

## Recursos Modernos (ES6+)

```javascript
// Template literals
const mensagem = `Olá, ${nome}! Você tem ${idade} anos.`;

// Destructuring
const [a, b] = [1, 2];
const {nome, idade} = pessoa;

// Spread operator
const todos = [...numeros1, ...numeros2];
const novoObj = {...pessoa, cidade: "SP"};
```

## Tratamento de Erros

```javascript
try {
    let resultado = funcaoPerigosa();
} catch (error) {
    console.error("Erro:", error.message);
} finally {
    console.log("Sempre executa");
}

// Throw personalizado
function dividir(a, b) {
    if (b === 0) throw new Error("Divisão por zero!");
    return a / b;
}
```

## Conceitos Importantes

### **Closures**
```javascript
function contador() {
    let count = 0;
    return function() {
        return ++count;
    };
}

const c = contador();
console.log(c()); // 1
console.log(c()); // 2
```

### **Hoisting**
```javascript
console.log(x); // undefined (var é içado)
var x = 5;

console.log(y); // ReferenceError (let não é içado)
let y = 10;
```

## Frameworks e Ferramentas

### **Principais Frameworks**
- **React**: Biblioteca UI (Facebook)
- **Vue.js**: Framework progressivo
- **Angular**: Framework completo (Google)

### **Ferramentas Essenciais**
- **Node.js**: JavaScript no servidor
- **npm**: Gerenciador de pacotes
- **VS Code**: Editor recomendado

## Boas Práticas

1. Use `const` por padrão, `let` quando necessário
2. Evite `var` (escopo confuso)
3. Use nomes descritivos
4. Sempre trate erros
5. Use async/await
6. Valide dados de entrada
7. Use template literals
8. Mantenha funções pequenas

## Conclusão

JavaScript é fundamental para web moderna. Dominar variáveis, funções, DOM, eventos e programação assíncrona é essencial para criar aplicações web interativas e dinâmicas.