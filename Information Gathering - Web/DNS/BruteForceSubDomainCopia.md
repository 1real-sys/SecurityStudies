# Força Bruta em Subdomínios

A Enumeração de Subdomínios por Força Bruta é uma técnica ativa poderosa que utiliza listas predefinidas de nomes potenciais de subdomínios. Esta abordagem testa sistematicamente esses nomes contra o domínio alvo para identificar subdomínios válidos. Usando wordlists cuidadosamente elaboradas, você pode aumentar significativamente a eficiência e eficácia dos seus esforços de descoberta de subdomínios.

## O Processo em Quatro Etapas

1. **Seleção da Wordlist:** O processo começa selecionando uma wordlist contendo nomes potenciais de subdomínios. Essas wordlists podem ser:
   - **Propósito Geral:** Contendo uma ampla gama de nomes comuns de subdomínios (ex: dev, staging, blog, mail, admin, test). Esta abordagem é útil quando você não conhece as convenções de nomenclatura do alvo.
   - **Direcionadas:** Focadas em indústrias específicas, tecnologias ou padrões de nomenclatura relevantes ao alvo. Esta abordagem é mais eficiente e reduz as chances de falsos positivos.
   - **Personalizadas:** Você pode criar sua própria wordlist baseada em palavras-chave específicas, padrões ou inteligência coletada de outras fontes.

2. **Iteração e Consulta:** Um script ou ferramenta itera através da wordlist, anexando cada palavra ou frase ao domínio principal (ex: example.com) para criar nomes potenciais de subdomínios (ex: dev.example.com, staging.example.com).

3. **Consulta DNS:** Uma consulta DNS é realizada para cada subdomínio potencial para verificar se ele resolve para um endereço IP. Isso é tipicamente feito usando o tipo de registro A ou AAAA.

4. **Filtragem e Validação:** Se um subdomínio resolver com sucesso, ele é adicionado a uma lista de subdomínios válidos. Etapas adicionais de validação podem ser tomadas para confirmar a existência e funcionalidade do subdomínio (ex: tentando acessá-lo através de um navegador web).

## Ferramentas Disponíveis

| Ferramenta | Descrição |
|------------|-----------|
| dnsenum | Ferramenta abrangente de enumeração DNS que suporta ataques de dicionário e força bruta para descobrir subdomínios. |
| fierce | Ferramenta amigável para descoberta recursiva de subdomínios, com detecção de wildcard e interface fácil de usar. |
| dnsrecon | Ferramenta versátil que combina múltiplas técnicas de reconhecimento DNS e oferece formatos de saída personalizáveis. |
| amass | Ferramenta ativamente mantida focada em descoberta de subdomínios, conhecida por sua integração com outras ferramentas e extensas fontes de dados. |
| assetfinder | Ferramenta simples mas eficaz para encontrar subdomínios usando várias técnicas, ideal para varreduras rápidas e leves. |
| puredns | Ferramenta poderosa e flexível de força bruta DNS, capaz de resolver e filtrar resultados efetivamente. |

## DNSEnum

dnsenum é uma ferramenta de linha de comando versátil e amplamente usada escrita em Perl. É um toolkit abrangente para reconhecimento DNS, fornecendo várias funcionalidades para coletar informações sobre a infraestrutura DNS de um domínio alvo e subdomínios potenciais.

### Funções Principais

- **Enumeração de Registros DNS:** dnsenum pode recuperar vários registros DNS, incluindo A, AAAA, NS, MX e TXT, fornecendo uma visão abrangente da configuração DNS do alvo.
- **Tentativas de Transferência de Zona:** A ferramenta automaticamente tenta transferências de zona dos servidores de nomes descobertos. Embora a maioria dos servidores esteja configurada para prevenir transferências de zona não autorizadas, uma tentativa bem-sucedida pode revelar um tesouro de informações DNS.
- **Força Bruta de Subdomínios:** dnsenum suporta enumeração por força bruta de subdomínios usando uma wordlist. Isso envolve testar sistematicamente nomes potenciais de subdomínios contra o domínio alvo para identificar os válidos.
- **Scraping do Google:** A ferramenta pode fazer scraping dos resultados de busca do Google para encontrar subdomínios adicionais que podem não estar listados diretamente nos registros DNS.
- **Lookup Reverso:** dnsenum pode realizar lookups DNS reversos para identificar domínios associados a um endereço IP dado, potencialmente revelando outros sites hospedados no mesmo servidor.
- **Consultas WHOIS:** A ferramenta também pode realizar consultas WHOIS para coletar informações sobre propriedade e detalhes de registro do domínio.

### Exemplo de Uso

Demonstração de enumeração de subdomínios para inlanefreight.com usando a wordlist subdomains-top1million-20000.txt do SecLists:

```bash
dnsenum --enum inlanefreight.com -f /usr/share/seclists/Discovery/DNS/subdomains-top1million-20000.txt -r
```

**Parâmetros:**
- `dnsenum --enum inlanefreight.com`: Especifica o domínio alvo com opções de ajuste via --enum
- `-f /caminho/wordlist.txt`: Indica o caminho para a wordlist do SecLists
- `-r`: Habilita força bruta recursiva de subdomínios (se encontrar um subdomínio, tentará enumerar subdomínios desse subdomínio)

### Saída de Exemplo

```
dnsenum VERSION:1.2.6

-----   inlanefreight.com   -----

Host's addresses:
__________________

inlanefreight.com.                       300      IN    A        134.209.24.248

[...]

Brute forcing with /usr/share/seclists/Discovery/DNS/subdomains-top1million-20000.txt:
_______________________________________________________________________________________

www.inlanefreight.com.                   300      IN    A        134.209.24.248
support.inlanefreight.com.               300      IN    A        134.209.24.248
[...]

done.
```
