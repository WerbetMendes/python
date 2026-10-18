# %%
nome = "Werbet Mendes"

for letra in nome:
    print(letra)
# %%
numero = 2
max_numero = 100

for i in range(1, max_numero+1):
    print(numero, "x", i, "=", numero * i)
# %%
# Quais números são divisíveis por 4 no intervalo de 4 a 100?

for i in range(4, 101):
    if i % 4 == 0:
        print(i)
# %%
soma = 0
entradas = 4

for i in range(entradas):
    altura = input("Entre com a altura: ")
    altura = float(altura)
    soma += altura

print("Soma das alturas:", soma)
# %%
