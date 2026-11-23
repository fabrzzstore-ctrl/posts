---
titulo: "Mensagens enviadas à IA foram parar a estranhos"
resumo: "Um estudo da Dragos com milhões de mensagens-armadilha mostrou que três fornecedores de IA foram invadidos. A OpenRouter afastou-os e retirou 125 serviços da sua lista de privacidade."
data: 2026-11-22
nivel: ALTO
tema: ciberseguranca
ilustracao: ia
caixa: O QUE FAZER
acao: "Nunca escreva senhas, dados bancários ou documentos confidenciais em conversas com IA, sobretudo em serviços intermédios pouco conhecidos."
fontes:
  - nome: "Dragos: Three breaches, endless leaks, your AI supply chain needs canaries"
    url: https://www.dragos.com/blog/ai-supply-chain-security-canary-tokens
  - nome: "OpenRouter: Zero Data Retention"
    url: https://openrouter.ai/docs/guides/features/zdr
---
A empresa de segurança Dragos publicou um estudo que mostra como mensagens enviadas a modelos de inteligência artificial podem acabar nas mãos de estranhos. Durante meses, a Dragos enviou cerca de 2 milhões de mensagens de teste com «armadilhas» escondidas (canary tokens) e descobriu que três fornecedores de IA tinham sido invadidos desde meados de Julho. Na sequência, a OpenRouter, uma plataforma que distribui pedidos por dezenas de fornecedores, afastou esses três e retirou 125 serviços da sua lista de «zero retenção de dados», a 22 de Novembro.

## Como funciona a armadilha

Uma canary token é um dado falso, como uma chave de acesso ou um endereço, que não serve para nada além de avisar quando alguém o usa. A Dragos escondeu milhares destes dados nas mensagens enviadas aos modelos. Se uma chave falsa fosse usada mais tarde, era a prova de que alguém tinha lido a mensagem original.

Foi assim que a empresa percebeu que, em três fornecedores, as mensagens estavam a ser lidas por quem não devia.

## Os casos conhecidos

Um dos casos citados envolve a Together AI, que teve uma fuga de mensagens entre Junho e Julho, por causa de uma credencial deixada no GitHub. Outros fornecedores mencionados são a Novita e a Phala. As empresas foram contactadas, e a OpenRouter decidiu agir de imediato.

## O problema dos intermédios

Muitas aplicações de IA não usam directamente os modelos da OpenAI, da Anthropic ou da Google. Passam por plataformas como a OpenRouter, que encaminham o pedido para o fornecedor mais barato ou mais rápido. Cada intermédio a mais é mais um sítio onde as mensagens podem ser guardadas, vistas ou roubadas.

A promessa de «zero retenção» significa que o fornecedor não guarda as mensagens. O estudo mostra que essa promessa não chega se os sistemas do fornecedor forem invadidos.

## O que fazer

- Nunca escreva senhas, códigos, dados bancários ou números de documentos em conversas com IA.
- Em empresas, defina que ferramentas de IA podem ser usadas e com que tipo de dados.
- Prefira serviços com políticas de privacidade claras e evite aplicações desconhecidas que prometem «IA grátis».
- Trate tudo o que escreve numa IA como se pudesse um dia ser lido por outra pessoa.
