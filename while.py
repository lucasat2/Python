#%%
texto ="""
Escolha a sua água para comprar
(1) Água mineral natural
(2) Água mineral com gás
"""
#%%
numero = 2
count = 1

while count <= 100:
    print(numero, "X", count, "=", numero * count)
    count += 1 # count = count + 1

print("Acabou !! ")
#_

#%%
                          #Soma de 4 alturas while

soma = 0
count = 4 

while count > 0: 
    altura = input("Digite a altura")
    altura = float(altura)
    soma += altura 
    count-=1

print("A soma das alturas é:", soma)

#%%
                        #Pausar o while ao apertar enter e somar o saldo

saldo_total = 0 

while True:
    saldo = input("Digite um valor: ")
    if saldo == "":
        break
    saldo_total += float(saldo)
    
print("A soma do saldo é ", saldo_total)
    