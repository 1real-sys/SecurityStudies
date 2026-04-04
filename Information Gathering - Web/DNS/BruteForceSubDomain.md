# Força Bruta em Subdomínios

Técnica ativa que testa sistematicamente nomes de subdomínios de uma wordlist contra o domínio alvo.

## Processo (4 Etapas)

1. **Seleção da Wordlist:** Propósito geral (dev, staging, blog, admin), direcionada (indústria específica) ou personalizada
2. **Iteração:** Anexa cada palavra ao domínio (ex: dev.example.com)
3. **Consulta DNS:** Verifica se resolve para IP (registro A/AAAA)
4. **Validação:** Confirma existência e funcionalidade

## Ferramentas

| Ferramenta | Descrição |
|------------|-----------|
| **dnsenum** | Abrangente, suporta dicionário e força bruta |
| **fierce** | Descoberta recursiva, detecção de wildcard |
| **dnsrecon** | Múltiplas técnicas, saída personalizável |
| **amass** | Integração com outras ferramentas, extensas fontes |
| **assetfinder** | Simples, ideal para varreduras rápidas |
| **puredns** | Poderosa, filtragem eficaz de resultados |

## DNSEnum

Ferramenta CLI em Perl para reconhecimento DNS completo:

- Enumeração de registros (A, AAAA, NS, MX, TXT)
- Tentativas de transferência de zona
- Força bruta de subdomínios
- Scraping do Google
- Lookup reverso
- Consultas WHOIS

### Uso

```bash
dnsenum --enum inlanefreight.com -f /usr/share/seclists/Discovery/DNS/subdomains-top1million-20000.txt -r
```

- `--enum`: Domínio alvo com opções de ajuste
- `-f`: Caminho da wordlist
- `-r`: Força bruta recursiva (enumera subdomínios de subdomínios encontrados)

### Outras Opções Úteis

| Flag | Descrição |
|------|-----------|
| `--threads <n>` | Define número de threads (padrão: 5) |
| `-o <arquivo>` | Exporta resultados para arquivo XML |
| `--noreverse` | Pula lookup reverso (mais rápido) |
| `-s <n>` | Máximo de subdomínios do Google scraping (padrão: 15) |
| `-p <n>` | Máximo de páginas do Google a processar (padrão: 5) |

**Dica:** Para scans mais rápidos, combine `--noreverse` com mais threads: `--threads 10`