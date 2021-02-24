# Changelog
# 2.0.1
### Fixado
  - Iphakethe não estava apagando pastas usadas no desenvolvimento .git por
  exemplo. 

## [2.0.0]
### Alterado
  - Alterado iphakethe pra estruturar pacotes no arquivo de configuração em vez
  do repositório

## [1.0.6.0]
### Fixado
  - Resolvido problema do iphakethe não conseguir baixar o repositório em portas
  ssh diferentes da 22

## [1.0.5.0]
### Não lançado
  - Criação de novos repositórios pacotes .deb de forma automatizada
  - Interface de administração web

### Features
  - Baixa o código do repositório somente via ssh, empacota usando dpkg e
  envia para o repositório de pacotes .deb dentro de uma estrutura de pastas
  hospedadas pelo apache via reprepro.

### Adicionado
  - Suporte a testes do desenvolvedor sem precisar empacotar o código e
  instalar via apt-get

### Alterado
  - Alterado a estrutura de arquivos do código pra fica contido tudo dentro da
  pasta principal do iphakethe, incluindo arquivo de configuração que agora
  vira um link simbólico em /etc

## [1.0.4.288]
### Adicionado
  - Suporte a portas diferentes da 22
