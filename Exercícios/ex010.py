# 6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. 
# Utilize um bloco try-except para lidar com possíveis exceções.

try:
    numeros = [1,2,3,4,5,6,7,8,9,10]
    soma = 0 
    for numero in numeros:
        soma += numero
except:
    print("Somente números")

print(soma)