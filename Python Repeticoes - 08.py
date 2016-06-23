# IVO NUNES
# Exercicio de Fixacao - Repeticoes
## Questao 08 - Elaborar um programa que calcule o somatorio do numero de graos de trigo que se pode obter no tabuleiro de xadrez.

a = 0
b = 1
trigo = 0

for i in range (2, 65):
        a = b
        b = b * 2
        trigo = trigo + b

print (trigo, "Graos de Trigo")
