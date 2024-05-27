#Peça ao usuário para digitar 5 números e adicione a uma lista.

lista = []
print ('Informe os 5 numeros')
for i in range(5):
    lista.append(input('Numero '+ str(i+1) + ':\n'))
print(lista)