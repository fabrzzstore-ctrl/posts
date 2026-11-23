---
titulo: "Falha no Windows abre programas sem pedir a senha"
resumo: "Um investigador revelou uma forma de contornar o ecrã de bloqueio do Windows através do Narrador, a ferramenta de leitura de ecrã. Ainda não há correcção da Microsoft."
data: 2026-11-20
nivel: MÉDIO
tema: ciberseguranca
ilustracao: portatil
caixa: O QUE FAZER
acao: "Para usar esta falha, é preciso ter o computador nas mãos. Não deixe o portátil sozinho em locais públicos e instale a correcção assim que a Microsoft a lançar."
fontes:
  - nome: "ThreatLocker: Proof of concept for FastUnlock Windows lock screen bypass from Nightmare Eclipse"
    url: https://www.threatlocker.com/blog/proof-of-concept-for-fastunlock-windows-lock-screen-bypass-from-nightmare-eclipse
  - nome: "Security Affairs: Chaotic Eclipse releases FastUnlock, a new Windows zero-day"
    url: https://securityaffairs.com/?p=203537
  - nome: "Born City: FastUnlock, Windows-11-Lücke"
    url: https://borncity.com/news/fastunlock-windows-11-luecke-soll-bitlocker-in-fuenf-minuten-umgehen/
---
Um investigador de segurança conhecido pelo pseudónimo Nightmare Eclipse publicou a 19 de Novembro uma forma de contornar o ecrã de bloqueio do Windows. A técnica, a que chamou FastUnlock, usa o Narrador, a ferramenta de acessibilidade que lê em voz alta o que aparece no ecrã, para abrir programas sem ser preciso escrever a senha. A Microsoft ainda não lançou correcção.

## Como funciona

O ecrã de bloqueio do Windows deixa usar algumas funções de acessibilidade antes de a pessoa entrar, para que quem tem dificuldades de visão consiga iniciar sessão. O investigador descobriu que, através do Narrador e de um componente do sistema ligado às contas (WSIAccount), é possível lançar programas a partir desse ecrã, com permissões que não deviam estar disponíveis.

A empresa de segurança ThreatLocker analisou a técnica e confirmou que a demonstração funciona. Alguns sites especializados referem que o método poderia ajudar a contornar também a cifra do disco (BitLocker), mas esse ponto ainda não foi confirmado de forma independente.

## Quem está em risco

A falha só pode ser usada por quem tenha acesso físico ao computador: não funciona à distância, pela internet. O risco é maior para portáteis perdidos ou roubados, computadores partilhados em escritórios e máquinas deixadas sozinhas em cafés, aeroportos ou salas de aula.

Num computador roubado, contornar o ecrã de bloqueio pode dar acesso a ficheiros, e-mails e contas abertas no navegador.

## Um investigador em guerra com a Microsoft

O mesmo investigador já tinha publicado outras falhas do Windows sem esperar pela correcção, em protesto contra a forma como a Microsoft trata quem lhe reporta problemas. Esta prática é polémica: dá visibilidade ao problema, mas também entrega o método aos criminosos antes de haver solução.

## O que fazer

Enquanto não há correcção:

- não deixe o portátil sozinho em locais públicos;
- em empresas, os administradores podem limitar as ferramentas de acessibilidade no ecrã de bloqueio de computadores que não precisem delas;
- mantenha as actualizações automáticas do Windows ligadas, para receber a correcção assim que sair;
- em caso de roubo, mude as senhas das contas que estavam abertas no computador.
