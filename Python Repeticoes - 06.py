# IVO NUNES
# Exercicio de Fixacao - Repeticoes
## Questao 06 - Escreva um programa que imprima na tela a serie de Fibonacci ate o decimo quinto termo.

a = 1
b = 1
print (a)
print (b)

for i in range (3, 16):
        c = a + b
        print (c)
        a = b
        b = c
