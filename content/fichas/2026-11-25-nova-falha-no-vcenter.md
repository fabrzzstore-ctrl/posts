---
nome: Nova falha no vCenter
codigo: CVE-2026-123903
categoria: Falha · VMware
severidade: CRÍTICA
nota: "9,8"
data: 2026-11-25
noticia: vmware-corrige-nova-falha-grave-nos-servidores
resumo: Falha no serviço de directório do vCenter que deixa entrar no sistema sem senha a partir da rede. A Broadcom corrigiu-a a 24 de Novembro e não refere ataques.
linhas:
  - rotulo: Revelada
    texto: A 24 de Novembro de 2026, no aviso VMSA-2026-0011 da Broadcom. Descoberta por investigadores da QiAnXin, da depthfirst e da ThreatBook.
  - rotulo: Onde está
    texto: No serviço de directório (vmdir) do vCenter, nas versões 7.0, 8.0, 9.0 e 9.1, e no VMware Cloud Foundation 5.x.
  - rotulo: O que faz
    texto: Permite que um atacante com acesso à rede onde está o vCenter contorne a verificação de identidade e entre no sistema sem senha.
  - rotulo: Alvos conhecidos
    texto: Empresas, bancos, operadoras e instituições que gerem servidores virtuais com o vCenter.
  - rotulo: Ataques
    texto: A Broadcom não refere ataques. Uma falha parecida (CVE-2026-123890) foi explorada por espiões ligados à China desde Setembro.
  - rotulo: Correcção
    texto: Disponível desde 24 de Novembro nas versões 8.0 U3m, 9.0.2.0300, 9.1.2 e Cloud Foundation 5.2.5. Quem usa a 7.0 deve contactar a Broadcom.
acao: Quem gere o vCenter deve actualizar já e não o deixar acessível pela internet. O utilizador comum não precisa de fazer nada.
fontes:
  - nome: "The Hacker News: VMware vCenter Hit by Another Critical 9.8-Rated Auth Bypass Flaw After Zero-Day Exploitation"
    url: https://thehackernews.com/2026/11/vmware-vcenter-hit-by-another-critical.html
---
No mesmo aviso, a Broadcom corrigiu 23 falhas no ESX, vCenter, Workstation, Fusion e Avi Load Balancer. No vCenter há ainda a CVE-2026-123904 (nota 7,5), que permite gravar ficheiros no sistema ao processar certos arquivos e pode levar à execução de programas, e três falhas (CVE-2026-123905, CVE-2026-123906 e CVE-2026-123907, nota 7,5 cada) que podem deixar o serviço de directório fora de serviço. Para usar a falha principal, o atacante precisa de chegar à rede onde o vCenter está ligado, por isso mantê-lo longe da internet reduz o risco. Não há medidas alternativas indicadas.
