---
titulo: "Falha da Microsoft expõe dados de empresas clientes"
resumo: "Uma falha num serviço do Entra, o sistema de contas empresariais da Microsoft, foi explorada para ler dados de organizações, como e-mails de administradores. Foi corrigida a 19 de Novembro."
data: 2026-11-21
nivel: ALTO
tema: ciberseguranca
ilustracao: cloud
caixa: O QUE FAZER
acao: "Os administradores de Microsoft 365 devem estar atentos a e-mails falsos dirigidos a eles nas próximas semanas. A Microsoft já corrigiu a falha."
fontes:
  - nome: "BleepingComputer: Microsoft Entra Connect Health flaw exploited to steal tenant data"
    url: https://www.bleepingcomputer.com/news/security/microsoft-entra-connect-health-flaw-exploited-to-steal-tenant-data/
  - nome: "Cybersecurity News: Hackers exploit Microsoft Entra Connect Health flaw"
    url: https://cybersecuritynews.com/microsoft-entra-connect-health-flaw/
---
A Microsoft confirmou que uma falha no Entra Connect Health, um serviço que vigia a ligação entre os servidores das empresas e as contas na nuvem da Microsoft, foi usada por atacantes para ler informações de organizações clientes. O caso foi noticiado a 21 de Novembro pelo BleepingComputer. A falha existia desde 23 de Julho, foi descoberta a 9 de Novembro e corrigida a 19 de Novembro.

## Que dados foram expostos

A falha permitia ler metadados das organizações, a que a Microsoft chama tenants: os endereços de e-mail dos administradores, identificadores internos e informações sobre as licenças contratadas. A Microsoft garante que não foram expostas senhas, chaves de acesso (tokens) nem o conteúdo de e-mails ou ficheiros.

A falha não recebeu um código CVE, porque foi corrigida do lado da Microsoft, sem que os clientes precisassem de instalar nada.

## Porque estes dados interessam aos hackers

Pode parecer pouco, mas saber quem são os administradores de uma empresa é muito útil para um atacante. São essas as pessoas com as chaves do reino: podem criar contas, mudar permissões e ver os dados de todos. Com o e-mail certo e informação sobre as licenças, um hacker consegue preparar mensagens falsas muito convincentes, como avisos de renovação, alertas de segurança ou pedidos de aprovação, para enganar precisamente quem tem mais poder.

Como resumiu um analista, a Microsoft corrigiu a falha, mas o risco de mensagens falsas não tem correcção.

## O que fazer

Os administradores de Microsoft 365 e Entra devem:

- desconfiar de e-mails que peçam para aprovar acessos, renovar licenças ou entrar numa página para «resolver um problema de segurança»;
- usar métodos de entrada resistentes a burlas, como chaves de segurança ou a aplicação Authenticator com confirmação por número;
- rever os registos de entrada das contas de administração nas últimas semanas;
- confirmar se receberam algum aviso da Microsoft no centro de mensagens do Microsoft 365.

Muitas empresas e instituições angolanas usam o Microsoft 365. O utilizador comum não precisa de fazer nada, além de desconfiar de e-mails estranhos em nome da Microsoft.
