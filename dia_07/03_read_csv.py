# %%
arquivo = "data.csv"

with open(arquivo) as f:
    lines = f.readlines()

print(lines)
# %%
# Percorrer linhas da tabela
for l in lines:
    print(l)
# %%
# strip: remove espaços em branco e quebras de linha no início e no fim de uma string.
# split: transforma uma string em uma lista de sub-strings, utilizando um separador específico.
chaves = lines[0].strip().split(";")
chaves
# %%
dados = dict()

chaves = lines[0].strip().split(";")
for c in chaves:
    dados[c] = []

dados
# %%
for l in lines[1:]:
    valores = l.strip().split(";")
    for i in range(len(valores)):
        dados[chaves[i]].append(valores[i])

dados
# %%
# Para saber a média de idades
idades = []
for i in dados["idade"]:
    idades.append(int(i))

media = sum(idades)/ len(idades)
media
# %%
