---
titulo: "Hackers infectam routers da GL.iNet pela nuvem"
resumo: "Uma falha no GoodCloud, o serviço de gestão remota da GL.iNet, foi usada para instalar programas maliciosos em routers e aparelhos KVM. A empresa lançou nova versão do sistema a 22 de Novembro."
data: 2026-11-22
nivel: ALTO
tema: ciberseguranca
ilustracao: firewall
caixa: O QUE FAZER
acao: "Quem tem router ou KVM da GL.iNet deve actualizar o sistema e, se não usar a gestão remota GoodCloud, desligá-la."
fontes:
  - nome: "BleepingComputer: Hackers exploit GL.iNet cloud flaw to infect routers, KVM devices"
    url: https://www.bleepingcomputer.com/news/security/hackers-exploit-glinet-cloud-flaw-to-infect-routers-kvm-devices/
  - nome: "GL.iNet Forum: 2026-11-20 GL.iNet Security Notice, GoodCloud / KVM / Routers"
    url: https://forum.gl-inet.com/t/2026-11-20-gl-inet-security-notice-goodcloud-kvm-routers/73056
  - nome: "SC Media: GL.iNet confirms cloud vulnerability led to router and KVM malware infections"
    url: https://www.scworld.com/brief/gl-inet-confirms-cloud-vulnerability-led-to-router-and-kvm-malware-infections
---
A GL.iNet, fabricante chinesa de routers portáteis e de aparelhos para controlar computadores à distância (KVM), confirmou que hackers usaram uma falha no seu serviço de gestão na nuvem, o GoodCloud, para instalar programas maliciosos em aparelhos de clientes. O aviso foi publicado no fórum oficial a 20 de Novembro, e uma nova versão do sistema dos aparelhos (firmware) saiu a 22 de Novembro.

## O que é o GoodCloud

O GoodCloud permite gerir os routers e os KVM da GL.iNet a partir de qualquer lugar: ver o estado, mudar configurações e aceder à rede de casa ou do escritório sem estar lá. É prático, mas cria um risco: se o serviço na nuvem for comprometido, todos os aparelhos ligados a ele podem ser atingidos ao mesmo tempo.

Foi o que aconteceu. Através da falha, os atacantes conseguiram enviar comandos para aparelhos de clientes e instalar neles programas maliciosos. Segundo a GL.iNet, a maioria dos aparelhos afectados tinha activa a função de acesso remoto RemoteToHome: 152 dos 183 casos identificados.

## Porque os routers são alvos

Um router infectado é muito valioso para os hackers. Fica ligado 24 horas por dia, raramente é vigiado e vê todo o tráfego da rede. Pode ser usado para espiar, para entrar noutros aparelhos da casa ou da empresa, ou para fazer parte de redes de aparelhos controlados à distância, usadas em ataques maiores.

No caso dos KVM, o risco é ainda maior: estes aparelhos dão controlo total do teclado, do rato e do ecrã de um computador, como se a pessoa estivesse sentada à frente dele.

## O que fazer

Para quem tem aparelhos GL.iNet:

- actualize o firmware para a versão mais recente, publicada a 22 de Novembro;
- se não usa o GoodCloud ou o RemoteToHome, desligue-os nas definições;
- mude a senha de administração do aparelho;
- se suspeitar de infecção, faça a reposição de fábrica e configure tudo de novo.

Os routers portáteis da GL.iNet são populares entre quem viaja ou trabalha à distância, incluindo em Angola. A falha não tem código CVE porque foi corrigida no serviço da própria empresa.
