# %%

def juros_compostos(aporte:int, taxa:float, anos:int)->float:
    """ juros compostos servem para calcular o retorno financeiro pos um aporte. deve se considerar a taxa de juros atual e o tempo em anos para calculo do valor retornado.

    aporte: um numero inteiro que represente o valor em reais 
    taxa : um numero float  entre 0 e 1 que represente o valor da taxa
    anos: um numero inteiro maior ou igual a 1 que representa o tempo que o investimento tera liquidez.
    """
    return aporte * (1 + taxa) ** anos

juros_compostos(aporte=1000,taxa=0.13, anos=5)


#%% 
def ola_mundo():
 print("Boas vindas!")
 
#%% 
ola_mundo()

#%%  #EXERCICIOS

  # Função para ver se um numero é par ou impar"""

def par_impar(numero:int) -> None:
  if numero % 2:
    print("É par")
  else:
    print("É impar!")

numero = input("Entre com um número")
numero = int(numero)
par_impar(numero)

# %%
         #FUNCAO DENTRO DE OUTRA FUNCAO
 
def soma(a:float,b:float) -> float:
  return a + b

def media(a:float,b:float) ->float:
  return soma(a,b) / 2

a = float(input("Entre com o valor de a: "))
b = float(input("Entre com o valor de b: "))

print("Média:", media(a,b))

# %%

# DEIXANDO EM ABERTO A QUANTIDADE DE VALORES PARA A FUNCAO

#Precisamos aqui de 2 argumentos obrigatorios e infinitos argumentos opcionais no args


def soma(a:float, b:float, *args)->float:
  valores = [a,b] + list(args)
  return sum(valores)

def media(a:float, b:float, *args)->float:
  return soma(a, b, *args) / (len(args)+2) # + 2 argumentos obrigatorios

a = float(input("entre com o valor de a: "))
b = float(input("entre com o valor de b: "))
c = float(input("entre com o valor de c: "))
d = float(input("entre com o valor de c: "))


# Aqui o valor de c,d está indo pro args, pq a e b sao obrigatorios, o resto é extra


print("Média:", media(a,b,c,d))


# %%                   **KWARGS

"""O KWARGS cria um dicionario com chave e valor que eu posso invocar na hora da chamada da funcao """

def calc_imposto(preco:float, tx_base:float, ** kwargs):
  imposto = preco * tx_base

  for i in kwargs:
    print(i, kwargs[i])
    imposto += preco * kwargs[i]

  return imposto

impostos_gerais = { 
  "municipio":0.01,
  "estadual":0.005,
  "nacional":0.001
}
calc_imposto(100, 0.03,**impostos_gerais )

# %%
