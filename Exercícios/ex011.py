# 7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, 
# caso a lista esteja vazia.

import os 
os.system('cls')

numeros = []
soma = 0 

while True:
        numero_usuario = input("Digite um número inteiro (para sair deste loop, digite sair): ")

        if numero_usuario.lower() == 'sair':
                break
        try:
               numero_convetido = int(numero_usuario)
               numeros.append(numero_convetido)
                     
        except ValueError:
                print("Digite somente números.")

for numero in numeros:
    soma += numero
try:
       resultado = soma / len(numeros)
       print(f"A média dos números é: {resultado}")
except:
       print("Não é possível fazer a divisão por zero.")