---
nome: Falha no VMware vCenter
codigo: CVE-2026-123890
categoria: Falha · VMware
severidade: CRÍTICA
nota: "9,8"
data: 2026-11-20
noticia: falha-grave-abre-a-porta-de-servidores-vmware
resumo: Falha no serviço de directório do VMware vCenter que permite entrar no sistema sem senha. Foi usada por espiões ligados à China desde Setembro, antes de haver correcção.
linhas:
  - rotulo: Revelada
    texto: A 19 de Novembro de 2026, pela Broadcom (aviso VMSA-2026-0009). Comunicada pela Mandiant, da Google.
  - rotulo: Onde está
    texto: No VMware Directory Service do vCenter 8.0, 9.0 e 9.1, incluindo o VMware Cloud Foundation, o vSphere Foundation e as plataformas Telco. As versões 6.5, 6.7 e 7.0 devem ser consideradas vulneráveis.
  - rotulo: O que faz
    texto: Permite a quem tenha acesso pela rede contornar a autenticação e entrar no vCenter, que controla os servidores virtuais da empresa.
  - rotulo: Alvos conhecidos
    texto: Centros de dados de empresas e organismos públicos. A Google ligou os ataques ao grupo Armory Castle, suspeito de ligações à China.
  - rotulo: Ataques
    texto: Usada como falha sem correcção (zero-day) desde o início de Setembro de 2026 para obter acesso de administrador em redes já invadidas.
  - rotulo: Correcção
    texto: Disponível desde 19 de Novembro para todas as versões suportadas. A Broadcom não indica medidas alternativas. Na versão 7.0, só com suporte alargado.
acao: Quem gere VMware vCenter deve instalar a correcção de imediato e rever os registos de acesso desde Setembro. O utilizador comum não precisa de fazer nada.
fontes:
  - nome: "The Hacker News: Critical VMware vCenter flaw (CVSS 9.8)"
    url: https://thehackernews.com/2026/11/critical-vmware-vcenter-flaw-cvss-98.html
  - nome: "Rapid7: CVE-2026-123890, critical authentication bypass in VMware vCenter"
    url: https://www.rapid7.com/blog/post/etr-cve-2026-123890-critical-authentication-bypass-vmware-vcenter
---
O mesmo aviso da Broadcom corrige mais quatro falhas, com notas entre 6,7 e 8,1: três no SDDC Manager (CVE-2026-123891, CVE-2026-123892 e CVE-2026-123893) e uma no VMware Tools para Windows (CVE-2026-123894).
