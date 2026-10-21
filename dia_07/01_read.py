# %%

nome_arquivo = "historia.txt"
# open_file = open(nome_arquivo)

# A maneira mais prática e usual é esta:
with open('historia.txt', 'r', encoding='utf-8') as f:
    conteudo = f.read()
    print(conteudo)

# with: Context manager que garante que o arquivo será fechado ao sair do bloco, mesmo se ocorrerem erros.
# open(file, mode, encoding): função integrada para abrir o arquivo.
# 'r': Modo de abertura para leitura (read).
# encoding='utf-8': Parâmetro recomendado para ler acentos e caracteres especiais corretamente.
# as f: Apelido (variável) que representa o objeto do arquivo.


# %%
# Abre o arquivo em formato de leitura.
#print(open_file)
# %%
# Lê os dados e exibe o arquivo.
# conteudo = open_file.read()
# print(conteudo)
# %%
# Fecha o arquivo.
# open_file.close()
# %%
