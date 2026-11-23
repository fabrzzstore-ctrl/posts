---
titulo: "Sites falsos pedem para colar comandos no computador"
resumo: "A Blackpoint Cyber descreveu uma campanha que engana as vítimas para colarem um comando no Windows, que instala um programa espião. Os burlões usam sites falsos e até assistentes do ChatGPT."
data: 2026-11-20
nivel: ALTO
tema: ciberseguranca
ilustracao: portatil
caixa: O QUE FAZER
acao: "Nenhum site legítimo pede para colar comandos na janela Executar ou no PowerShell. Se uma página pedir isso, feche-a."
fontes:
  - nome: "Blackpoint Cyber: ROMULUS campaign, CNCMachineRMS RAT analysis"
    url: https://blackpointcyber.com/blog/romulus-cncmachinerms/
  - nome: "Cybersecurity News: Hackers use new ROMULUS ClickFix platform to deliver malware"
    url: https://cybersecuritynews.com/new-romulus-clickfix-platform/
  - nome: "SecurityWeek: Hackers use ChatGPT custom GPTs in ClickFix attacks"
    url: https://securityweek.com/hackers-use-chatgpt-custom-gpts-in-clickfix-attacks
---
A empresa de segurança Blackpoint Cyber publicou a 20 de Novembro uma análise da campanha ROMULUS, que usa uma técnica de burla cada vez mais comum, chamada ClickFix. A vítima é levada a copiar e colar um comando no próprio computador, convencida de que está a resolver um problema ou a provar que não é um robô. Na verdade, está a instalar um programa que permite aos atacantes espiar e controlar o computador à distância.

## Como funciona o golpe

A página mostra uma mensagem como «erro ao carregar» ou «verificação de segurança» e dá instruções simples: carregar em duas teclas para abrir a janela Executar do Windows, colar o texto que já foi copiado automaticamente e carregar em Enter. Parece inofensivo, mas esse texto é um comando que descarrega e instala o programa malicioso.

Na campanha ROMULUS, os atacantes usaram, entre outros, um site falso da Stardock, uma empresa que vende programas para personalizar o Windows, e assistentes personalizados do ChatGPT (Custom GPTs) criados para dar «ajuda» que incluía o comando malicioso.

## O que instala

O programa final é um RAT, uma ferramenta de acesso remoto, a que os investigadores chamam CNCMachineRMS. Com ele, os atacantes podem ver o ecrã, registar o que se escreve, roubar ficheiros e senhas e usar o computador para outros ataques. Pelo caminho, é usado também um programa de carregamento conhecido como Legion Loader.

## Porque funciona

O ClickFix explora a confiança: a pessoa sente que está a seguir instruções técnicas legítimas, e o comando é colado por ela própria, o que ajuda a enganar algumas protecções. Ao usar assistentes do ChatGPT, os burlões aproveitam ainda a credibilidade das ferramentas de IA.

## O que fazer

- Nunca cole comandos na janela Executar, no PowerShell ou no Terminal a pedido de um site.
- Desconfie de «verificações» que pedem combinações de teclas como Windows+R.
- Descarregue programas só dos sites oficiais, escrevendo o endereço à mão.
- Em empresas, os administradores podem limitar o uso do PowerShell e da janela Executar para utilizadores comuns.
- Se já colou um comando suspeito, desligue o computador da internet e peça ajuda a um técnico de confiança.
