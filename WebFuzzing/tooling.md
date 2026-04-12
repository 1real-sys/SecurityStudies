# Ferramentas

Neste módulo, utilizaremos quatro ferramentas poderosas para reconhecimento de aplicações web e avaliação de vulnerabilidades. Para simplificar o ambiente, instalaremos tudo de uma vez.

## Instalando Go, Python e pipx

Você precisará de Go e Python instalados. Se estiver em um sistema baseado em Debian (como Ubuntu), use:

```bash
sudo apt update
sudo apt install -y golang
sudo apt install -y python3 python3-pip
sudo apt install pipx
pipx ensurepath
sudo pipx ensurepath --global
```

Para confirmar a instalação:

```bash
go version
python3 --version
```

## FFUF

FFUF (Fuzz Faster U Fool) é um fuzzer web rápido escrito em Go. Ele se destaca na enumeração rápida de diretórios, arquivos e parâmetros em aplicações web.

Instalação:

```bash
go install github.com/ffuf/ffuf/v2@latest
```

Casos de uso:

| Caso de uso | Descrição |
| --- | --- |
| Enumeração de diretórios e arquivos | Identifica rapidamente diretórios e arquivos ocultos em um servidor web. |
| Descoberta de parâmetros | Encontra e testa parâmetros em aplicações web. |
| Ataque de força bruta | Executa tentativas para descobrir credenciais de login ou outras informações sensíveis. |

## Gobuster

Gobuster é outro fuzzer popular para diretórios e arquivos web, conhecido pela velocidade e simplicidade.

Instalação:

```bash
go install github.com/OJ/gobuster/v3@latest
```

Casos de uso:

| Caso de uso | Descrição |
| --- | --- |
| Descoberta de conteúdo | Localiza conteúdo web oculto, como diretórios, arquivos e virtual hosts. |
| Enumeração de subdomínios DNS | Identifica subdomínios de um domínio-alvo. |
| Detecção de conteúdo WordPress | Usa wordlists específicas para encontrar conteúdo relacionado a WordPress. |

## FeroxBuster

FeroxBuster é uma ferramenta rápida e recursiva de descoberta de conteúdo, escrita em Rust. É voltada para descoberta por força bruta de conteúdo não linkado em aplicações web.

Instalação:

```bash
curl -sL https://raw.githubusercontent.com/epi052/feroxbuster/main/install-nix.sh | sudo bash -s $HOME/.local/bin
```

Casos de uso:

| Caso de uso | Descrição |
| --- | --- |
| Varredura recursiva | Descobre diretórios e arquivos aninhados. |
| Descoberta de conteúdo não linkado | Identifica conteúdo que não está vinculado na aplicação web. |
| Varreduras de alto desempenho | Aproveita o desempenho do Rust para descoberta de conteúdo em alta velocidade. |

## wfuzz/wenum

`wenum` é um fork ativamente mantido do `wfuzz`, uma ferramenta de fuzzing em linha de comando bastante versátil, especialmente útil para fuzzing de parâmetros.

Em distribuições de pentest como PwnBox ou Kali, o `wfuzz` pode já vir instalado. Como podem existir complicações na instalação do `wfuzz`, você pode usar `wenum` como substituto. Os comandos são intercambiáveis e seguem a mesma sintaxe.

Instalação do `wenum` com `pipx`:

```bash
pipx install git+https://github.com/WebFuzzForge/wenum
pipx runpip wenum install setuptools
```

Casos de uso:

| Caso de uso | Descrição |
| --- | --- |
| Enumeração de diretórios e arquivos | Identifica rapidamente diretórios e arquivos ocultos em um servidor web. |
| Descoberta de parâmetros | Encontra e testa parâmetros em aplicações web. |
| Ataque de força bruta | Executa tentativas para descobrir credenciais de login ou outras informações sensíveis. |

## Grau de detecção das ferramentas

**Legenda:** 🟢 não detectável/discreto · 🟡 detectável · 🔴 detectável com risco de banimento e rastreio

| Ferramenta | Grau | Leitura prática de detecção |
| --- | --- | --- |
| FFUF | 🟡 | Gera padrão de enumeração e volume de requisições que costuma aparecer em logs, WAF e IDS. |
| Gobuster | 🟡 | Muito detectável por repetição de paths e comportamento de brute-force de conteúdo. |
| FeroxBuster | 🔴 | Recursão e alta taxa de varredura aumentam bastante chance de bloqueio, rate-limit, rastreio e banimento. |
| wfuzz/wenum | 🔴 | Fuzzing de parâmetros com payloads anômalos tende a disparar regras de segurança e facilitar correlação de origem. |
