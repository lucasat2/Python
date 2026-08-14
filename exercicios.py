# Faça um programa que de bom dia: 

#%% 
print("Bom dia")

# %%
''' Faça um programa que de bom dia,
 pergunta o nome da pessoa e
 responde que é um prazer conhecer ela,
 citando o nome da pessoa.
 '''
print("Bom dia")

nome = input("Qual é o seu nome? ")

print("É um prazer te conhecer,",nome)

# %%
# Crie uma história simples.
# A cada parágrafo, a história deve aguardar o usuário apertar "enter" para dar continuidade.

input("Era uma vez uma pessoa muito feliz. Ela descubriu a área da programação.")

input("E assim, ela deixou de ser feliz.")

input("Mas ela conheceu a área de dados e voltou e ficar bem feliz !! ")

input("Então, moral da história. A aleatoriedade te leva para algo inesperado.")


# %%
# Faça um programa que receba um número inteiro e calcule sua raiz quadrada e exiba o resultado.

numero = int(input("Entre com um número inteiro: "))
raiz = numero ** 0.5 
print(raiz)

# %%
# Faça um programa que exiba o dobro de um número inserido pelo usuário.

numero = float(input("Entre com um numero: "))

dobro = numero * 2

print("O dobro de", numero, "é:", dobro)

# %%
# Peça ao usuario o tipo de agua mineral, a quantidade e imprima o valor total.

tipo = input("Escolha um tipo de água: (1) Água Mineral Natural / (2) Água Mineral com Gás ")
qtde = int(input("Qual a quantidade de garrafas? "))

if tipo == "1":
    valor = 1.5 * qtde
    print("Total: R$", valor)

elif tipo == "2":
    valor = 2.5 * qtde
    print("Total: R$", valor)

else:
    print("Entre com dados válidos!")


# %%
# Faça o programa de uma sorveteria, onde o usuário pode escolher:
# Tipo de sorvete: casquinha (R$1,00), cascão (R$2,50), cestinha (R$4,00)
# Sabor do sorvete: morango, creme, chocolate
# Cobertura: Caramelo (R$1,50), morango (R$1,50), chocolate (R$1,50), sem cobertura (R$0,00)
# Apresente o valor a ser pago

tipo = input("Entre com o tipo o sorvete: [Casquinha (R$1,00) / Cascão (R$2,50) / Cestinha (R$4,00)] ")
tipo = tipo.lower()

sabor = input("Escolha o seu sabor: [Morango / Creme / Chocolate] ")
sabor = sabor.lower()

cobertura = input("Escolha a cobertura: [Caramelo (R$1,50) / Morango (R$1,50) / Chocolate (R$1,50) / Sem cobertura (R$0,00)]")
cobertura = cobertura.lower()

valor = 0
if tipo == "casquinha":
    valor += 1
elif tipo == "cascão":
    valor += 2.5
elif tipo == "cestinha":
    valor += 4 

if cobertura in ["caramelo", "morango", "chocolate"]:
    valor += 1.5

txt = f"Seu sorverte {tipo} de {sabor} com cobertura de {cobertura} custou R${valor :. 2f}"
print(txt)


# %%
# Faça um programa que verifique se a pessoa pertence à família "calvo" ou "silva".

nome = input("Entre com seu nome completo: ")
nome_split = nome.lower().split(" ")

if "calvo" in nome_split: # "teo calvo" -> ["teo", "calvo"]
    print("Essa pessoa é Calvo")

if "silva" in nome_split: # silvana calvo -> ["silvana", "calvo"]
    print("Essa pessoa é Silva")

if "silva" not in nome_split and "calvo" not in nome_split:
    print("Essa pessoa não é Silva, nem Calvo")


# %%
# Faça um programa que conte quantas vezes a letra "a" aparece em uma palavra

palavra = input("Entre com uma palavra: "). lower()
count = 0

for letra in palavra:
    if letra == "a":
        count += 1

print(f"A palavra '{palavra}' tem {count} 'a'.")

# %%  Forma 2 

palavra = input("Entre com uma palavra: ").lower()
count = palavra.count("a")

print(f"A palavra '{palavra}' tem {count} 'a'.")

# %%

# Faça um programa que receba 4 alturas
# usando um laço de repetição e realize a soma dessas alturas.

soma = 0 
for i in range(4):
    altura = float(input("Entre com a altura: "))
    soma += altura
    
print ("A soma das altura é:", soma)
# %%
# Faça um programa que receba uma quantidade indefinida de valores
# correspondentes a "saldo em conta",
# mas quando o usuário apertar "enter" sem digitar valor algum,
# o programa para de receber valores, e exibe a soma de todos os
# valores digitados anteriormente.

soma = 0

while True:
    entrada = input("Entre com um valor: ")
    if entrada == "":
        break

    soma += float(entrada)

print(f"A soma total dos valores é: R${soma}")


# %%
