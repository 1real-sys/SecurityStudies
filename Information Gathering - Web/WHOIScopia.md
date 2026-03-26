
WHOIS é um protocolo de consulta e resposta amplamente utilizado, projetado para acessar bancos de dados que armazenam informações sobre recursos registrados na internet. Primordialmente associado a nomes de domínio, o WHOIS também pode fornecer detalhes sobre blocos de endereços IP e sistemas autônomos. Imagine-o como uma gigantesca lista telefônica da internet, permitindo que você consulte quem é o proprietário ou responsável por diversos ativos online.

        sessão de shell
JLMreal@htb[/htb]$ whois inlanefreight.com

[...]
Domain Name: inlanefreight.com
Registry Domain ID: 2420436757_DOMAIN_COM-VRSN
Registrar WHOIS Server: whois.registrar.amazon
Registrar URL: https://registrar.amazon.com
Updated Date: 2023-07-03T01:11:15Z
Creation Date: 2019-08-05T22:43:09Z
[...]

Cada registro WHOIS normalmente contém as seguintes informações:

Domain NameO próprio nome de domínio (ex.: example.com)
RegistrarA empresa onde o domínio foi registrado (ex.: GoDaddy, Namecheap)
Registrant ContactA pessoa ou organização que registrou o domínio.
Administrative ContactA pessoa responsável pela gestão do domínio.
Technical ContactA pessoa responsável por lidar com questões técnicas relacionadas ao domínio.
Creation and Expiration DatesQuando o domínio foi registrado e quando ele expira.
Name ServersServidores que traduzem o nome de domínio em um endereço IP.
Histórico do WHOIS
A história do WHOIS está intrinsecamente ligada à visão e dedicação de Elizabeth Feinler , uma cientista da computação que desempenhou um papel fundamental na formação da internet em seus primórdios.

Na década de 1970, Feinler e sua equipe no Centro de Informações de Rede (NIC) do Instituto de Pesquisa de Stanford reconheceram a necessidade de um sistema para rastrear e gerenciar o crescente número de recursos de rede na ARPANET, precursora da internet moderna. Sua solução foi a criação do diretório WHOIS, um banco de dados rudimentar, porém inovador, que armazenava informações sobre usuários de rede, nomes de host e nomes de domínio.

Clique para expandir e descobrir um fato interessante sobre a história da internet, caso tenha interesse.

Por que o WHOIS é importante para a reanálise de sites?
Os dados WHOIS servem como um tesouro de informações para os profissionais de testes de penetração durante a fase de reconhecimento de uma avaliação. Eles oferecem insights valiosos sobre a presença digital da organização-alvo e suas potenciais vulnerabilidades.

Identifying Key PersonnelOs registros WHOIS frequentemente revelam os nomes, endereços de e-mail e números de telefone dos indivíduos responsáveis ​​pela administração do domínio. Essas informações podem ser exploradas para ataques de engenharia social ou para identificar potenciais alvos de campanhas de phishing.
Discovering Network InfrastructureDetalhes técnicos como servidores de nomes e endereços IP fornecem pistas sobre a infraestrutura de rede do alvo. Isso pode ajudar os testadores de penetração a identificar possíveis pontos de entrada ou configurações incorretas.
Historical Data AnalysisAcessar registros históricos do WHOIS por meio de serviços como o WhoisFreaks pode revelar mudanças de propriedade, informações de contato ou detalhes técnicos ao longo do tempo. Isso pode ser útil para acompanhar a evolução da presença digital da empresa-alvo.