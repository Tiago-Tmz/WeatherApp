import requests

def obter_tempo(cidade):
    api_key = "de8898ac913d6229e6318239e4e47290" 
    
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&units=metric&lang=pt"

    try:
        resposta = requests.get(url)
        dados = resposta.json()

        if resposta.status_code == 200:
            temperatura = dados['main']['temp']
            descricao = dados['weather'][0]['description']
            
            print("\n" + "-"*30)
            print(f"Tempo atual em {cidade.capitalize()}:")
            print(f"Temperatura: {temperatura}ºC")
            print(f"Descrição: {descricao.capitalize()}")
            print("-"*30 + "\n")
            escolha = input("Escreva '1' para ver todos os detalhes meteorológicos da cidade : " + cidade.capitalize() + ", 'sair' para fechar ou outra cidade para consultar: ")
            if escolha == "1":
                main = dados.get('main', {})
                wind = dados.get('wind', {})
                sys = dados.get('sys', {})

                from datetime import datetime, timezone
                fmt = lambda ts: datetime.fromtimestamp(ts, timezone.utc).strftime('%H:%M:%S') if ts else 'N/A'

                print(f"\n--- Detalhes meteorológicos de {cidade.capitalize()} ---")
                if 'feels_like' in main:
                    print(f"Sensação térmica: {main['feels_like']}ºC")
                if 'temp_min' in main and 'temp_max' in main:
                    print(f"Temperatura mínima/máxima: {main['temp_min']}ºC / {main['temp_max']}ºC")
                if 'pressure' in main:
                    print(f"Pressão: {main['pressure']} hPa")
                if 'humidity' in main:
                    print(f"Humidade: {main['humidity']}%")
                if 'speed' in wind:
                    print(f"Vento: {wind['speed']} m/s")
                if 'deg' in wind:
                    print(f"Direção do vento: {wind['deg']}°")
                if 'gust' in wind:
                    print(f"Rajada: {wind['gust']} m/s")

                print(f"Nuvens: {dados.get('clouds', {}).get('all', 'N/A')}%")

                if 'sunrise' in sys:
                    print(f"Nascer do sol: {fmt(sys['sunrise'])} UTC")
                if 'sunset' in sys:
                    print(f"Pôr do sol: {fmt(sys['sunset'])} UTC")

                print("" + "-"*30 + "\n")
                return None
            if escolha.lower() == 'sair':
                return 'sair'
            return escolha
        else:
            print("\nErro: Cidade não encontrada ou chave de API inválida.")

    except requests.exceptions.RequestException as e:
        print(f"\nErro de ligação. Detalhes: {e}")

if __name__ == "__main__":
    print("Bem-vindo à App de Meteorologia!")
    cidade_input = None
    while True:
        
        if not cidade_input:
            cidade_input = input("Escreve o nome de uma cidade (ou 'sair' para fechar): ")

        if cidade_input.lower() == 'sair':
            print("Até logo!")
            break

        resultado = obter_tempo(cidade_input)
        if resultado == 'sair':
            print("Até logo!")
            break
        if resultado:
            cidade_input = resultado
            continue
        cidade_input = None 