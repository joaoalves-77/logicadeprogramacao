usuarios = []

while True:
    print("="*30)
    print("Cadastro de usuários")
    print("="*30)
    print("1- Cadastrar usuário")
    print("2- Atualizar Usuário")
    print("3- Deletar Usuário")
    print("4- Listar Usuário")
    print("q - Sair")
    opcao = input("Digite sua opção:")
    
    if opcao == "1":
        nome = input("Digite seu nome:")
        usuarios.append(nome)

    elif opcao == "2":
        pass
            
    elif opcao == "3":
        
    elif opcao == "4":
        pass
    elif opcao == "q":
        pass
    else:
        print("Resposta Inválida")