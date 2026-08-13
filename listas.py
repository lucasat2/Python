#%%

           #LIST COMPREHENSION

y = [i for i in range(1,101)]
y

# %%

#Lista para saber se o numero é par ou não.

def eh_par(x):
    return x % 2 == 0 

z = [eh_par(i) for i in range (1,101)]
z

# %%
# Somente os numeros de 1 a 100 pares

w = [i for i in range (1,101) if eh_par(i)]
w

               #UNPACK   
# %%
A = 5
B = 6
# %%
B, A = A, B

# %%
a, b, *resto = 1, 2, 3, 4,4,5,6,643, 23, 34, 2342
print(a,b, resto)


# %%

*resto, a, b = 1, 2, 3, 4,4,5,6,643,23,34,2342
print(a,b, resto)


# %%

a, *resto, b = 1, 2, 3, 4,4,5,6,643,23,34,2342
print(a,b, resto)

# %%
