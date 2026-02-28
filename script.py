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
            print("-"**30 + "\n")
        else:
            print("\nErro: Cidade não encontrada ou chave de API inválida.")

    except requests.exceptions.RequestException as e:
        print(f"\nErro de ligação. Detalhes: {e}")

if __name__ == "__main__":
    print("Bem-vindo à App de Meteorologia!")
    while True:
        cidade_input = input("Escreve o nome de uma cidade (ou 'sair' para fechar): ")
        
        if cidade_input.lower() == 'sair':
            print("Até logo!")
            break
            
        obter_tempo(cidade_input)