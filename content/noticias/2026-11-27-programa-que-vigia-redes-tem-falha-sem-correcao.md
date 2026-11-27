---
titulo: Programa que vigia redes de empresas tem falha grave sem correcção
resumo: Um investigador publicou um ataque que toma conta do Cacti, usado para vigiar redes, sem precisar de senha. Ainda não há correcção nem código CVE.
data: 2026-11-27
nivel: ALTO
tema: ciberseguranca
ilustracao: firewall
caixa: O QUE FAZER
acao: Quem usa o Cacti deve desligar a conta de convidado, limitar o acesso ao painel e instalar a correcção logo que saia. O utilizador comum não precisa de agir.
fontes:
  - nome: "The Hacker News: Unpatched Cacti Zero-Day Enables RCE in Just Four HTTP Requests via Guest Access"
    url: https://thehackernews.com/2026/11/unpatched-cacti-zero-day-enables-rce-in.html
---
Um investigador de segurança que usa o pseudónimo "ek0ms savi0r" publicou um ataque de demonstração que permite tomar conta do Cacti, um programa gratuito usado por empresas e operadoras para vigiar o funcionamento das suas redes. Basta enviar quatro pedidos ao servidor, sem senha. A falha afecta a versão mais recente, a 1.2.31, e ainda não tem correcção, segundo o The Hacker News, que noticiou o caso na sexta-feira. A empresa de segurança watchTowr também publicou um alerta.

## O que se passa

O ataque aproveita a conta de convidado do Cacti, que permite ver gráficos sem iniciar sessão. Quando essa conta está ligada, um atacante pode correr comandos no servidor como se fosse o próprio programa (execução remota de código). O investigador publicou duas versões da demonstração, chamadas 4HTTP2SHELL e 4HTTP2ROOT.

## Quem está em risco

O Cacti guarda muitas vezes as credenciais usadas para ler dados dos routers, servidores e outros equipamentos da rede. Um atacante que tome conta do programa pode usar essas credenciais para avançar dentro da empresa ou desligar os alertas que avisariam os técnicos de um problema. Ainda não há notícia de ataques reais, mas a demonstração pública torna-os mais prováveis.

## O estado actual

A falha ainda não recebeu código CVE e os responsáveis do Cacti ainda não lançaram uma correcção. Até lá, os especialistas recomendam:

- desligar a conta de convidado;
- limitar o acesso ao painel web do Cacti à rede interna ou a endereços de confiança;
- rever as configurações de recolha de dados à procura de comandos estranhos;
- instalar a correcção assim que for publicada.

## E em Angola?

Operadoras, bancos, universidades e empresas de serviços informáticos em Angola usam ferramentas como o Cacti para vigiar as suas redes. Os técnicos devem confirmar hoje se o programa está exposto à internet e se a conta de convidado está ligada. Para o utilizador comum, não há nada a fazer.
