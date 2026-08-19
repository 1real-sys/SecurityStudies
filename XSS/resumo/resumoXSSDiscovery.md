# Descoberta de vulnerabilidades XSS

## Visão geral

Descobrir XSS exige mais do que inserir um payload genérico e observar se aparece um alerta. O processo envolve localizar entradas controláveis, entender onde e como elas são renderizadas e confirmar se o navegador realmente as interpreta como código.

Há três abordagens principais:

1. scanners automatizados;
2. testes manuais com payloads;
3. revisão de código front-end e back-end.

Nenhuma detecção automatizada deve ser considerada prova definitiva sem validação manual.

## Descoberta automatizada

Scanners de aplicações web, como Nessus, Burp Pro e ZAP, geralmente combinam:

- **Passive Scan:** analisa respostas e código do cliente sem enviar payloads invasivos, procurando padrões perigosos e possíveis fluxos de DOM XSS;
- **Active Scan:** envia entradas e payloads especialmente construídos para tentar provocar a vulnerabilidade.

Ferramentas automatizadas costumam identificar campos e parâmetros, injetar payloads e procurar reflexões no HTML ou no DOM. Encontrar a entrada refletida é um indício, mas não confirma execução: o valor pode estar codificado, inserido em um contexto não executável ou bloqueado por outra proteção.

### XSStrike

O material apresenta XSStrike como uma opção open source, ao lado de Brute XSS e XSSer.

Instalação e execução inicial:

```shellsession
JLMreal@htb[/htb]$ git clone https://github.com/s0md3v/XSStrike.git
JLMreal@htb[/htb]$ cd XSStrike
JLMreal@htb[/htb]$ pip install -r requirements.txt
JLMreal@htb[/htb]$ python xsstrike.py

XSStrike v3.1.4
...SNIP...
```

Teste do parâmetro `task` no laboratório de Reflected XSS:

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

Parâmetros importantes:

- `python xsstrike.py` → executa a ferramenta;
- `-u` → informa a URL completa que será testada;
- `task=test` → fornece ao scanner um parâmetro e um valor inicial para análise.

O payload encontrado deve ser reproduzido manualmente no laboratório. Métricas como *Efficiency* e *Confidence* são estimativas da ferramenta, não substitutos para a comprovação da execução.

## Descoberta manual

O procedimento inicial é inserir um marcador único em cada ponto de entrada e acompanhar seu comportamento:

1. envie um texto facilmente reconhecível;
2. procure-o na resposta HTTP e no DOM renderizado;
3. determine o contexto de saída;
4. escolha um payload compatível com esse contexto;
5. confirme a execução e a origem em que ela ocorre;
6. classifique a vulnerabilidade como Stored, Reflected ou DOM-based.

As entradas não se limitam aos campos de formulário. Também podem incluir:

- parâmetros de URL e corpo da requisição;
- fragmentos da URL usados por JavaScript;
- headers como `User-Agent`, `Referer` e `Cookie`;
- nomes de arquivo e metadados;
- dados recuperados de APIs ou WebSockets.

Um header só se torna relevante para XSS quando seu conteúdo é posteriormente exibido ou inserido em um contexto interpretável.

## Por que muitos payloads falham

Payloads de listas públicas, como PayloadAllTheThings e Payload-Box, foram criados para contextos diferentes. Um payload pode precisar:

- encerrar uma string delimitada por aspas simples ou duplas;
- escapar de um atributo HTML;
- funcionar dentro de um bloco JavaScript;
- explorar um Sink específico do DOM;
- sobreviver à codificação, sanitização ou a um WAF;
- usar uma tag ou um evento permitido pelo navegador.

Portanto, falhar ao executar alguns payloads não prova que a aplicação é segura. Da mesma forma, ver o payload refletido não prova que existe XSS.

## O contexto determina o payload

Considere estas saídas conceituais:

```html
<div>ENTRADA</div>
<input value="ENTRADA">
<script>const value = 'ENTRADA';</script>
```

Embora a mesma entrada apareça nas três linhas, cada posição possui regras distintas de parsing e exige codificação de saída e testes específicos. Antes de tentar executar JavaScript, é necessário compreender quais caracteres delimitam o contexto e como o navegador constrói o DOM.

## Automação personalizada

Quando scanners genéricos não compreendem o fluxo da aplicação, um script próprio pode:

- enumerar parâmetros e campos;
- enviar uma lista controlada de marcadores ou payloads;
- registrar status, tamanho e conteúdo das respostas;
- detectar reflexões e transformações;
- comparar respostas e priorizar casos para análise manual.

Uma reflexão automatizada deve ser tratada como candidata. A confirmação ainda requer entender o contexto e verificar a execução real no navegador.

## Revisão de código

A revisão manual é o método mais confiável quando o código está disponível. O objetivo é rastrear dados não confiáveis desde a entrada até a saída.

No front-end, procure:

- Sources como `location.search`, `location.hash`, `document.URL` e campos de formulário;
- Sinks como `innerHTML`, `outerHTML`, `document.write()` e funções que avaliam código;
- transformações que parecem sanitização, mas apenas decodificam ou alteram strings.

No back-end, examine:

- onde dados da requisição são lidos;
- validação, normalização e armazenamento;
- templates e mecanismos de escape automático;
- pontos em que o escape é desativado;
- diferenças entre os contextos HTML, atributo, URL, CSS e JavaScript.

Com o caminho completo da entrada conhecido, é possível construir um teste específico com muito mais precisão que uma lista genérica.

## Falsos positivos e falsos negativos

- **Falso positivo:** o scanner encontra uma reflexão, mas o navegador a trata apenas como texto.
- **Falso negativo:** a ferramenta não identifica uma vulnerabilidade dependente de estado, autenticação, interação, transformação complexa ou execução no DOM.

Aplicações maduras frequentemente já foram testadas por scanners comuns. Vulnerabilidades restantes podem depender de fluxos de dados e contextos que somente uma revisão detalhada consegue revelar.

## Checklist de estudo

- Identifique todas as entradas, não apenas formulários.
- Use marcadores únicos para rastrear reflexões.
- Inspecione tanto a resposta HTTP quanto o DOM final.
- Determine o contexto antes de escolher o payload.
- Confirme manualmente todo resultado automatizado.
- Em DOM XSS, rastreie o caminho Source → transformações → Sink.
- Registre método HTTP, parâmetro, contexto, payload e resultado.
- Execute os testes somente em laboratórios ou sistemas autorizados.
