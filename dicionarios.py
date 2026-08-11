#%%
dados = {
    "nome":"Lucas",
    "sobrenome":"Ataide",
    "filhos":"False",
    "formacao":["estatistica","bigdata datascience"],
    "cargos":[
        {"nome":"ds jr.","empresa":"tapps"},
        {"nome":"ds pl.","empresa":"sas"},
        {"nome":"ds sr.","empresa":"boticario"},
        {"nome":"ds espec.","empresa":"via varejo"}
    ]
}
#%% #ULTIMA EMPRESA TRABALHADA
dados["cargos"][-1]["empresa"]

# %% #ADICIONAR NOVA CHAVE
dados["estado civil"] = "Solteiro"

# %% #COMO SABER QUAIS SAO OS NOMES DAS CHAVES E VALORES DO DICIONARIO

dados.keys() 
dados.values()
dados.items()
# %% #PERCORRER UM DICIONARIO
#  
for chave,valor in dados.items():
    print(chave,"->",valor)