# Descoberta de XSS

A esta altura, já devemos ter uma boa compreensão do que é uma vulnerabilidade XSS, dos três tipos de XSS e de como cada tipo se diferencia dos demais. Também devemos entender como o XSS funciona por meio da injeção de código JavaScript no código-fonte da página no lado do cliente, executando assim código adicional, que mais adiante aprenderemos a utilizar a nosso favor.

Nesta seção, veremos várias formas de detectar vulnerabilidades XSS em uma aplicação web. No caso das vulnerabilidades de aplicações web — e das vulnerabilidades em geral —, detectá-las pode se tornar tão difícil quanto explorá-las. Entretanto, como as vulnerabilidades XSS são muito difundidas, existem muitas ferramentas que podem nos ajudar a detectá-las e identificá-las.

## Descoberta automatizada

Praticamente todos os scanners de vulnerabilidades em aplicações web, como Nessus, Burp Pro ou ZAP, possuem diversos recursos para detectar os três tipos de vulnerabilidade XSS. Esses scanners geralmente realizam dois tipos de varredura: uma **varredura passiva (Passive Scan)**, que examina o código do lado do cliente em busca de possíveis vulnerabilidades DOM-based, e uma **varredura ativa (Active Scan)**, que envia vários tipos de payload para tentar acionar um XSS por meio da injeção de payloads no código-fonte da página.

Embora as ferramentas pagas normalmente tenham um nível maior de precisão na detecção de vulnerabilidades XSS, especialmente quando é necessário contornar mecanismos de segurança, ainda podemos encontrar ferramentas open source que ajudam a identificar possíveis vulnerabilidades XSS. Essas ferramentas geralmente funcionam identificando campos de entrada nas páginas web, enviando vários tipos de payload XSS e comparando o código-fonte renderizado da página para verificar se o mesmo payload pode ser encontrado nele, o que pode indicar uma injeção XSS bem-sucedida. Ainda assim, isso nem sempre será preciso, pois, em alguns casos, mesmo que o payload tenha sido injetado, ele pode não ser executado com sucesso por diversas razões. Portanto, devemos sempre verificar manualmente a injeção XSS.

Algumas ferramentas open source comuns que podem auxiliar na descoberta de XSS são XSS Strike, Brute XSS e XSSer. Podemos experimentar o XSS Strike clonando-o para nossa VM com `git clone`:

```shellsession
JLMreal@htb[/htb]$ git clone https://github.com/s0md3v/XSStrike.git
JLMreal@htb[/htb]$ cd XSStrike
JLMreal@htb[/htb]$ pip install -r requirements.txt
JLMreal@htb[/htb]$ python xsstrike.py

XSStrike v3.1.4
...SNIP...
```

Em seguida, podemos executar o script e fornecer uma URL com um parâmetro usando `-u`. Vamos testá-lo com o exemplo de Reflected XSS da seção anterior:

```shellsession
JLMreal@htb[/htb]$ python xsstrike.py -u "http://SERVER_IP:PORT/index.php?task=test" 

        XSStrike v3.1.4

[~] Checking for DOM vulnerabilities 
[+] WAF Status: Offline 
[!] Testing parameter: task 
[!] Reflections found: 1 
[~] Analysing reflections 
[~] Generating payloads 
[!] Payloads generated: 3072 
------------------------------------------------------------
[+] Payload: <HtMl%09onPoIntERENTER+=+confirm()> 
[!] Efficiency: 100 
[!] Confidence: 10 
[?] Would you like to continue scanning? [y/N]
```

Como podemos ver, a ferramenta identificou o parâmetro como vulnerável a XSS já no primeiro payload. Tente verificar o payload acima testando-o em um dos exercícios anteriores. Você também pode experimentar as outras ferramentas e executá-las nos mesmos exercícios para observar a capacidade de cada uma na detecção de vulnerabilidades XSS.

## Descoberta manual

