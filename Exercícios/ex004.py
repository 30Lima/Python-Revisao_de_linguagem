#4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para 
# determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:

#Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
#Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
#Terceiro Quadrante: os valores de x e y devem ser menores que zero;
#Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
#Caso contrário: o ponto está localizado no eixo ou origem.

import os
os.system("cls")

valor_x = int(input("Digite o valor de x: "))
valor_y = int(input("Digite o valor de y: "))

if valor_x > 0 and valor_y > 0:
    print("Primeiro Quadrante")

elif valor_x < 0 and valor_y > 0:
    print("Segundo Quadrante")

elif valor_x < 0 and valor_y < 0:
    print("Terceiro Quadrante")

elif valor_x > 0 and valor_y < 0:
    print("Quarto Quadrante")

else:
    print("O ponto está localizado no eixo ou origem")