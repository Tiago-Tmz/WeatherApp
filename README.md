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

É necessário ter o Python instalado no sistema. As dependências estão listadas em `requirements.txt`.

Instale-as com:

```
pip install -r requirements.txt
```

### Segurança da chave da API

Não inclua a sua chave de API diretamente no código. Defina a variável de ambiente `OPENWEATHER_API_KEY` ou crie um ficheiro `.env` com a linha:

```
OPENWEATHER_API_KEY=suachaveaqui
```

O script carrega automaticamente variáveis de um `.env` quando presente.

## Como Executar

1. Abra o terminal e navegue até à pasta do projecto.
2. Defina a variável de ambiente `OPENWEATHER_API_KEY` ou crie um `.env` como indicado acima.
3. Execute o script com:

```
python script.py
```

## Tecnologias

* Python 3
* Biblioteca Requests
* API do OpenWeatherMap