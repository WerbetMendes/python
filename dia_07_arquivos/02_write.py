# %%
# Esse mode 'w' escreve (arquivo novo) ou sobrescreve tudo (arquivo já criado)
nome_arquivo = "historia_02.txt"

with open(nome_arquivo, 'w', encoding='utf-8') as fw:
    fw.write('Esta é a primeira linha.\n')
    fw.write('Esta é a segunda linha.\n')

# Como já determinamos a variável nome_arquivo, deve ser utilizada sem aspas.
# Também poderíamos colocar todo o texto dentro de um variável txt, por exemplo.
# %%
# Para adicionar texto, precisamos alterar o mode para 'a'.
txt = "Mais uma linha para meu arquivo novo.\n"
with open(nome_arquivo, 'a', encoding='utf-8') as fw:
    fw.write(txt)
    
# %%
