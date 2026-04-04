# Transferência de Zona DNS

Método menos invasivo que força bruta para descobrir subdomínios. Mecanismo de replicação de registros DNS que, se mal configurado, expõe toda a zona.

## O que é

Cópia completa de todos os registros DNS de uma zona (domínio + subdomínios) entre servidores. Essencial para redundância, mas perigoso se não protegido.

## Processo (AXFR)

1. **Requisição AXFR:** Servidor secundário solicita transferência ao primário
2. **Registro SOA:** Primário envia Start of Authority (contém serial da zona)
3. **Transmissão:** Todos os registros (A, AAAA, MX, CNAME, NS...) são transferidos
4. **Conclusão:** Primário sinaliza fim; secundário confirma (ACK)

## A Vulnerabilidade

Servidores mal configurados permitem que qualquer cliente solicite a zona completa. Informações expostas:

- **Subdomínios:** Lista completa, incluindo ocultos (dev, staging, admin)
- **Endereços IP:** Alvos para reconhecimento/ataques
- **Servidores de Nomes:** Revela provedor e configurações

## Remediação

Servidores modernos restringem transferências apenas para secundários confiáveis. Configurações incorretas ainda ocorrem por erro humano.

## Exploração com dig

```bash
dig axfr @nsztm1.digi.ninja zonetransfer.me
```

- `axfr`: Solicita transferência de zona completa
- `@servidor`: Servidor DNS alvo
- `domínio`: Zona a ser transferida

### Saída (exemplo com zonetransfer.me)

```
zonetransfer.me.    7200    IN  SOA nsztm1.digi.ninja. robin.digi.ninja. ...
zonetransfer.me.    7200    IN  A   5.196.105.14
zonetransfer.me.    7200    IN  NS  nsztm1.digi.ninja.
canberra-office.zonetransfer.me. 7200 IN A  202.14.81.230
;; XFR size: 50 records
```

> **Nota:** zonetransfer.me é um serviço de demonstração de riscos de transferências de zona.