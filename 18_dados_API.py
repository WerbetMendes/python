# %%

import requests

url = "https://viacep.com.br/ws/19060100/json/"
resposta = requests.get(url)
# %%
dados = resposta.json()
dados
# %%
type(dados)
# %%
