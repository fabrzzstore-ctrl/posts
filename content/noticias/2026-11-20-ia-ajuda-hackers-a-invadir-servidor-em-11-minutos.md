---
titulo: "IA ajuda hackers a invadir servidor em 11 minutos"
resumo: "A Amazon revelou que agentes de IA usados por hackers encontraram e exploraram uma falha desconhecida num servidor de uma universidade em apenas 11 minutos."
data: 2026-11-20
nivel: ALTO
tema: ciberseguranca
ilustracao: ia
caixa: PORQUE IMPORTA
acao: "Os ataques com IA são cada vez mais rápidos. Servidores expostos à internet sem actualizações podem ser invadidos em minutos."
fontes:
  - nome: "SecurityWeek: Amazon, China-linked hackers' AI agents exploited medical software zero-day"
    url: https://www.securityweek.com/amazon-china-linked-hackers-ai-agents-exploited-medical-software-zero-day/
  - nome: "Cloud Security Alliance: MONAI Label zero-day, AI agents exploit medical imaging research servers"
    url: https://labs.cloudsecurityalliance.org/research/csa-research-note-monai-label-agent-discovered-zero-day-2026/
---
A equipa de informações sobre ameaças da Amazon revelou que um grupo de hackers ligado à China usou agentes de inteligência artificial, a que chama Cairn, para descobrir e explorar uma falha até então desconhecida no MONAI Label, um programa usado em investigação de imagens médicas. Do primeiro contacto com o servidor até obterem controlo total, passaram apenas 11 minutos. O caso foi noticiado a 20 de Novembro.

## O que aconteceu

O ataque teve lugar em Setembro e atingiu servidores de universidades da Ásia Oriental. O MONAI Label é uma ferramenta de código aberto que ajuda investigadores a marcar imagens médicas, como TACs e ressonâncias, para treinar modelos de IA. Estes servidores estavam acessíveis a partir da internet.

Os agentes de IA analisaram o programa, encontraram uma falha de dia zero (zero-day), escreveram o código para a explorar e usaram-no para obter as permissões máximas no servidor. A correcção para o MONAI Label saiu a 18 de Novembro.

## Porque os 11 minutos assustam

Tradicionalmente, encontrar uma falha nova e criar um ataque funcional levava dias ou semanas a especialistas. Os agentes de IA fizeram todo o processo em minutos, sem intervenção humana constante. Isto reduz muito o tempo que os defensores têm para reagir.

Curiosamente, foram os próprios registos deixados pelos agentes que permitiram aos investigadores reconstruir cada passo do ataque.

## Uma vaga de ataques com IA

O caso junta-se a outros relatados nas últimas semanas: a Google, a Barracuda e a própria Amazon descreveram ataques em que a IA foi usada para criar exploits ou conduzir invasões. A Amazon já tinha revelado em Novembro outra campanha com agentes de IA, chamada ARTEX, que roubava chaves de acesso a serviços de IA.

## Porque importa

Para universidades, hospitais e centros de investigação, incluindo em Angola, a lição é clara: ferramentas de investigação não devem estar expostas directamente à internet, precisam de ser actualizadas e devem ter acesso protegido. Com a IA a acelerar os ataques, deixar um servidor esquecido online é cada vez mais perigoso.
