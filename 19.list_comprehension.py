# %%
lista_precos = [500, 1500, 2000, 100, 25]
# Caso 1
nova_lista_precos = []
for preco in lista_precos:
    nova_lista_precos.append(preco * 2)
print(nova_lista_precos)

# %%
# Caso 2
nova_lista_precos2 = [preco * 2 for preco in lista_precos]
print(nova_lista_precos2)
# %%