Quando se trata da descoberta manual de XSS, a dificuldade de encontrar a vulnerabilidade depende do nível de segurança da aplicação web. Vulnerabilidades XSS básicas normalmente podem ser encontradas testando vários payloads XSS, mas a identificação de vulnerabilidades XSS avançadas exige habilidades avançadas de revisão de código.

### Payloads XSS

O método mais básico para procurar vulnerabilidades XSS é testar manualmente vários payloads XSS em um campo de entrada de determinada página web. Podemos encontrar grandes listas de payloads XSS online, como as disponíveis no PayloadAllTheThings e no Payload-Box. Em seguida, podemos começar a testar esses payloads um a um, copiando cada um, inserindo-o em nosso formulário e verificando se uma caixa de alerta é exibida.

> **Observação:** XSS pode ser injetado em qualquer entrada da página HTML. Isso não se limita a campos de entrada HTML, pois a injeção também pode ocorrer em headers HTTP, como `Cookie` ou `User-Agent`, quando seus valores são exibidos na página.

Você perceberá que a maioria dos payloads mencionados acima não funciona em nossas aplicações web de exemplo, embora estejamos lidando com os tipos mais básicos de vulnerabilidade XSS. Isso acontece porque esses payloads foram escritos para uma ampla variedade de pontos de injeção, como uma injeção após uma aspa simples, ou foram projetados para contornar determinadas medidas de segurança, como filtros de sanitização. Além disso, esses payloads utilizam vários vetores de injeção para executar código JavaScript, como tags `<script>` básicas, outros atributos HTML, como `<img>`, ou até atributos CSS `style`. Por isso, podemos esperar que muitos desses payloads não funcionem em todos os casos de teste, pois foram projetados para tipos específicos de injeção.

Consequentemente, recorrer à cópia e colagem manual de payloads XSS não é muito eficiente. Mesmo que uma aplicação web esteja vulnerável, pode levar algum tempo para identificarmos a vulnerabilidade, especialmente quando há muitos campos de entrada a serem testados. Por isso, pode ser mais eficiente escrever nosso próprio script Python para automatizar o envio desses payloads e depois comparar o código-fonte da página para verificar como eles foram renderizados. Isso pode ajudar em casos avançados nos quais as ferramentas de XSS não conseguem enviar e comparar os payloads com facilidade. Dessa forma, teríamos a vantagem de personalizar nossa ferramenta para a aplicação web alvo. Contudo, essa é uma abordagem avançada para descoberta de XSS e não faz parte do escopo deste módulo.

## Revisão de código

O método mais confiável para detectar vulnerabilidades XSS é a revisão manual de código, que deve abranger tanto o código de back-end quanto o de front-end. Se compreendermos exatamente como nossa entrada é tratada durante todo o caminho até chegar ao navegador web, poderemos escrever um payload personalizado com alta probabilidade de funcionar.

Na seção anterior, vimos um exemplo básico de revisão de código HTML ao discutir Source e Sink em vulnerabilidades DOM-based XSS. Isso nos proporcionou uma visão rápida de como a revisão de código front-end funciona na identificação de vulnerabilidades XSS, embora tenha sido um exemplo bastante básico de front-end.

É pouco provável que encontremos vulnerabilidades XSS em aplicações web mais conhecidas apenas por meio de listas de payloads ou ferramentas de XSS. Isso acontece porque os desenvolvedores dessas aplicações provavelmente as submetem a ferramentas de avaliação de vulnerabilidades e corrigem as falhas identificadas antes do lançamento. Nesses casos, a revisão manual de código pode revelar vulnerabilidades XSS não detectadas que sobrevivam aos lançamentos públicos de aplicações web conhecidas. Essas também são técnicas avançadas e estão fora do escopo deste módulo. Ainda assim, se você tiver interesse em aprendê-las, os módulos **Secure Coding 101: JavaScript** e **Whitebox Pentesting 101: Command Injection** abordam esse assunto detalhadamente.
