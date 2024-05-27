#Faça um Programa que leia uma lista de 10 caracteres, e diga quantas consoantes foram lidas.
#Imprima as consoantes.

listaConsoantes= []
consoantes = 0
print ('Informe os caracters')
for i in range(10):
	char = input('Caracter  '+ str(i+1) + ':\n')
	if (char not in ('a','e','i','o','u')):
		consoantes += 1
		listaConsoantes.append(char)

	
print(f'Total de consoantes {consoantes}')
print(listaConsoantes)