# Transferência de Zona DNS

Enquanto força bruta pode ser uma abordagem frutífera, existe um método menos invasivo e potencialmente mais eficiente para descobrir subdomínios – transferências de zona DNS. Este mecanismo, projetado para replicar registros DNS entre servidores de nomes, pode inadvertidamente se tornar uma mina de ouro de informações se mal configurado.

## O que é uma Transferência de Zona

Uma transferência de zona DNS é essencialmente uma cópia por atacado de todos os registros DNS dentro de uma zona (um domínio e seus subdomínios) de um servidor de nomes para outro. Este processo é essencial para manter consistência e redundância entre servidores DNS. No entanto, se não estiver adequadamente protegido, partes não autorizadas podem baixar o arquivo de zona inteiro, revelando uma lista completa de subdomínios, seus endereços IP associados e outros dados DNS sensíveis.

## Processo de Transferência de Zona

1. **Requisição de Transferência de Zona (AXFR):** O servidor DNS secundário inicia o processo enviando uma requisição de transferência de zona ao servidor primário. Esta requisição tipicamente usa o tipo AXFR (Transferência de Zona Completa).

2. **Transferência do Registro SOA:** Ao receber a requisição (e potencialmente autenticar o servidor secundário), o servidor primário responde enviando seu registro Start of Authority (SOA). O registro SOA contém informações vitais sobre a zona, incluindo seu número serial, que ajuda o servidor secundário a determinar se seus dados de zona estão atualizados.

3. **Transmissão de Registros DNS:** O servidor primário então transfere todos os registros DNS na zona para o servidor secundário, um por um. Isso inclui registros como A, AAAA, MX, CNAME, NS e outros que definem os subdomínios do domínio, servidores de email, servidores de nomes e outras configurações.

4. **Transferência de Zona Completa:** Uma vez que todos os registros foram transmitidos, o servidor primário sinaliza o fim da transferência de zona. Esta notificação informa ao servidor secundário que ele recebeu uma cópia completa dos dados da zona.

5. **Reconhecimento (ACK):** O servidor secundário envia uma mensagem de reconhecimento ao servidor primário, confirmando o recebimento e processamento bem-sucedido dos dados da zona. Isso completa o processo de transferência de zona.

## A Vulnerabilidade de Transferência de Zona

Enquanto transferências de zona são essenciais para gerenciamento legítimo de DNS, um servidor DNS mal configurado pode transformar este processo em uma vulnerabilidade de segurança significativa. O problema central está nos controles de acesso que governam quem pode iniciar uma transferência de zona.

Nos primeiros dias da internet, era prática comum permitir que qualquer cliente solicitasse uma transferência de zona de um servidor DNS. Esta abordagem aberta simplificava a administração, mas abriu uma grande falha de segurança. Significava que qualquer pessoa, incluindo atores maliciosos, poderia pedir a um servidor DNS uma cópia completa de seu arquivo de zona, que contém uma riqueza de informações sensíveis.

### Informações Reveladas

As informações obtidas de uma transferência de zona não autorizada podem ser invaluáveis para um atacante. Ela revela um mapa abrangente da infraestrutura DNS do alvo, incluindo:

- **Subdomínios:** Uma lista completa de subdomínios, muitos dos quais podem não estar vinculados ao site principal ou facilmente descobertos por outros meios. Esses subdomínios ocultos podem hospedar servidores de desenvolvimento, ambientes de staging, painéis administrativos ou outros recursos sensíveis.
- **Endereços IP:** Os endereços IP associados a cada subdomínio, fornecendo alvos potenciais para reconhecimento adicional ou ataques.
- **Registros de Servidor de Nomes:** Detalhes sobre os servidores de nomes autoritativos para o domínio, revelando o provedor de hospedagem e potenciais configurações incorretas.

## Remediação

Felizmente, a conscientização sobre esta vulnerabilidade cresceu, e a maioria dos administradores de servidores DNS mitigou o risco. Servidores DNS modernos são tipicamente configurados para permitir transferências de zona apenas para servidores secundários confiáveis, garantindo que dados sensíveis de zona permaneçam confidenciais.

No entanto, configurações incorretas ainda podem ocorrer devido a erro humano ou práticas desatualizadas. Por isso, tentar uma transferência de zona (com autorização adequada) permanece uma técnica de reconhecimento valiosa. Mesmo se malsucedida, a tentativa pode revelar informações sobre a configuração e postura de segurança do servidor DNS.

## Explorando Transferências de Zona

Você pode usar o comando `dig` para solicitar uma transferência de zona:

```bash
dig axfr @nsztm1.digi.ninja zonetransfer.me
```

Este comando instrui o `dig` a solicitar uma transferência de zona completa (axfr) do servidor DNS responsável por zonetransfer.me. Se o servidor estiver mal configurado e permitir a transferência, você receberá uma lista completa de registros DNS para o domínio, incluindo todos os subdomínios.

### Exemplo de Saída

```
; <<>> DiG 9.18.12-1~bpo11+1-Debian <<>> axfr @nsztm1.digi.ninja zonetransfer.me
; (1 server found)
;; global options: +cmd
zonetransfer.me.    7200    IN  SOA nsztm1.digi.ninja. robin.digi.ninja. 2019100801 172800 900 1209600 3600
zonetransfer.me.    300 IN  HINFO   "Casio fx-700G" "Windows XP"
zonetransfer.me.    7200    IN  MX  0 ASPMX.L.GOOGLE.COM.
...
zonetransfer.me.    7200    IN  A   5.196.105.14
zonetransfer.me.    7200    IN  NS  nsztm1.digi.ninja.
zonetransfer.me.    7200    IN  NS  nsztm2.digi.ninja.
_acme-challenge.zonetransfer.me. 301 IN TXT "6Oa05hbUJ9xSsvYy7pApQvwCUSSGgxvrbdizjePEsZI"
_sip._tcp.zonetransfer.me. 14000 IN SRV 0 0 5060 www.zonetransfer.me.
asfdbbox.zonetransfer.me. 7200  IN  A   127.0.0.1
canberra-office.zonetransfer.me. 7200 IN A  202.14.81.230
...
;; XFR size: 50 records (messages 1, bytes 2085)
```

> **Nota:** zonetransfer.me é um serviço configurado especificamente para demonstrar os riscos de transferências de zona.
