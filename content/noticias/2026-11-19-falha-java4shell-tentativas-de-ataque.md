---
titulo: Hackers já tentam aproveitar falha grave do Java
resumo: Dois dias depois de ser revelada, a falha do Java conhecida como Java4Shell já é alvo de tentativas de ataque. Ainda não há invasões confirmadas, e a correcção já está disponível.
data: 2026-11-19
hora: "14:00"
nivel: ALTO
tema: ciberseguranca
ilustracao: cadeia
caixa: O QUE FAZER
acao: Quem gere servidores com Java deve instalar já a actualização de Novembro, a começar pelos sistemas ligados à internet. O utilizador comum não precisa de fazer nada.
fontes:
  - nome: "SecurityWeek: Java4Shell exploitation attempts begin as vendors rush out advisories"
    url: https://www.securityweek.com/java4shell-exploitation-attempts-begin-as-vendors-rush-out-advisories/
  - nome: "The Record: CISA issues Java4Shell alert"
    url: https://therecord.media/cisa-issues-java4shell-alert
  - nome: "Cyber Security News: Java4Shell exploitation disguised as Chrome"
    url: https://cybersecuritynews.com/java4shell-rce-flaw-exploited/
---
Na terça-feira, 17 de Novembro, a empresa de segurança Calif revelou uma falha grave no Java, a tecnologia que está por trás de muitos sistemas usados por empresas, bancos e instituições públicas. Dois dias depois, as empresas que vigiam o tráfego da internet já detectaram as primeiras tentativas de ataque. A falha foi baptizada de Java4Shell e tem o código oficial CVE-2026-114938.

## O que é a falha

O problema está na forma como o Java trata um tipo de dados muito comum na internet (a codificação Base64). Um atacante pode enviar dados preparados de propósito para baralhar a memória do programa. No caso mais grave, consegue dar ordens ao servidor sem precisar de senha, ou seja, tomar o controlo da máquina à distância (execução remota de código).

A falha afecta o OpenJDK, a versão aberta do Java, a partir da versão 17.0.6. Há, no entanto, uma condição: só funciona em servidores com processadores Intel ou AMD recentes, que têm uma função de cálculo chamada AVX-512 VBMI. Os sistemas com processadores ARM não são afectados.

## Quem está em risco

Segundo a Calif, o Java é a terceira linguagem de programação mais usada do mundo e está presente em cerca de 90% das 500 maiores empresas dos Estados Unidos. Os investigadores mostraram que é possível atacar, sem senha, programas muito usados nas empresas, como o Jira e o Confluence (da Atlassian), o Jenkins e o Keycloak. Não há, contudo, um ataque único que funcione em todos: cada sistema exige passos diferentes.

Vários fabricantes já publicaram avisos. A Cisco tem mais de uma dezena de produtos afectados e ainda não lançou correcções. A Siemens identificou três produtos industriais e recomenda desligá-los da rede até haver correcção. A Elastic confirmou o problema no Elasticsearch a partir da versão 7.17.3, e a Red Hat classificou a falha como crítica.

## Os primeiros ataques

A GreyNoise, empresa que monitoriza ataques na internet, registou até à manhã de quinta-feira mais de 150 pedidos com a forma de um ataque Java4Shell, vindos de cinco endereços. Nenhum resultou numa invasão nos seus sensores. A Previdian contou nove tentativas, vindas de seis endereços, entre 18 e 19 de Novembro, mas não consegue confirmar se algum alvo foi atingido.

A Cloudflare notou que os atacantes estão a esconder-se. Num dos casos, um endereço fez um primeiro reconhecimento identificando-se como Java4Shell e voltou cerca de 17 horas depois com o ataque, desta vez disfarçado de navegador Chrome. A Cisco diz conhecer código de demonstração, mas não tem notícia de uso malicioso.

## Descoberta com inteligência artificial

A Calif atribui a descoberta aos investigadores Quang Luong e Albert Yang, que usaram inteligência artificial. Segundo a empresa, a falha foi encontrada em cerca de uma hora, e o primeiro ataque funcional ficou pronto em mais duas. O custo total em IA ficou abaixo de 200 dólares. É mais um sinal de que a IA está a acelerar a descoberta de falhas, tanto por quem defende como por quem ataca.

## A correcção já existe

A Oracle e o projecto OpenJDK lançaram a correcção no próprio dia 17, na actualização de Novembro, onde a Oracle deu à falha a nota 8,1 em 10. A Amazon, a Microsoft e a Azul também já disponibilizaram versões corrigidas do Java. A CISA, a agência de cibersegurança dos Estados Unidos, pediu às organizações que instalem a correcção de imediato. Pediu também que verifiquem os programas que trazem o Java incluído lá dentro, a começar pelos que estão ligados à internet.

Para quem ainda não pode actualizar, a Atlassian sugere desactivar temporariamente a função AVX-512 nos produtos instalados nos próprios servidores. Os seus clientes na nuvem não precisam de fazer nada.

## E em Angola?

Bancos, operadoras, empresas e instituições públicas que usam estes sistemas devem confirmar se têm o Java 17 ou mais recente em servidores com processadores Intel ou AMD e actualizar quanto antes. Para o utilizador comum, o risco está nos servidores das empresas e não no telemóvel, por isso não há nada a fazer além de manter os aparelhos actualizados.
