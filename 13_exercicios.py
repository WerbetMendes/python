# Solicite ao usuário o nome de uma fruta e exiba o preço correspondente.
# Obviamente, devemos evitar fazer muitos if.
# %%
fruta = input("Digite a fruta desejada:")

frutas = {
    "Pera": "R$1,15",
    "Goiaba": "R$2,15",
    "Abacaxi": "R$3,20",
    "Jaca": "R$5,80",
    "Laranja": "R$0,65",
    "Limão": "R$1,25",
    "Maçã": "R$1,50",
    "Banana": "R$2,75",
    "Uva": "R$1,90",
}

if fruta in frutas:
    print(frutas[fruta])
else:
    print("Desculpe, essa fruta está em falta!")
# %%
# Escreva um programa que solicite ao usuário frases. Para parar de solicitar 
# frases, ele pode apenas apertar o "enter".
# Seu programa deve apresentar cada frase e quantas vezes ela foi repetida.
frases = {}

while True:
    frase = input("Digite sua frase: ")
    if frase == "":
        break

    if frase not in frases:
        frases[frase] = 1
    else:
        frases[frase] += 1

for i in frases:
    print(i, "->", frases[i])

# %%
