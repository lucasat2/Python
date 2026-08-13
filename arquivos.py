
#%%  LER
nome_arquivo = "historia.txt"

with open(nome_arquivo) as open_file:
    conteudo = open_file.read()
print(conteudo)


# %%   ESCREVER
txt = "Meu novo arquivo de texto\n"

nome_arquivo = "historia_02.txt"

with open(nome_arquivo, mode="a") as open_file:
    open_file.write(txt)
# %%
