---
titulo: "Hackers já atacam aparelhos de rede da Cisco"
resumo: "Uma falha grave no Cisco Expressway, usado em videoconferências e chamadas de empresas, já está a ser explorada. A CISA juntou-a à lista de falhas atacadas a 20 de Novembro."
data: 2026-11-21
nivel: CRÍTICO
tema: ciberseguranca
ilustracao: firewall
caixa: O QUE FAZER
acao: "Quem gere Cisco Expressway deve instalar já a versão X15.5.20, disponível desde Outubro. O utilizador comum não precisa de fazer nada."
fontes:
  - nome: "SecurityWeek: Hackers exploit Cisco Expressway vulnerability soon after PoC release"
    url: https://securityweek.com/hackers-exploit-cisco-expressway-vulnerability-soon-after-poc-release
  - nome: "SecurityOnline: Cisco Expressway vulnerabilities, root RCE patched"
    url: https://securityonline.info/cisco-expressway-vulnerabilities-root-rce-patched/
  - nome: "Action1: CVE-2026-76466, Cisco TelePresence VCS Expressway"
    url: https://www.action1.com/vulnerabilities/cve-2026-76466/
---
Uma falha grave no Cisco Expressway (CVE-2026-76466), o equipamento que liga as videoconferências e as chamadas internas das empresas ao exterior, já está a ser usada em ataques. A CISA, a agência de cibersegurança dos Estados Unidos, acrescentou-a a 20 de Novembro ao seu catálogo de falhas exploradas, e a empresa de segurança russa F6 relatou um ataque real contra uma organização na Rússia.

## O que é o Expressway

O Expressway é usado por empresas, bancos, hospitais e serviços públicos para permitir que funcionários fora do escritório façam chamadas e videoconferências pelo sistema da empresa, sem precisarem de uma ligação VPN. Por isso, está normalmente virado para a internet, o que o torna um alvo directo.

## A falha

A falha recebeu a nota 9,8 em 10. Afecta instalações em grupo (cluster) e está ligada a credenciais fixas no código, usadas na comunicação entre os aparelhos do grupo. Um atacante que as conheça pode executar comandos com as permissões máximas do sistema (root), ou seja, controlar o aparelho por completo.

A Cisco corrigiu o problema na versão X15.5.20, lançada a 21 de Outubro. A versão X15.5.3 está entre as afectadas.

## Do código público ao ataque

A 5 de Novembro apareceu no GitHub um código de demonstração que mostra como explorar a falha. Pouco depois, a F6 detectou o ataque a uma organização russa, em que foram comprometidos quatro aparelhos Expressway. É o padrão habitual: quando o método fica público, os atacantes passam a procurar aparelhos que ainda não foram actualizados.

Na mesma actualização do catálogo, a CISA incluiu também uma falha no Apache Roller (CVE-2026-129448), um programa para criar blogues.

## Quem está em risco

Estão em risco as organizações que usam Expressway em grupo e que não instalaram a correcção de Outubro. Um aparelho destes invadido pode servir para escutar chamadas, entrar na rede interna ou lançar outros ataques.

## O que fazer

Os responsáveis de informática devem actualizar para a X15.5.20 ou mais recente, verificar os registos desde o início de Novembro à procura de acessos estranhos e, se houver dúvidas, tratar o aparelho como comprometido: reinstalar e mudar todas as credenciais. Em Angola, operadoras, bancos e ministérios usam frequentemente equipamentos Cisco de comunicações. O utilizador comum não precisa de fazer nada.
