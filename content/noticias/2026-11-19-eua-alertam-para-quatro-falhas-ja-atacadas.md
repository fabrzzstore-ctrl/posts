---
titulo: EUA alertam para quatro falhas já atacadas
resumo: A CISA, a agência de cibersegurança dos EUA, juntou à sua lista de falhas em uso por hackers problemas no Synology, no LiteLLM, no Apache Axis e no REDCap.
data: 2026-11-19
nivel: ALTO
tema: ciberseguranca
ilustracao: escudo
caixa: O QUE FAZER
acao: Quem tem um NAS da Synology deve actualizar o DSM já. Empresas com LiteLLM, Apache Axis 1 ou REDCap devem corrigir ou desligar estes sistemas da internet.
fontes:
  - nome: "The Hacker News: CISA warns of 4 exploited flaws"
    url: https://thehackernews.com/2026/11/cisa-warns-of-4-exploited-flaws-linked.html
  - nome: "Security Affairs: CISA adds flaws to its Known Exploited Vulnerabilities catalog"
    url: https://securityaffairs.com/?p=203504
  - nome: "CISA: Known Exploited Vulnerabilities Catalog"
    url: https://cisa.gov/kev
---
A CISA, a agência de cibersegurança dos Estados Unidos, acrescentou a 18 de Novembro quatro falhas à sua lista de vulnerabilidades que já estão a ser usadas em ataques reais (catálogo KEV). Os organismos públicos americanos têm prazos curtos para as corrigir, mas o aviso serve para empresas de todo o mundo.

## Synology: ataques com resgate

A falha que mais interessa a utilizadores comuns está no DSM, o sistema dos aparelhos de armazenamento em rede (NAS) da Synology, muito usados em pequenas empresas e em casa para guardar cópias de segurança. Com o código CVE-2024-10441 e nota 9,8, permite executar comandos à distância. Está a ser usada para instalar o ransomware C3RB3R, que bloqueia os ficheiros e exige um resgate.

## LiteLLM: roubo de acesso à IA

O LiteLLM é uma ferramenta que as empresas usam para ligar as suas aplicações a vários modelos de inteligência artificial. A falha CVE-2026-40217 (nota 8,8) permite executar código através de uma função de teste. Segundo a Google, os atacantes usam-na para transformar chaves de acesso limitadas em credenciais de administrador e gastar o serviço de IA da vítima, uma prática conhecida como LLMjacking. Os alvos incluem empresas financeiras, de retalho, transportes e tecnologia na América e na Ásia-Pacífico.

## Apache Axis e REDCap

O Apache Axis 1.x, uma biblioteca antiga de serviços web, tem uma falha (CVE-2026-90436, nota 9,8) que já não terá correcção oficial, porque a versão chegou ao fim de vida. A Rapid7 viu-a ser usada contra o Confluence da Atlassian para procurar senhas e números de cartões. A recomendação é migrar para o Axis 2.

O REDCap, plataforma da Universidade Vanderbilt usada em investigação médica, tem uma falha (CVE-2026-90817, nota 9,8) que está a ser usada para instalar programas que mineram moedas digitais nos servidores.

## Porque importa

Estas falhas não são teóricas: já há quem as use. Quem tem um destes sistemas ligado à internet deve tratá-lo como prioridade máxima.
