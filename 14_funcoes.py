# %%
def f(x):
    return 1 + x

# %%
f(5)
# %%
# Definimos uma função através da palavra reservada def.
# Opcionalmente, definimos os parâmetros e podemos dar dicas de quais tipos a função espera.
# Também podemos definir o retorno, embora o python já faça isos após definirmos os tipos.
# Podemos documentar o que a função faz por meio de três aspas duplas.
def juros_compostos(aporte:int, taxa:float, anos:int)->float:
    """"Juros_compostos serve para calcular o retorno financeiro sobre um investimento.
Deve-se considerar o valor, a taxa de juros atual e o tempo (anos).

aporte:
    um número inteiro, que representa o valor em R$.

taxa:
    um número float entre 0 e 1 que represente o valor taxa de juros.

anos:
    um número inteiro >= 1 que representa o tempo que o investimento terá liquidez.
    
    """
    return aporte * (1 + taxa) ** anos

juros_compostos(200, 0.13, 5)
# %%
