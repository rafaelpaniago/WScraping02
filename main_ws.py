import requests

url = "https://raw.githubusercontent.com/kelvins/municipios-brasileiros/refs/heads/main/csv/municipios.csv"

response = requests.get(url)

if response.status_code == 200:
    textoResposta = response.text
    textoEmLinhas = textoResposta.splitlines()
    header = textoEmLinhas[0].split(',')

    todos_os_dados = []


    for linha in textoEmLinhas[1:]:
        valores = linha.split(',')

        dicionario_dados = {header[i]: valores[i] for i in range(len(header))}
        todos_os_dados.append(dicionario_dados)
    
    lista_capitais = []
    contador = 1
    
    for linha_de_todos_os_dados in todos_os_dados:
        if linha_de_todos_os_dados['capital'] == '1':
            linha_de_todos_os_dados['id'] = contador
            # PRONTO. ATÉ AQUI, A BASE ESTÁ COMPLETA. COM ID.

            linha_de_todos_os_dados = {'id': linha_de_todos_os_dados['id'], **linha_de_todos_os_dados}
            # AQUI ORDENAMOS PARA O ID SER O PRIMEIRO VALOR.

            lista_capitais.append(linha_de_todos_os_dados)
            contador += 1
    
    print(lista_capitais)

        
