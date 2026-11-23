---
titulo: "Drupal corrige falha grave que expõe sites"
resumo: "O Drupal, usado em muitos sites de governos e empresas, corrigiu uma falha no instalador que permite assumir o controlo do site. Já há código de demonstração público."
data: 2026-11-20
nivel: ALTO
tema: ciberseguranca
ilustracao: cadeia
caixa: O QUE FAZER
acao: "Quem gere sites em Drupal deve actualizar para as versões 10.6.22, 11.3.22 ou 11.4.13 e confirmar que o instalador não está acessível."
fontes:
  - nome: "BleepingComputer: Drupal patches critical RCE flaw, warns exploits may surface quickly"
    url: https://bleepingcomputer.com/news/security/drupal-patches-critical-rce-flaw-warns-exploits-may-surface-quickly
  - nome: "The Hacker News: Drupal patches critical installer flaw"
    url: https://thehackernews.com/2026/11/drupal-patches-critical-installer-flaw.html
  - nome: "SecurityOnline: CVE-2026-132165, Drupal core"
    url: https://securityonline.info/cve-watchtower/cve-2026-132165/
---
A equipa do Drupal, um dos sistemas mais usados para criar sites de governos, universidades e grandes empresas, publicou a 18 de Novembro uma correcção para uma falha grave no instalador (CVE-2026-132165). A falha pode permitir a um atacante executar comandos no servidor e assumir o controlo do site. O Drupal classificou-a com 18 pontos em 25 na sua escala de risco, o que corresponde a «crítico».

## Onde está o problema

Quando se cria um site em Drupal, corre-se um assistente de instalação, o ficheiro install.php. Em condições normais, depois de o site estar montado, esse instalador deixa de ter utilidade. A falha está precisamente aí: em certas configurações, o instalador continua acessível e pode ser usado por um estranho para correr código no servidor.

A equipa do Drupal corrigiu o problema nas versões 10.6.22, 11.3.22 e 11.4.13 e avisou que os ataques podem surgir depressa, porque a falha é relativamente simples de explorar.

## Já há código público

Pouco depois do aviso, apareceu na internet um código de demonstração (prova de conceito) que mostra como aproveitar a falha. Até 20 de Novembro não havia ataques confirmados, mas a experiência mostra que, quando um código destes fica público, os hackers começam a procurar sites vulneráveis em poucas horas ou dias.

O Drupal já teve falhas muito exploradas no passado, como a conhecida Drupalgeddon, em 2018, que levou à invasão de milhares de sites para minerar moedas digitais e espalhar programas maliciosos.

## Quem está em risco

Estão em risco os sites em Drupal que não tenham sido actualizados e em que o instalador continue acessível a partir da internet. O risco é maior para sites antigos, montados há anos e sem manutenção regular.

Para o visitante comum, não há nada a fazer. Mas um site invadido pode passar a mostrar páginas falsas, redireccionar para burlas ou espalhar vírus, por isso vale a pena desconfiar de comportamentos estranhos em sites conhecidos.

## O que fazer

Os responsáveis por sites em Drupal devem:

- actualizar já para uma das versões corrigidas;
- confirmar que o ficheiro install.php não está acessível a partir da internet;
- rever os registos do servidor à procura de acessos ao instalador desde 18 de Novembro.

Em Angola, várias instituições e empresas usam Drupal nos seus portais. Esta é uma actualização que não deve esperar.
