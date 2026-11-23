---
titulo: "Uma página web bastava para enganar a IA da Meta"
resumo: "Investigadores da NebuSec mostraram que uma página maliciosa conseguia levar o Muse, o assistente de IA da Meta, a entregar conversas e memórias do utilizador. A falha já foi corrigida."
data: 2026-11-21
nivel: MÉDIO
tema: ciberseguranca
ilustracao: ia
caixa: O QUE FAZER
acao: "Não dê a assistentes de IA acesso a contas, pagamentos ou senhas sem necessidade, e mantenha as apps actualizadas."
fontes:
  - nome: "Guardian MSSP (via The Hacker News): A single malicious webpage let researchers hijack Meta Muse and access private chats"
    url: https://www.guardianmssp.com/2026/11/21/a-single-malicious-webpage-let-researchers-hijack-meta-muse-and-access-private-chats/
  - nome: "FourWeekMBA: 1 webpage let researchers pull Meta Muse chats and memories"
    url: https://fourweekmba.com/ai-1-webpage-let-researchers-pull-meta-muse-chats-and-memories/
  - nome: "Meta AI: Security and safety for AI agents, our approach with Muse"
    url: https://research.meta.ai/blog/security-and-safety-for-ai-agents-our-approach-with-muse
---
Investigadores da empresa de segurança NebuSec demonstraram que bastava uma página web preparada de propósito para enganar o Muse, o assistente de inteligência artificial da Meta, e levá-lo a entregar conversas privadas e memórias guardadas sobre o utilizador. O trabalho foi divulgado a 20 de Novembro e noticiado pelo The Hacker News no dia seguinte. A Meta já corrigiu o problema.

## O que é o Muse

O Muse é um agente de IA da Meta que não se limita a conversar: pode navegar na internet, usar contas do utilizador e até fazer pagamentos em seu nome. Para isso, guarda memórias sobre a pessoa e trabalha numa máquina na nuvem. É precisamente este poder que o torna um alvo atractivo.

## Como funcionava o ataque

Quando o Muse abria a página maliciosa, encontrava instruções escondidas no texto, invisíveis para uma pessoa mas lidas pela IA. O assistente tratava-as como ordens e acabava por enviar para os atacantes o conteúdo das conversas e das memórias. Os investigadores conseguiram ainda controlar a máquina na nuvem usada pelo agente e contornar o Sentinel, o sistema de protecção da Meta.

Este tipo de truque chama-se injecção de instruções (prompt injection) e é um dos maiores problemas de segurança dos agentes de IA.

## Uma demonstração, não um ataque real

A NebuSec fez a demonstração em laboratório e informou a Meta, que corrigiu a falha. Não há indicação de que tenha sido usada contra utilizadores reais. Não é, porém, o primeiro problema do Muse: em Setembro e Outubro, outros investigadores já tinham revelado falhas que permitiam sequestrar o agente.

## O que fazer

Quem usa assistentes de IA com acesso a contas deve:

- dar apenas as permissões estritamente necessárias;
- evitar ligar o assistente a contas bancárias, de pagamento ou de e-mail principal;
- rever e apagar regularmente as memórias guardadas pelo assistente;
- manter a aplicação sempre actualizada.

Quanto mais um assistente pode fazer sozinho, maior o estrago se for enganado.
