---
titulo: OpenAI e Cisco criam escudo de IA que trava ataques antes da correcção
resumo: A OpenAI e a Cisco lançaram o Shirudo, uma ferramenta gratuita em que a IA cria protecções temporárias para servidores Linux. Serve para ganhar tempo até haver uma correcção oficial.
data: 2026-11-25
nivel: NOVIDADE
tema: tecnologia
ilustracao: ia
caixa: PORQUE IMPORTA
acao: As empresas podem travar ataques a uma falha sem desligar os sistemas, ganhando tempo até instalarem a correcção oficial.
fontes:
  - nome: "The Hacker News: OpenAI and Cisco Unveil AI-Assisted Linux Security Tool to Block Exploits Before Patching"
    url: https://thehackernews.com/2026/11/openai-and-cisco-unveil-ai-assisted.html
---
A OpenAI, criadora do ChatGPT, e a Cisco, uma das maiores empresas de equipamentos de rede do mundo, apresentaram a 24 de Novembro o Shirudo, uma ferramenta gratuita e de código aberto que usa inteligência artificial para proteger servidores Linux contra ataques a falhas que ainda não foram corrigidas. O nome vem da palavra japonesa para "escudo".

## Como funciona

Quando é revelada uma falha grave, as empresas precisam de tempo para instalar a correcção, e muitas vezes isso obriga a reiniciar os sistemas. O Shirudo tenta resolver esse intervalo. Agentes de IA escrevem pequenas protecções temporárias que bloqueiam o caminho que o ataque usaria, sem desligar os serviços. É como pôr uma tranca provisória numa porta enquanto o serralheiro não chega.

Antes de serem activadas, as protecções podem ser testadas para confirmar que travam o ataque sem bloquear o uso normal. São também assinadas digitalmente, para garantir que não foram alteradas. A ferramenta assenta no Tetragon, uma plataforma de segurança para Linux tornada pública em 2022 pela Isovalent.

Segundo as empresas, num teste controlado, uma protecção criada pelo Codex, a ferramenta de programação da OpenAI, travou uma tentativa de ataque com a falha do Java (Java4Shell) contra um serviço em funcionamento, sem ser preciso reiniciá-lo.

## Porque importa

Nas últimas semanas surgiram várias falhas graves em programas muito usados, como o Java, o NGINX e o VMware, e os hackers começaram a explorá-las poucos dias depois de reveladas. A Cisco diz que a protecção "só passa a bloquear quando os dados mostram que é seguro". As empresas descrevem o Shirudo como um "primeiro passo" para sistemas que se defendem sozinhos.

## E em Angola?

Para as equipas técnicas de bancos, operadoras e instituições angolanas, que muitas vezes demoram a actualizar sistemas críticos, ferramentas deste tipo podem reduzir o risco no período mais perigoso. Ainda assim, não substituem a correcção oficial, que continua a ser obrigatória.
