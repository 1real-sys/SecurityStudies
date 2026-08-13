# XSS refletido (Reflected XSS)

Existem dois tipos de vulnerabilidade XSS não persistente (Non-Persistent XSS): o Reflected XSS, que é processado pelo servidor de back-end, e o DOM-based XSS, que é processado inteiramente no lado do cliente e nunca chega ao servidor de back-end. Diferentemente do Persistent XSS, as vulnerabilidades Non-Persistent XSS são temporárias e não persistem após atualizações da página. Portanto, nossos ataques afetam somente o usuário-alvo e não afetam outros usuários que visitarem a página.

As vulnerabilidades Reflected XSS ocorrem quando nossa entrada chega ao servidor de back-end e é devolvida sem filtragem ou sanitização. Existem muitas situações em que toda a entrada pode ser retornada, como em mensagens de erro ou de confirmação. Nesses casos, podemos tentar usar payloads XSS para verificar se eles são executados. Entretanto, como normalmente são mensagens temporárias, depois que saímos da página elas não voltam a ser executadas e, portanto, são não persistentes.

Podemos iniciar o servidor abaixo para praticar em uma página web vulnerável a Reflected XSS. Trata-se de uma aplicação de lista de tarefas (To-Do List) semelhante àquela em que praticamos na seção anterior. Podemos tentar adicionar qualquer string de teste para observar como ela é processada:

<a href="../xss4.png">
  <img src="../xss4.png" alt="Aplicação de lista de tarefas usada para praticar Reflected XSS">
</a>

Como podemos ver, recebemos a mensagem `Task 'test' could not be added.`, que inclui nossa entrada `test` como parte da mensagem de erro. Se nossa entrada não tiver sido filtrada ou sanitizada, a página poderá estar vulnerável a XSS. Podemos experimentar o mesmo payload XSS usado na seção anterior e clicar em **Add**:

<a href="../xss5.png">
  <img src="../xss5.png" alt="Payload de Reflected XSS inserido na aplicação de lista de tarefas">
</a>

Assim que clicamos em **Add**, a caixa de alerta é exibida:

<a href="../xss6.png">
  <img src="../xss6.png" alt="Caixa de alerta mostrando a execução bem-sucedida do payload de Reflected XSS">
</a>

Nesse caso, vemos que a mensagem de erro agora diz `Task '' could not be added.`. Como nosso payload está envolvido por uma tag `<script>`, ele não é renderizado visualmente pelo navegador, então vemos apenas as aspas simples vazias `''`. Podemos novamente visualizar o código-fonte da página para confirmar que a mensagem de erro contém nosso payload XSS:

```html
<div></div><ul class="list-unstyled" id="todo"><div style="padding-left:25px">Task '<script>alert(window.origin)</script>' could not be added.</div></ul>
```

Como podemos ver, as aspas simples realmente contêm nosso payload XSS: `'<script>alert(window.origin)</script>'`.

Se visitarmos novamente a página Reflected, a mensagem de erro não aparecerá mais e nosso payload XSS não será executado, o que significa que essa vulnerabilidade XSS é realmente não persistente.

Mas, se a vulnerabilidade XSS não é persistente, como poderíamos atingir vítimas com ela?

Isso depende de qual requisição HTTP é usada para enviar nossa entrada ao servidor. Podemos verificar essa informação nas ferramentas de desenvolvedor do Firefox, pressionando `CTRL+Shift+I` e selecionando a aba **Network**. Em seguida, podemos inserir novamente nosso payload de teste e clicar em **Add** para enviá-lo:

```text
http://SERVER_IP:PORT/
```

A aba Network mostra as requisições HTTP: status 200 para `localhost index.php`, `bootstrap.min.js` e `jquery.min.js`; e status 404 para `localhost favicon.ico`.

Como podemos ver, a primeira linha mostra que nossa requisição foi do tipo GET. Requisições GET enviam seus parâmetros e dados como parte da URL. Portanto, para atingir um usuário, podemos enviar a ele uma URL que contenha nosso payload. Para obter essa URL, podemos copiá-la da barra de endereços do Firefox depois de enviar o payload XSS ou clicar com o botão direito sobre a requisição GET na aba Network e selecionar **Copy > Copy URL**. Assim que a vítima visitar essa URL, o payload XSS será executado:

<a href="../xss7.png">
  <img src="../xss7.png" alt="URL contendo o payload de Reflected XSS enviado por meio de uma requisição GET">
</a>
