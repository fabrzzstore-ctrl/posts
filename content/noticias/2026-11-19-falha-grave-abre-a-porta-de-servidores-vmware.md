---
titulo: Falha grave abre a porta de servidores VMware
resumo: A Broadcom corrigiu uma falha com nota 9,8 em 10 no VMware vCenter, que permite entrar no sistema sem senha. Não há forma de se proteger sem actualizar.
data: 2026-11-19
nivel: CRÍTICO
tema: ciberseguranca
ilustracao: cloud
caixa: O QUE FAZER
acao: Quem gere VMware vCenter 8.0, 9.0 ou 9.1 deve instalar já a correcção da Broadcom (aviso VMSA-2026-0009). O utilizador comum não precisa de fazer nada.
fontes:
  - nome: "The Hacker News: Critical VMware vCenter flaw (CVSS 9.8)"
    url: https://thehackernews.com/2026/11/critical-vmware-vcenter-flaw-cvss-98.html
  - nome: "Rapid7: CVE-2026-123890, critical authentication bypass in VMware vCenter"
    url: https://www.rapid7.com/blog/post/etr-cve-2026-123890-critical-authentication-bypass-vmware-vcenter
  - nome: "Network World: Critical flaw in VMware vCenter allows authentication bypass"
    url: https://www.networkworld.com/article/4251001/critical-flaw-in-vmware-vcenter-allows-authentication-bypass.html
---
A Broadcom, dona da VMware, publicou a 19 de Novembro correcções para uma falha muito grave no VMware vCenter, o programa que as empresas usam para gerir os seus servidores virtuais. A falha tem o código CVE-2026-123890 e recebeu a nota 9,8 em 10.

## O que está em causa

O problema está no serviço de directório do vCenter (VMware Directory Service). Um atacante que consiga chegar ao sistema pela rede pode contornar a autenticação, ou seja, entrar sem precisar de senha. Como o vCenter controla dezenas ou centenas de servidores virtuais, quem o domina fica com acesso a grande parte da infra-estrutura informática de uma empresa.

Estão afectadas as versões 8.0, 9.0 e 9.1, incluindo as que vêm integradas no VMware Cloud Foundation, no vSphere Foundation e nas plataformas para operadoras de telecomunicações. A Broadcom diz que as versões antigas 6.5, 6.7 e 7.0 também devem ser consideradas vulneráveis. Para a 7.0, só há correcção para quem tem contrato de suporte alargado.

## Sem alternativa à actualização

Ao contrário de outros avisos, a Broadcom não indica nenhuma medida provisória para reduzir o risco. A única protecção eficaz é instalar a correcção. A falha foi comunicada pela Mandiant, empresa de segurança da Google.

O mesmo aviso (VMSA-2026-0009) corrige outras quatro falhas, com notas entre 6,7 e 8,1, no SDDC Manager e no VMware Tools para Windows.

## Já era usada por hackers

No dia seguinte soube-se que a falha já tinha sido usada como falha sem correcção (zero-day) mais de dois meses antes do aviso. Segundo a equipa de informações de ameaças da Google, um grupo suspeito de ligações à China, chamado Armory Castle, usou-a no início de Setembro para obter acesso de administrador a um vCenter dentro de uma rede que já tinha invadido.

## E em Angola?

O VMware é muito usado em centros de dados de bancos, operadoras, seguradoras e organismos públicos. As equipas de informática devem confirmar a versão do vCenter, instalar a correcção e rever os registos de acesso desde Setembro à procura de entradas estranhas.
