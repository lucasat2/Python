
"""                               DICIONÁRIOS                                                    """


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

#----------------------------------------------------------------------------------------


"""                                TUPLAS                                                    """

# TUPLA É UMA LISTA IMUTAVEL 
#%%
tupla = (32,1,"solteiro","dev_golang")
type(tupla)

#Nao pode fazer isso 
tupla [-1] = ["a","b"]

#Porém se tiver uma lista dentro, consigo mexer nela, que é mutavel.
#_____________________________________________________________

#%%
# EXERCICIOS DE TUPLAS

""" Escreva um programa que crie um dicionário com
nomes de frutas como chaves e seus respectivos
preços como valores. Solicite ao usuário o nome
de uma fruta e exiba o preço correspondente.

"""

fruta = input("Digite a fruta")

frutas = {
"Pera": "R$1,25",
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
    print("Entre com um valor válido!")

#%% Exercicio 2 
"""
Escreva um programa que solicite ao usuário
frases. Para parar de solicitar frases, ele pode
apenas apertar o "enter".

Seu programa deve apresentar cada frase e
quantas vezes ela foi repetida.
"""
frases = { }

while True:
    frase = input("Entre com a frase: ")
    if frase == "":
        break

    if frase not in frases:
        frases[frase] = 1
    else:
        frases[frase] += 1 
    
for chave, valor in frases.items():
    print(chave,"->",valor)      

#------------------------------------------------------
#                   FUNCOES

