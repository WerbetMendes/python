# %%
count = 1
while count <= 10:
    print("Entrei no laço", count)
    count = count + 1
# %%
numero = 2
count = 1
while count <= 100:
    print(numero, "x", count, "=", numero * count)
    count += 1

# %%
# Faça um programa que some a quantidade de alturas inseridas pelo usuário
soma = 0
entradas = 4
while entradas > 0:
    altura = input("Entre com a altura")
    altura = float(altura)
    soma += altura
    entradas -= 1

print("A soma das alturas é:", soma)


# Faça um programa que simule uma conta bancária e receba uma quantidade 
# indefinida de valores. Mas quando o usuário apertar enter, sem digitar valor algum,
# o programa pare e exiba a soma dos valores digitados
# %%
saldo_total = 0
while True:
    saldo = input("Digite o valor do depósito: ")

    if saldo == "":
        break

    saldo_total += float(saldo)

print("O saldo da conta é: ", saldo_total)
# %%
