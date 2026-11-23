---
titulo: "Espiões ligados à China já atacavam a falha do VMware"
resumo: "A falha grave do VMware vCenter revelada a 19 de Novembro já era usada desde Setembro por um grupo de espionagem ligado à China. A descoberta é da Mandiant, da Google."
data: 2026-11-20
nivel: CRÍTICO
tema: ciberseguranca
ilustracao: cloud
caixa: O QUE FAZER
acao: "Quem gere servidores VMware vCenter deve instalar já a correcção da Broadcom e procurar sinais de invasão desde Setembro. O utilizador comum não precisa de fazer nada."
fontes:
  - nome: "Google Cloud (Mandiant/GTIG): ARMORY CASTLE exploits vSphere"
    url: https://cloud.google.com/blog/topics/threat-intelligence/armory-castle-exploits-vsphere
  - nome: "SecurityWeek: Newly patched VMware vCenter flaw exploited as zero-day by Chinese APT"
    url: https://securityweek.com/newly-patched-vmware-vcenter-flaw-exploited-as-zero-day-by-chinese-apt
  - nome: "Cybersecurity Dive: Chinese espionage group exploited zero-day flaw in VMware vCenter"
    url: https://www.cybersecuritydive.com/news/chinese-espionage-zero-day-flaw-vmware-vcenter/875273/
---
A falha grave no VMware vCenter (CVE-2026-123890), corrigida pela Broadcom a 19 de Novembro, não era um perigo apenas teórico. Um dia depois, a Mandiant e o Grupo de Informações sobre Ameaças da Google (GTIG) revelaram que um grupo de espionagem ligado à China já a usava desde Setembro, antes de existir qualquer correcção. É o que se chama uma falha de dia zero (zero-day).

## Quem está por trás

A Google chama ao grupo Armory Castle e associa-o ao UNC5221, um grupo que já tinha sido apanhado a explorar falhas em equipamentos de rede de várias marcas nos últimos anos. O objectivo deste tipo de grupo não é pedir resgate, mas ficar escondido dentro das redes durante muito tempo para recolher informação.

Segundo a Mandiant, os atacantes combinaram a falha do vCenter com outra falha de dia zero, no software de assistência remota da BeyondTrust (CVE-2026-102764), e instalaram um programa espião a que os investigadores chamam Bonesaw.

## Porque o vCenter é um alvo valioso

O vCenter é o painel central que controla os servidores virtuais de uma empresa. Num só sítio, os administradores ligam, desligam, copiam e configuram dezenas ou centenas de máquinas. Quem o controla tem, na prática, as chaves de quase toda a infra-estrutura.

A falha recebeu a nota 9,8 em 10 e permite entrar no serviço de directório do vCenter sem senha. Afecta as versões 8.0, 9.0 e 9.1 e não há forma alternativa de a bloquear: a única solução é instalar a correcção.

## O que muda com esta descoberta

No dia anterior, a recomendação era actualizar depressa. Agora, as empresas têm também de assumir que podem já ter sido invadidas e de procurar sinais disso. A Mandiant publicou indicadores técnicos para ajudar as equipas de segurança nessa busca.

## O que fazer

Os responsáveis de informática devem:

- instalar de imediato a correcção da Broadcom em todos os vCenter;
- verificar também os sistemas BeyondTrust Remote Support, se existirem;
- procurar sinais de acesso indevido desde Setembro, usando os indicadores da Mandiant;
- garantir que o vCenter não está acessível directamente a partir da internet.

Bancos, operadoras e grandes empresas angolanas usam frequentemente VMware nos seus centros de dados. O utilizador comum não precisa de fazer nada.
