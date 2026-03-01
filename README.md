# WeatherApp

Aplicação de linha de comandos em Python para consulta de condições meteorológicas em tempo real, utilizando a API do OpenWeatherMap.

## Funcionalidades

* Consulta da temperatura atual e descrição do estado do tempo de uma determinada cidade.
* Opção para visualizar detalhes adicionais da previsão, incluindo:
  * Sensação térmica, temperatura mínima e máxima.
  * Humidade e pressão atmosférica.
  * Velocidade, direção e rajadas do vento.
  * Cobertura de nuvens.
  * Horário do nascer e do pôr do sol (em UTC).
* Permite a pesquisa contínua de diferentes cidades ou o encerramento da aplicação através de comandos simples.

## Pré-requisitos

É necessário ter o Python instalado no sistema. O script requer a biblioteca 'requests'g para efetuar as chamadas à API.

Para instalar as dependências necessárias, execute o seguinte comando no terminal:

pip install requests

## Como Executar

1. Transfira o ficheiro Python para o seu computador.
2. Abra o terminal e navegue até à pasta onde o ficheiro se encontra.
3. Execute o script com o comando:

python script.py

*(Nota: Certifique-se de que o nome do ficheiro corresponde ao que guardou).*

## Tecnologias

* Python 3
* Biblioteca Requests
* API do OpenWeatherMap