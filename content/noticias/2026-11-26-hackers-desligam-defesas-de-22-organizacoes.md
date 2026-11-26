---
titulo: Hackers desligam defesas de rede de 22 organizações em 17 países
resumo: Hackers controlaram 24 servidores da Check Point que gerem as barreiras de rede de 22 organizações. A GreyNoise suspeita que o ataque foi feito com ajuda de inteligência artificial.
data: 2026-11-26
nivel: ALTO
tema: ciberseguranca
ilustracao: firewall
caixa: O QUE FAZER
acao: Quem gere aparelhos da Check Point deve instalar a correcção que já existe, limitar o acesso aos painéis de gestão e procurar sinais de actividade estranha. O utilizador comum não precisa de agir.
fontes:
  - nome: "The Hacker News: Hackers Compromise 24 Check Point Management Servers in Suspected AI-Driven Attack Campaign"
    url: https://thehackernews.com/2026/11/hackers-compromise-24-check-point.html
---
Um grupo de hackers ainda não identificado tomou o controlo de 24 servidores que gerem as barreiras de protecção da rede (firewalls) da Check Point, em 22 organizações de 17 países. O caso foi revelado a 25 de Novembro pela GreyNoise, uma empresa que vigia ataques na internet, e suspeita-se que os atacantes usaram ferramentas de inteligência artificial.

## O que se passou

A GreyNoise acompanhou a campanha entre 17 de Outubro e 2 de Novembro. As vítimas são dos sectores financeiro, da energia, do governo, dos transportes, da mineração, da engenharia e da indústria, em países como o Reino Unido, a França, a Alemanha, a Índia, a Coreia do Sul, a Austrália e os Estados Unidos.

Os servidores atacados são os "centros de comando" das firewalls: é a partir deles que as empresas decidem o que entra e o que sai da sua rede. Os hackers usaram uma falha já conhecida e corrigida (CVE-2026-16232) para correr mais de cem tarefas de gestão. Tentaram roubar as bases de dados das firewalls e ficheiros de certificados, criar um certificado novo e desligar regras de segurança, o que equivale a abrir as portas de um edifício por dentro. Depois, procuraram avançar para outros computadores das organizações.

## A suspeita de uso de IA

A GreyNoise diz que os atacantes usavam um sistema automático para procurar e atacar servidores vulneráveis, e suspeita do uso de "agentes" de IA que trabalham sozinhos. É uma suspeita e não uma prova. A empresa também não conseguiu perceber como os hackers entraram pela primeira vez nos servidores da Check Point.

## O que diz a Check Point

Sergey Shykevich, director de informações sobre ameaças da Check Point, afirmou que o ataque se apoia numa falha já revelada e corrigida, e não numa técnica nova. A empresa pede aos clientes que instalem as actualizações, sigam as suas recomendações de segurança, limitem o acesso aos painéis de gestão e procurem actividade suspeita.

## Porque importa

As firewalls são a primeira linha de defesa de bancos, operadoras e empresas, também em Angola. Quando os próprios aparelhos de protecção ficam nas mãos dos atacantes, toda a rede fica exposta. O caso mostra, mais uma vez, que atrasar uma actualização de segurança pode sair caro.
