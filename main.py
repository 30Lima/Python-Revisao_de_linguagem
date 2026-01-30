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

restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False}, 
                {'nome':'Pizza Suprema', 'categoria':'Pizza', 'ativo':True},
                {'nome':'Cantina', 'categoria':'Italiano', 'ativo':False}]

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def adicionar_restaurante():
    os.system("cls")
    print("Cadastro de novos restaurantes\n")
    nome_restaurante = input("Digite o nome do restaurante que deseja cadastrar : ")
    categoria = input(f"Digite a categoria do restaurante {nome_restaurante} : ")
    print("Restaurante cadastrado com Sucesso!")
    dados_restaurante = {'nome':{nome_restaurante}, 'categoria':{categoria}, 'ativo':False}
    restaurantes.append(dados_restaurante)
    input("\nDigite qualquer tecla para voltar ao menu principal: ")
    main()

def listar_restaurantes():
    os.system("cls")
    print("Restaurantes cadastrados\n")

    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        situacao_restaurante = restaurante['ativo']
        print(f'- {nome_restaurante} | {categoria_restaurante} | {situacao_restaurante}')
    
    input("\n Digite qualquer tecla para voltar ao menu principal: ")
    main()

def alternando_estado_restaurante():
    print("Alternando estado do restaurante\n")
    nome_restaurante = input("Digite o nome do restaurante que deseja alterar o estado: ")
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O Restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
            input("Digite uma tecla para voltar ao menu principal")
            main()
    if not restaurante_encontrado:
        print("O restaurante não foi encontado\n")
        input("Digite uma tecla para voltar ao menu principal: ")
        main()

def finalizando_app():
    os.system("cls")
    print("Encerrando o programa\n")

def opcao_invalida():
    print("Opção inválida\n")
    input("Digite uma tecla para voltar ao menu principal")
    main()

def escolher_opcao():
    opcao_escolhida = int(input('Escolha uma opção: \n'))

    try:
        if opcao_escolhida == 1:
            adicionar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternando_estado_restaurante()
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