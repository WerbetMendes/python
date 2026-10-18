# %%
# Uma maneira de definir listas
idades = [28, 34, 56, 12, 89, 41]
print(idades)
# %%
# listas não são arrays
werbet = ["Pardo", 43, "Casado", "sem filhos", 1.69]

print(werbet)
# %%
type(werbet)
# %%
#idade
print(werbet[1])
# %%
#altura
print(werbet[4])
# %%
print("soma idades:", sum(idades))
# %%
print("quantidade idades: ", len(idades))
# %%
print("médias das idades: ", sum(idades)/len(idades))
# %%
#Adicionar elementos, pois listas são mutáveis.
idades.append(32)
print(idades)
# %%
