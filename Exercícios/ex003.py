#Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos 
#correspondem aos valores esperados determinados por você.

nome_admin = 'admin'
senha_admin = 'admin'

nome_usuario = str(input("Digite seu nome: "))
senha_usuario = str(input("Digite uma senha: "))

if nome_usuario == 'admin' and senha_admin == 'admin':
    print("Credenciais corretas")
else:
    print("Credenciais inválidas")