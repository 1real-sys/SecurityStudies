# Ferramentas

Neste módulo, utilizaremos quatro ferramentas poderosas projetadas para reconhecimento de aplicações web e avaliação de vulnerabilidades. Para agilizar nossa configuração, vamos instalar todas antecipadamente.

## Instalando Go, Python e PIPX

Você precisará ter Go e Python instalados para essas ferramentas. Instale-os como mostrado abaixo, caso ainda não estejam instalados.

`pipx` é uma ferramenta de linha de comando criada para simplificar a instalação e o gerenciamento de aplicações Python. Ela facilita o processo ao criar ambientes virtuais isolados para cada aplicação, garantindo que as dependências não entrem em conflito. Isso significa que você pode instalar e executar várias aplicações Python sem se preocupar com problemas de compatibilidade. O `pipx` também facilita atualizar ou desinstalar aplicações, mantendo seu sistema organizado e sem acúmulo desnecessário.

Se você estiver usando um sistema baseado em Debian (como Ubuntu), pode instalar Go, Python e PIPX usando o gerenciador de pacotes APT.

Abra um terminal e atualize a lista de pacotes para garantir que você tenha as informações mais recentes sobre as versões novas dos pacotes e suas dependências.

```bash
sudo apt update
```

Use o comando a seguir para instalar Go:

```bash
sudo apt install -y golang
```

Use o comando a seguir para instalar Python:

```bash
sudo apt install -y python3 python3-pip
```

Use o comando a seguir para instalar e configurar o pipx:

```bash
sudo apt install pipx
pipx ensurepath
sudo pipx ensurepath --global
```

Para garantir que Go e Python foram instalados corretamente, você pode verificar suas versões:

```bash
go version
python3 --version
```

Se as instalações tiverem sido bem-sucedidas, você verá as informações de versão de Go e Python.

## FFUF

FFUF (Fuzz Faster U Fool) é um fuzzer web rápido escrito em Go. Ele se destaca por enumerar rapidamente diretórios, arquivos e parâmetros em aplicações web. Sua flexibilidade, velocidade e facilidade de uso fazem dele uma ferramenta favorita entre profissionais e entusiastas de segurança.

Você pode instalar o FFUF com o seguinte comando:

```bash
go install github.com/ffuf/ffuf/v2@latest
```

### Casos de uso

| Caso de uso | Descrição |
| --- | --- |
| Enumeração de diretórios e arquivos | Identifique rapidamente diretórios e arquivos ocultos em um servidor web. |
| Descoberta de parâmetros | Encontre e teste parâmetros em aplicações web. |
| Ataque de força bruta | Execute ataques de força bruta para descobrir credenciais de login ou outras informações sensíveis. |

## Gobuster

Gobuster é outro fuzzer popular para diretórios e arquivos web. É conhecido por sua velocidade e simplicidade, sendo uma ótima escolha tanto para iniciantes quanto para usuários experientes.

Você pode instalar o GoBuster com o seguinte comando:

```bash
go install github.com/OJ/gobuster/v3@latest
```

### Casos de uso

| Caso de uso | Descrição |
| --- | --- |
| Descoberta de conteúdo | Faça varredura rápida para encontrar conteúdo web oculto, como diretórios, arquivos e hosts virtuais. |
| Enumeração de subdomínios DNS | Identifique subdomínios de um domínio-alvo. |
| Detecção de conteúdo WordPress | Use wordlists específicas para encontrar conteúdo relacionado a WordPress. |

## FeroxBuster

FeroxBuster é uma ferramenta de descoberta de conteúdo rápida e recursiva escrita em Rust. Ela é projetada para descoberta por força bruta de conteúdo não linkado em aplicações web, sendo particularmente útil para identificar diretórios e arquivos ocultos. Ela é mais uma ferramenta de "forced browsing" do que um fuzzer como o ffuf.

Para instalar o FeroxBuster, você pode usar o seguinte comando:

```bash
curl -sL https://raw.githubusercontent.com/epi052/feroxbuster/main/install-nix.sh | sudo bash -s $HOME/.local/bin
```

### Casos de uso

| Caso de uso | Descrição |
| --- | --- |
| Varredura recursiva | Execute varreduras recursivas para descobrir diretórios e arquivos aninhados. |
| Descoberta de conteúdo não linkado | Identifique conteúdo que não está linkado dentro da aplicação web. |
| Varreduras de alto desempenho | Aproveite o desempenho do Rust para conduzir descoberta de conteúdo em alta velocidade. |

## wfuzz/wenum

`wenum` é um fork ativamente mantido do `wfuzz`, uma ferramenta de fuzzing em linha de comando altamente versátil e poderosa, conhecida por sua flexibilidade e opções de personalização. Ela é especialmente adequada para fuzzing de parâmetros, permitindo testar uma ampla variedade de valores de entrada em aplicações web e descobrir vulnerabilidades potenciais na forma como esses parâmetros são processados.

Se você estiver usando uma distribuição Linux de testes de invasão como PwnBox ou Kali, o `wfuzz` pode já vir pré-instalado, permitindo uso imediato, se desejar. No entanto, atualmente há complicações na instalação do `wfuzz`, então você pode substituí-lo por `wenum`. Os comandos são intercambiáveis e seguem a mesma sintaxe, então você pode simplesmente trocar comandos de `wenum` por `wfuzz` quando necessário.

Os comandos abaixo usam `pipx`, uma ferramenta para instalar e gerenciar aplicações Python em ambientes isolados, para instalar o `wenum`. Isso garante um ambiente limpo e consistente para o `wenum`, evitando possíveis conflitos de pacotes:

```bash
pipx install git+https://github.com/WebFuzzForge/wenum
pipx runpip wenum install setuptools
```

### Casos de uso

| Caso de uso | Descrição |
| --- | --- |
| Enumeração de diretórios e arquivos | Identifique rapidamente diretórios e arquivos ocultos em um servidor web. |
| Descoberta de parâmetros | Encontre e teste parâmetros em aplicações web. |
| Ataque de força bruta | Execute ataques de força bruta para descobrir credenciais de login ou outras informações sensíveis. |

## Grau de detecção das ferramentas

**Legenda:** 🟢 não detectável/discreto · 🟡 detectável · 🔴 detectável com risco de banimento e rastreio

| Ferramenta | Grau | Leitura prática de detecção |
| --- | --- | --- |
| FFUF | 🟡 | Gera padrão de enumeração e volume de requisições que costuma aparecer em logs, WAF e IDS. |
| Gobuster | 🟡 | Muito detectável por repetição de paths e comportamento de brute-force de conteúdo. |
| FeroxBuster | 🔴 | Recursão e alta taxa de varredura aumentam bastante chance de bloqueio, rate-limit, rastreio e banimento. |
| wfuzz/wenum | 🔴 | Fuzzing de parâmetros com payloads anômalos tende a disparar regras de segurança e facilitar correlação de origem. |
