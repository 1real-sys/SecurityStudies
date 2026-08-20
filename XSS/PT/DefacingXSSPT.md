# Defacement

Agora que compreendemos os diferentes tipos de XSS e vários métodos para descobrir vulnerabilidades XSS em páginas web, podemos começar a aprender como explorar essas vulnerabilidades. Como mencionado anteriormente, o dano e o alcance de um ataque XSS dependem do tipo de XSS: Stored XSS é o mais crítico, enquanto DOM-based XSS é menos crítico.

Um dos ataques mais comuns realizados com vulnerabilidades Stored XSS é o defacement de sites. Desfigurar (*deface*) um site significa alterar sua aparência para qualquer pessoa que o visite. É muito comum grupos de hackers desfigurarem um site para afirmar que conseguiram invadi-lo, como ocorreu quando hackers desfiguraram o site do National Health Service (NHS) do Reino Unido em 2018. Esses ataques podem gerar grande repercussão na mídia e afetar significativamente os investimentos e o preço das ações de uma empresa, especialmente no caso de bancos e empresas de tecnologia.

Embora muitas outras vulnerabilidades possam ser usadas para alcançar o mesmo resultado, as vulnerabilidades Stored XSS estão entre as mais utilizadas para esse fim.

## Elementos de defacement

Podemos utilizar código JavaScript injetado por meio de XSS para fazer uma página web assumir qualquer aparência que desejarmos. Entretanto, o defacement de um site normalmente é usado para transmitir uma mensagem simples, como “nós invadimos você com sucesso”; portanto, criar uma página desfigurada visualmente bonita não é o objetivo principal.

Quatro elementos HTML são normalmente utilizados para alterar a aparência principal de uma página web:

| Elemento | Propriedade |
| --- | --- |
| Cor de fundo | `document.body.style.background` |
| Imagem de fundo | `document.body.background` |
| Título da página | `document.title` |
| Texto da página | `DOM.innerHTML` |

Podemos utilizar dois ou três desses elementos para escrever uma mensagem básica na página web e até remover o elemento vulnerável, tornando mais difícil restaurar rapidamente a página, como veremos a seguir.

## Alterando o fundo

Vamos voltar ao exercício de Stored XSS e usá-lo como base para nosso ataque. Você pode retornar à seção de Stored XSS, iniciar o servidor e seguir os próximos passos.

Para alterar o fundo de uma página web, podemos escolher determinada cor ou usar uma imagem. Usaremos uma cor como fundo, pois a maioria dos ataques de defacement utiliza uma cor escura. Para isso, podemos usar o seguinte payload:

```html
<script>document.body.style.background = "#141d2b"</script>
```

> **Dica:** aqui definimos a cor de fundo como a cor padrão do Hack The Box. Podemos usar qualquer outro valor hexadecimal ou uma cor nomeada, como `= "black"`.

Depois que adicionarmos nosso payload à lista de tarefas (To-Do List), veremos que a cor de fundo foi alterada:

<a href="../img/xss12.png">
  <img src="../img/xss12.png" alt="Stored XSS alterando a cor de fundo da página web">
</a>

Essa alteração persistirá após atualizações da página e aparecerá para qualquer pessoa que a visitar, pois estamos utilizando uma vulnerabilidade Stored XSS.

Outra opção seria definir uma imagem como fundo usando o seguinte payload:

```html
<script>document.body.background = "https://www.hackthebox.eu/images/logo-htb.svg"</script>
```

Experimente o payload acima para observar como o resultado final poderá ficar.

## Alterando o título da página

Podemos alterar o título da página de `2Do` para qualquer título que escolhermos usando a propriedade JavaScript `document.title`:

```html
<script>document.title = 'HackTheBox Academy'</script>
```

Podemos ver na janela ou aba da página que o novo título substituiu o anterior:

<a href="../img/xss13.png">
  <img src="../img/xss13.png" alt="Aba do navegador mostrando o título da página alterado por meio de XSS">
</a>

## Alterando o texto da página

Quando queremos alterar o texto exibido na página web, podemos utilizar várias funções JavaScript. Por exemplo, podemos alterar o texto de um elemento HTML/DOM específico usando a propriedade `innerHTML`:

```javascript
document.getElementById("todo").innerHTML = "New Text"
```

Também podemos utilizar funções jQuery para alcançar o mesmo resultado com mais eficiência ou para alterar o texto de vários elementos em uma única linha. Para isso, a biblioteca jQuery deve ter sido importada no código-fonte da página:

```javascript
$("#todo").html('New Text');
```

Isso nos oferece várias opções para personalizar o texto da página web e fazer pequenos ajustes conforme nossas necessidades. Entretanto, como grupos de hackers normalmente deixam uma mensagem simples na página e removem todo o restante, alteraremos todo o código HTML do corpo principal usando `innerHTML`, da seguinte forma:

```javascript
document.getElementsByTagName('body')[0].innerHTML = "New Text"
```

Como podemos ver, podemos especificar o elemento `body` com `document.getElementsByTagName('body')` e, ao indicar `[0]`, selecionar o primeiro elemento `body`, o que deverá alterar todo o texto da página web. Também podemos usar jQuery para obter o mesmo resultado. Entretanto, antes de enviar nosso payload e realizar uma alteração permanente, devemos preparar o código HTML separadamente e depois usar `innerHTML` para inseri-lo no código-fonte da página.

Para nosso exercício, utilizaremos o código HTML da página principal do Hack The Box Academy:

```html
<center>
    <h1 style="color: white">Cyber Security Training</h1>
    <p style="color: white">by 
        <img src="https://academy.hackthebox.com/images/logo-htb.svg" height="25px" alt="HTB Academy">
    </p>
</center>
```

> **Dica:** é recomendável executar localmente nosso código HTML para verificar sua aparência e garantir que ele funcione conforme o esperado antes de incluí-lo no payload final.

Minificaremos o código HTML em uma única linha e o adicionaremos ao payload XSS anterior. O payload final deverá ser o seguinte:

```html
<script>document.getElementsByTagName('body')[0].innerHTML = '<center><h1 style="color: white">Cyber Security Training</h1><p style="color: white">by <img src="https://academy.hackthebox.com/images/logo-htb.svg" height="25px" alt="HTB Academy"> </p></center>'</script>
```

Depois que adicionarmos nosso payload à To-Do List vulnerável, veremos que o código HTML passa a fazer parte permanentemente do código-fonte da página web e exibe nossa mensagem para qualquer pessoa que a visite:

<a href="../img/xss14.png">
  <img src="../img/xss14.png" alt="Página desfigurada exibindo a mensagem injetada do Hack The Box Academy">
</a>

Usando três payloads XSS, conseguimos desfigurar com sucesso a página web alvo. Se examinarmos o código-fonte da página, veremos que o código original ainda existe e que os payloads injetados aparecem no final:

```html
<div></div><ul class="list-unstyled" id="todo"><ul>
<script>document.body.style.background = "#141d2b"</script>
</ul><ul><script>document.title = 'HackTheBox Academy'</script>
</ul><ul><script>document.getElementsByTagName('body')[0].innerHTML = '...SNIP...'</script>
</ul></ul>
```

Isso acontece porque o código JavaScript injetado altera a aparência da página quando é executado, o que, neste caso, ocorre no final do código-fonte. Se a injeção estivesse em um elemento no meio do código-fonte, outros scripts ou elementos poderiam ser adicionados depois dela, e teríamos que considerá-los para obter a aparência final desejada.

Entretanto, para os usuários comuns, a página parece desfigurada e exibe nossa nova aparência.
