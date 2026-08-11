#%% Percorrer as letras do nome
 
nome = "Teodoro Calvo"

for letra in nome:
    print(letra)

#%%  Tabuada do 2 

numero = 2 
max_numero = 100

for i in range(1,max_numero + 1):
    print(numero,"x",i, "=", numero * i )


#%% Divisivieis por 4

for i in range(4,101):
    if i % 4 == 0:
        print(i)   
        