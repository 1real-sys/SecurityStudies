# Logs de Transparência de Certificados

Na vasta extensão da internet, a confiança é uma mercadoria frágil. Uma das bases dessa confiança é o protocolo Secure Sockets Layer/Transport Layer Security (SSL/TLS), que criptografa a comunicação entre seu navegador e um site. No coração do SSL/TLS está o certificado digital, um pequeno arquivo que verifica a identidade de um site e permite uma comunicação segura e criptografada.

No entanto, o processo de emissão e gerenciamento desses certificados não é infalível. Atacantes podem explorar certificados fraudulentos ou emitidos incorretamente para se passar por sites legítimos, interceptar dados sensíveis ou espalhar malware. É aqui que os logs de Transparência de Certificados (CT) entram em cena.

## O que são Logs de Transparência de Certificados?

Os logs de Transparência de Certificados (CT) são registros públicos, apenas de adição (append-only), que registram a emissão de certificados SSL/TLS. Sempre que uma Autoridade Certificadora (CA) emite um novo certificado, ela deve submetê-lo a múltiplos logs CT. Organizações independentes mantêm esses logs e estão abertos para qualquer pessoa inspecionar.

Pense nos logs CT como um registro global de certificados. Eles fornecem um registro transparente e verificável de cada certificado SSL/TLS emitido para um site. Esta transparência serve a vários propósitos cruciais:

- **Detecção Precoce de Certificados Fraudulentos:** Ao monitorar os logs CT, pesquisadores de segurança e proprietários de sites podem identificar rapidamente certificados suspeitos ou emitidos incorretamente. Um certificado fraudulento é um certificado digital não autorizado ou falsificado emitido por uma autoridade certificadora confiável. Detectá-los cedo permite ação rápida para revogar os certificados antes que possam ser usados para fins maliciosos.

- **Responsabilização das Autoridades Certificadoras:** Os logs CT responsabilizam as CAs por suas práticas de emissão. Se uma CA emitir um certificado que viole as regras ou padrões, isso será publicamente visível nos logs, levando a potenciais sanções ou perda de confiança.

- **Fortalecimento da Web PKI (Infraestrutura de Chave Pública):** A Web PKI é o sistema de confiança que sustenta a comunicação online segura. Os logs CT ajudam a melhorar a segurança e integridade da Web PKI fornecendo um mecanismo para supervisão pública e verificação de certificados.

## Logs CT e Reconhecimento Web

Os logs de Transparência de Certificados oferecem uma vantagem única na enumeração de subdomínios comparado a outros métodos. Diferentemente de força bruta ou abordagens baseadas em wordlist, que dependem de adivinhar ou prever nomes de subdomínios, os logs CT fornecem um registro definitivo de certificados emitidos para um domínio e seus subdomínios. Isso significa que você não está limitado pelo escopo da sua wordlist ou pela eficácia do seu algoritmo de força bruta. Em vez disso, você ganha acesso a uma visão histórica e abrangente dos subdomínios de um domínio, incluindo aqueles que podem não estar ativamente em uso ou facilmente adivinháveis.

Além disso, os logs CT podem revelar subdomínios associados a certificados antigos ou expirados. Esses subdomínios podem hospedar software ou configurações desatualizadas, tornando-os potencialmente vulneráveis à exploração.

Em essência, os logs CT fornecem uma maneira confiável e eficiente de descobrir subdomínios sem a necessidade de força bruta exaustiva ou depender da completude de wordlists. Eles oferecem uma janela única para a história de um domínio e podem revelar subdomínios que de outra forma permaneceriam ocultos, melhorando significativamente suas capacidades de reconhecimento.

## Pesquisando Logs CT

Existem duas opções populares para pesquisar logs CT:

| Ferramenta | Recursos Principais | Casos de Uso | Prós | Contras |
|------------|---------------------|--------------|------|---------|
| crt.sh | Interface web amigável, busca simples por domínio, exibe detalhes do certificado, entradas SAN. | Buscas rápidas e fáceis, identificar subdomínios, verificar histórico de emissão de certificados. | Gratuito, fácil de usar, sem necessidade de registro. | Opções limitadas de filtragem e análise. |
| Censys | Motor de busca poderoso para dispositivos conectados à internet, filtragem avançada por domínio, IP, atributos de certificado. | Análise aprofundada de certificados, identificar configurações incorretas, encontrar certificados e hosts relacionados. | Dados extensivos e opções de filtragem, acesso à API. | Requer registro (camada gratuita disponível). |

## Consulta via crt.sh

Embora o crt.sh ofereça uma interface web conveniente, você também pode usar sua API para buscas automatizadas diretamente do seu terminal. Veja como encontrar todos os subdomínios 'dev' em facebook.com usando curl e jq:

```bash
curl -s "https://crt.sh/?q=facebook.com&output=json" | jq -r '.[]
 | select(.name_value | contains("dev")) | .name_value' | sort -u
 
*.dev.facebook.com
*.newdev.facebook.com
*.secure.dev.facebook.com
dev.facebook.com
devvm1958.ftw3.facebook.com
facebook-amex-dev.facebook.com
facebook-amex-sign-enc-dev.facebook.com
newdev.facebook.com
secure.dev.facebook.com
```

### Explicação do Comando

- `curl -s "https://crt.sh/?q=facebook.com&output=json"`: Busca a saída JSON do crt.sh para certificados correspondentes ao domínio facebook.com.
- `jq -r '.[] | select(.name_value | contains("dev")) | .name_value'`: Filtra os resultados JSON, selecionando apenas entradas onde o campo name_value (que contém o domínio ou subdomínio) inclui a string "dev". A flag -r diz ao jq para exibir strings brutas.
- `sort -u`: Ordena os resultados alfabeticamente e remove duplicatas.
