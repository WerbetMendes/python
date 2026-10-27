# %%
import requests
import json
from tqdm import tqdm
import pandas as pd


# %%
ceps = [
    "01519000",
    "13329120",
    "21870370",
    "14400760",
    "21645522",
    "13600110",
    "21051090",
    "09656000",
    "53420160",
    "01311902",
]

url = "https://viacep.com.br/ws/{cep}/json"
dados = []

for i in tqdm(ceps):
    resposta = requests.get(url.format(cep=i))
    if resposta.status_code == 200:
        dados.append(resposta.json())

dados
# %%
dataset = pd.DataFrame(dados)
dataset


# %%
with open("ceps.json", "w", encoding='utf-8') as open_file:
    json.dump(dados, open_file, ensure_ascii=False, indent=4)

# Repositório Github - Public APIs