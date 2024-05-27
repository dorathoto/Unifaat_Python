#Faça um Programa que leia uma lista de 10 números reais e mostre-os na ordem inversa.

lista = [1,2,3,4,5,6,7,8,9,10]

print(lista[::-1])

#ou utilizando for
for i in range(10):
    indice = 9 - i
    print(lista[indice])
    
#ou
lista.reverse()
print(lista)

