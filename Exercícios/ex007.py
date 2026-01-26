#3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.

numeros = [1,2,3,4,5,6,7,8,9,10]
soma = 0
for numero in numeros:
    resultado_inicial = numero%2
    if resultado_inicial == 1:
        soma += numero

print(f"A soma dos números ímpares é: {soma}")
