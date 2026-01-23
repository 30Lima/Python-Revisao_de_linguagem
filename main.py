import os

def exibir_nome_do_programa():
    os.system("cls")
    print("""
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
    """)

restaurantes = []

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def adicionar_restaurante():
    os.system("cls")
    print("Cadastro de novos restaurantes\n")
    nome_restaurante = input("Digite o nome do restaurante: \n")
    restaurantes.append(nome_restaurante)
    input("Digite qualquer tecla para voltar ao menu principal: ")
    main()


def finalizando_app():
    os.system("cls")
    print("Encerrando o programa\n")

def opcao_invalida():
    print("Opção inválida\n")
    input("Digite uma tecla para voltar ao menu principal")

def escolher_opcao():
    opcao_escolhida = int(input('Escolha uma opção: \n'))

    try:
        if opcao_escolhida == 1:
            adicionar_restaurante()
        elif opcao_escolhida == 2:
            print("Listar restaurantes")
        elif opcao_escolhida == 3:
            print("Ativar restaurante")
        elif opcao_escolhida == 4:
            print("Sair do sistema")
        else:
            finalizando_app()
    except:
        opcao_invalida()
    

def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()