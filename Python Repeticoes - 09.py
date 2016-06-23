# IVO NUNES
# Exercicio de Fixacao - Repeticoes
## Questao 09 - Elabore um programa que efetue a leitura sucessiva de valores numericos e apresente no final o total do somatorio.

n = 0
soma = 0
totaln = 0
media = 0
float (media)

while (n >= 0):
    n = int(input(" Insira um numero: "))
    soma = (soma + n)
    totaln = totaln + 1
    media = soma/totaln
    print (" Total ------------------------: %d " %soma)
    
    print (" Media -----------------------: %.2f " %media)
    
    print (" Valores Inseridos -------: %d " %totaln)
    if (n < 0):
        break
    
        
