#1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.
opcao_usuario = int(input("Insira um número: "))

calculo = opcao_usuario % 2

if calculo == 0:
    print("O número é par")
else:
    print("O númmero é ímpar")

