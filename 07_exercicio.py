# Faça um programa que vende uma garrafa de água:
# a) Se o cliente escolher água mineral natural, será cobrado R$1,50
# b) Se o cliente escolher água mineral com gás, será cobrado R$2,50

# %%
texto = """"
Escolha sua água:
(1) Água mineral natural
(2) Água mineral com gás
"""

opcao = input(texto)

if opcao == "1":
    print("A água custa R$1,50")
elif opcao == "2":
    print("A água custa R$2,50")

else:
    print("Entre com a opção correta")
# %%
