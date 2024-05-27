'''
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:

Fatorial de: 5

5! = 5 . 4 . 3 . 2 . 1 = 120
'''
string_saida = ""
def fatorial(n):
    string_saida = f'{n}! = {n} . '
    fat = 1
    while n>1:
        fat *= n
        n -= 1
        string_saida += f'{n} . '
    string_saida = string_saida[:-2]
    string_saida += f' = {fat}'
    print(string_saida)


fatorial(5)