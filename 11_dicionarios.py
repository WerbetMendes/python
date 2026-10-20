# Dicionários são conjuntos de pares chave/valor.
# Em outras linguagens como Golang, é conhecido como map.
# Chaves podem ser int e strings. evite float.
# %%
dados_werbet = {"nome": "werbet", "filhos":False, "altura":1.69}
print(dados_werbet)
# %%
# Posso ter um dicionário dentro de uma lista.
dados_werbet = {
    "nome": "werbet", 
    "filhos":False, 
    "altura":1.69,
    "stacks":["PHP", "JavaScript", "SQL"],
    "cargos":[
        {"nome": "progr. junior", "empresa": "MRE3"},
        {"nome": "progr. junior", "empresa": "Veracruz"},
        {"nome": "progr. junior", "empresa": "Werden Viagens"},
    ]
}
print(dados_werbet)
# %%
print(dados_werbet["stacks"][-1])
print(dados_werbet["cargos"][-1]["empresa"])
# %%
dados_werbet["estado civil"] = "casado"
# %%
print(dados_werbet)
# %%
# Como descobrir quais as chaves de um dicionário
print("Chaves: ", dados_werbet.keys())

# %%
print("Valores: ", dados_werbet.values())
# %%
print("Itens: ", dados_werbet.items())
# %%
for chave, valor in dados_werbet.items():
    print(chave, "->", valor)
# %%
