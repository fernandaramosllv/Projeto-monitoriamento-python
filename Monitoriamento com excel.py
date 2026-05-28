# Sistema de Cadastro e Monitoramento com Python

# Bibliotecas usadas:
# pip install faker pandas openpyxl beautifulsoup4 requests

from faker import Faker
import pandas as pd
import csv
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import requests

fake = Faker('pt_BR')


# FUNÇÃO PARA GERAR DADOS

def gerar_dados(qtd=10):
    """
    Gera uma lista de registros fictícios.

    Cada registro contém:
    ID, nome, email, idade, cidade e nota.
    """

    dados = []

    for i in range(1, qtd + 1):
        registro = {
            "ID": i,
            "Nome": fake.name(),
            "Email": fake.email(),
            "Idade": fake.random_int(min=18, max=40),
            "Cidade": fake.city(),
            "Nota": round(fake.random.uniform(0, 10), 1)
        }

        dados.append(registro)

    return dados



# SALVAR CSV

def salvar_csv(dados, arquivo="dados.csv"):

    with open(arquivo, mode="w", newline="", encoding="utf-8") as csvfile:

        campos = ["ID", "Nome", "Email", "Idade", "Cidade", "Nota"]

        writer = csv.DictWriter(csvfile, fieldnames=campos)

        writer.writeheader()

        for dado in dados:
            writer.writerow(dado)

    print(f"Arquivo CSV '{arquivo}' criado com sucesso!")



# SALVAR EXCEL

def salvar_excel(dados, arquivo="dados.xlsx"):

    df = pd.DataFrame(dados)

    df.to_excel(arquivo, index=False)

    print(f"Arquivo Excel '{arquivo}' criado com sucesso!")



# SALVAR XML

def salvar_xml(dados, arquivo="dados.xml"):

    raiz = ET.Element("Registros")

    for dado in dados:

        registro = ET.SubElement(raiz, "Registro")

        for chave, valor in dado.items():

            elemento = ET.SubElement(registro, chave)

            elemento.text = str(valor)

    arvore = ET.ElementTree(raiz)

    arvore.write(arquivo, encoding="utf-8", xml_declaration=True)

    print(f"Arquivo XML '{arquivo}' criado com sucesso!")



# LER CSV

def ler_csv(arquivo="dados.csv"):

    print("\n===== DADOS DO CSV =====\n")

    with open(arquivo, mode="r", encoding="utf-8") as csvfile:

        leitor = csv.reader(csvfile)

        for linha in leitor:
            print(linha)



# CALCULAR MÉDIA DAS NOTAS

def calcular_media(dados):

    soma = 0

    for dado in dados:
        soma += dado["Nota"]

    media = soma / len(dados)

    return media



# TAREFA EXTRA
# BeautifulSoup para extrair título de uma página

def extrair_titulo_site():

    url = "https://www.python.org"

    resposta = requests.get(url)

    soup = BeautifulSoup(resposta.text, "html.parser")

    titulo = soup.title.text

    print("\n===== TÍTULO DA PÁGINA =====")
    print(titulo)



# PROGRAMA PRINCIPAL

dados = gerar_dados(10)

salvar_csv(dados)

salvar_excel(dados)

salvar_xml(dados)

ler_csv()

media = calcular_media(dados)

print("\n===== ESTATÍSTICA =====")
print(f"Média das notas: {media:.2f}")

# Executa tarefa extra
extrair_titulo_site()