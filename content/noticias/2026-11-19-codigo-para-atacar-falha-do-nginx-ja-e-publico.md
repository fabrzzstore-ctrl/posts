---
titulo: Código para atacar falha do NGINX já é público
resumo: A F5 corrigiu cinco falhas graves no NGINX, o programa que serve milhões de sites. Investigadores já publicaram código que mostra como explorar a mais conhecida, baptizada de NGINX2Root.
data: 2026-11-19
nivel: ALTO
tema: ciberseguranca
ilustracao: firewall
caixa: O QUE FAZER
acao: Quem gere servidores com NGINX deve actualizar já para a versão 1.30.7 ou 1.31.9 (ou NGINX Plus 37.0.8.1 e 37.3.0.1). O utilizador comum não precisa de fazer nada.
fontes:
  - nome: "SecurityWeek: F5 patches critical NGINX2Root flaws as PoC exploits go public"
    url: https://www.securityweek.com/f5-patches-critical-nginx2root-flaws-as-poc-exploits-go-public/
  - nome: "BleepingComputer: Critical NGINX2Root bugs let attackers hijack servers"
    url: https://bleepingcomputer.com/news/security/critical-nginx-nginx2root-bugs-let-attackers-hijack-servers
  - nome: "Help Net Security: NGINX2Root, F5 patches five critical NGINX vulnerabilities"
    url: https://www.helpnetsecurity.com/?p=391836
---
A F5, empresa que desenvolve o NGINX, lançou a 18 de Novembro correcções para cinco falhas graves neste programa, que é usado por milhões de sites e serviços para receber e distribuir o tráfego da internet. O conjunto foi baptizado de NGINX2Root e todas as falhas receberam a nota 9,2 em 10.

## O que permitem fazer

No pior caso, um atacante consegue executar comandos no servidor sem precisar de senha (execução remota de código), com as permissões do próprio NGINX. A partir daí, pode chegar ao controlo total da máquina. A falha mais falada, com o código CVE-2026-123007, afecta todas as versões do NGINX desde a 1.9.5, lançada em 2015, segundo a empresa de segurança Wiz.

Nem todos os servidores estão expostos da mesma forma. Duas das falhas só funcionam com o protocolo HTTP/2 ligado, outra com HTTP/3, outra quando o NGINX funciona como intermediário de e-mail e a última em configurações de proxy específicas. A F5 diz que, para executar código, o atacante precisa de contornar uma protecção de memória do sistema (ASLR). A Wiz afirma que duas das falhas permitem precisamente isso.

## O código já circula

A Rapid7 publicou uma demonstração de ataque (PoC), mas que exige enviar cerca de 128 GB de dados. A Censys conseguiu reproduzir o problema com muito menos tráfego e pôs o código no GitHub, o que facilita a vida a quem quer atacar. Segundo a Censys, cerca de 9 milhões de serviços na internet usam uma versão afectada com HTTP/2 ligado, e há mais 103 milhões que não revelam a versão.

Até agora, a F5 diz não ter registo de ataques reais. A publicação do código costuma, no entanto, encurtar o tempo até aos primeiros ataques.

## Quem descobriu

As falhas foram comunicadas por várias equipas: Ikotas Labs, Metnir, Rapid7, Wiz e Xint. A Xint mostrou que é possível juntar a falha principal a um problema no Linux para sair de um contentor Docker. Na mesma actualização, a F5 corrigiu 22 falhas no total, incluindo 12 no BIG-IP.

## E em Angola?

Bancos, operadoras, empresas públicas e alojamentos de sites que usam NGINX devem confirmar a versão instalada e actualizar quanto antes, começando pelos servidores ligados à internet. Para quem só visita sites, não há nada a fazer.
