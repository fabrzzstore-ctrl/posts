---
titulo: VMware corrige nova falha grave no vCenter, dias depois de um ataque
resumo: A Broadcom corrigiu uma nova falha grave no vCenter, o programa da VMware que gere servidores de empresas. Ainda não há ataques conhecidos, mas uma falha parecida já foi usada por espiões.
data: 2026-11-25
nivel: ALTO
tema: ciberseguranca
ilustracao: vpn
caixa: O QUE FAZER
acao: Quem gere o vCenter deve instalar já a correcção. O utilizador comum não precisa de fazer nada.
fontes:
  - nome: "The Hacker News: VMware vCenter Hit by Another Critical 9.8-Rated Auth Bypass Flaw After Zero-Day Exploitation"
    url: https://thehackernews.com/2026/11/vmware-vcenter-hit-by-another-critical.html
---
A Broadcom, empresa dona da VMware, publicou na terça-feira, 24 de Novembro, correcções para uma nova falha grave no vCenter, o programa que muitas empresas usam para gerir os seus servidores. A falha (CVE-2026-123903) recebeu a nota 9,8 em 10 e permite que alguém com acesso à rede entre no sistema sem precisar de senha. O aviso chega poucos dias depois de ter sido revelado que uma falha parecida no mesmo programa estava a ser usada por espiões desde Setembro.

## O que se passa

O problema está no serviço de directório do vCenter, a parte que confirma quem tem autorização para entrar. É como se a fechadura de uma porta aceitasse qualquer chave. Segundo a Broadcom, um atacante que consiga chegar à rede onde o vCenter está ligado pode contornar a verificação de identidade e ganhar acesso ao sistema.

A falha foi descoberta por investigadores da empresa chinesa QiAnXin, da depthfirst e da ThreatBook. A Broadcom diz que é diferente da falha CVE-2026-123890, que tem a mesma nota e que, segundo a Mandiant e a Google, foi explorada por um grupo de espionagem ligado à China antes de haver correcção.

No mesmo aviso (VMSA-2026-0011), a Broadcom corrigiu 23 falhas em vários produtos, incluindo outras quatro no vCenter: uma que permite gravar ficheiros no sistema e três que podem deixá-lo fora de serviço.

## Quem está em risco

O vCenter é usado sobretudo por empresas, bancos, operadoras e instituições públicas que têm muitos servidores virtuais, isto é, vários "computadores" a funcionar dentro de uma única máquina. Quem controla o vCenter controla todos esses servidores. Por isso, estas falhas são muito procuradas por grupos de espionagem e por quem lança ataques que bloqueiam os sistemas e exigem resgate.

## O estado actual

Até agora, a Broadcom não refere ataques que usem a nova falha. Há correcções para as versões 9.1 (9.1.2), 9.0 (9.0.2.0300), 8.0 (8.0 U3m) e para o VMware Cloud Foundation 5.x (5.2.5). Quem ainda usa a versão 7.0 em suporte alargado deve contactar a Broadcom. O aviso não indica medidas alternativas, por isso a solução é actualizar.

## E em Angola?

Muitas empresas e instituições angolanas usam a VMware nos seus centros de dados. Os técnicos que gerem estes sistemas devem instalar a correcção o mais depressa possível e evitar que o vCenter esteja acessível a partir da internet. O cidadão comum não precisa de fazer nada.
