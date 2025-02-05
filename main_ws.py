import requests

url = "https://raw.githubusercontent.com/kelvins/municipios-brasileiros/refs/heads/main/csv/municipios.csv"

response = requests.get(url)

if response.status_code == 200:
    responseText = response.text
    linesplit = responseText.splitlines()
    header = linesplit[0].split(',')