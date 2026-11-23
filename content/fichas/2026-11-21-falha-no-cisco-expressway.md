---
nome: Falha no Cisco Expressway
codigo: CVE-2026-76466
categoria: "Falha · Cisco"
severidade: CRÍTICA
nota: "9,8"
data: 2026-11-21
noticia: hackers-ja-atacam-aparelhos-de-rede-da-cisco
resumo: "Falha no Cisco Expressway que permite executar comandos com permissões máximas em instalações em grupo. Já há ataques confirmados e a correcção existe desde Outubro."
linhas:
  - rotulo: Revelada
    texto: "Pela Cisco, com a correcção publicada a 21 de Outubro de 2026. O código de demonstração apareceu no GitHub a 5 de Novembro."
  - rotulo: Onde está
    texto: "No Cisco Expressway e no TelePresence Video Communication Server (VCS) instalados em grupo (cluster), incluindo a versão X15.5.3."
  - rotulo: O que faz
    texto: "Credenciais fixas no código, usadas na comunicação entre aparelhos do grupo, permitem executar comandos como root, ou seja, controlar o aparelho por completo."
  - rotulo: Alvos conhecidos
    texto: "Empresas, bancos, hospitais e serviços públicos que usam o Expressway para chamadas e videoconferências de funcionários fora do escritório."
  - rotulo: Ataques
    texto: "Confirmados. A empresa russa F6 relatou o ataque a uma organização na Rússia com quatro aparelhos comprometidos. A CISA juntou a falha ao catálogo KEV a 20 de Novembro."
  - rotulo: Correcção
    texto: "Disponível desde 21 de Outubro de 2026, na versão X15.5.20."
acao: "Quem gere Cisco Expressway deve instalar já a versão X15.5.20 e procurar sinais de invasão desde Novembro. O utilizador comum não precisa de fazer nada."
fontes:
  - nome: "SecurityWeek: Hackers exploit Cisco Expressway vulnerability soon after PoC release"
    url: https://securityweek.com/hackers-exploit-cisco-expressway-vulnerability-soon-after-poc-release
  - nome: "Action1: CVE-2026-76466, Cisco TelePresence VCS Expressway"
    url: https://www.action1.com/vulnerabilities/cve-2026-76466/
---
Na mesma actualização do catálogo de falhas exploradas, a 20 de Novembro, a CISA incluiu também uma falha no Apache Roller (CVE-2026-129448). Para a falha do Expressway, não há forma alternativa de bloqueio: a única solução é actualizar. Os aparelhos que estiveram expostos sem correcção desde o início de Novembro devem ser tratados como possivelmente comprometidos, com reinstalação e troca de todas as credenciais.
