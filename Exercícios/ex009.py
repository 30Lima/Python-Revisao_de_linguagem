# 5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.
import os 
os.system("cls")
numero_usuario = int(input("Digite um número inteiro: "))

for numero in range(1, 11):
    resultado = numero_usuario * numero
    print(f"{numero_usuario} X {numero} = {resultado}")