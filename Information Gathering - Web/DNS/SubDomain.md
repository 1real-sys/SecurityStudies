# Subdomínios

Subdomínios são extensões do domínio principal, criados para organizar diferentes seções de um site (ex: blog.example.com, shop.example.com, mail.example.com).

## Por que é Importante?

Subdomínios frequentemente hospedam:

- **Ambientes de Dev/Staging:** Podem conter vulnerabilidades devido a segurança relaxada
- **Portais de Login Ocultos:** Painéis administrativos não públicos
- **Aplicações Legadas:** Software desatualizado com vulnerabilidades conhecidas
- **Informações Sensíveis:** Documentos confidenciais ou arquivos de configuração expostos

## Enumeração de Subdomínios

Processo de identificar subdomínios sistematicamente. Representados por registros A/AAAA (mapeiam para IP) ou CNAME (aliases).

### 1. Enumeração Ativa

Interação direta com servidores DNS do alvo:
- **Transferência de zona DNS:** Servidor mal configurado pode vazar lista de subdomínios (raramente funciona)
- **Força bruta:** Testar lista de nomes potenciais. Ferramentas: **dnsenum**, **ffuf**, **gobuster**

### 2. Enumeração Passiva

Fontes externas sem consultar DNS do alvo:
- **Logs CT (Certificate Transparency):** Certificados SSL/TLS contêm subdomínios no campo SAN
- **Motores de busca:** Operador `site:` no Google/DuckDuckGo
- **Bancos de dados online:** Agregam dados DNS de múltiplas fontes

### Estratégia

Ativa = mais controle, mais detectável. Passiva = furtiva, menos completa. **Combinar ambas** para melhores resultados.