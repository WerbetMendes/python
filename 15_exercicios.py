# Faça um programa que receba um número. 
# Verifique se o número informado é par ou ímpar.
# %%
def par_impar(numero:int):
    if numero % 2 == 0:
        print("O número", numero, "é par")
    else:
        print("O número", numero, "é ímpar")

numero = input("Digite um número: ")
numero = int(numero)

par_impar(numero)
# %%
