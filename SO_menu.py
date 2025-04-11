import os

while True:
    os.system('cls')
    menu = int(input("\nCaio Mayan, 20242370036\n\nEscolha uma opção do menu abaixo:\n\n1. Limpar tela\n2. Acessar um diretório\n3. Executar um programa\n4. Ajuda de comandos\n5. Hora atual do sistema\n6. Sair\n"))

    while True:
        if menu == 1:
            os.system('cls')
            print("Tela limpa com sucesso")
            voltar = int(input("\n1. Voltar ao menu\n"))
            if voltar == 1:
                os.system('cls')
                break
        elif menu == 2:
            os.system('cls')
            diretorio = input("Digite o caminho completo de um diretório:")

            try:
                os.system('cls')
                arquivos = os.listdir(diretorio)
                print(f"\nArquivos encontrados em {diretorio}:")
                for arquivo in arquivos:
                    print(arquivos)
                voltar = int(input("\n\n1. Voltar ao menu\n"))
                if voltar == 1:
                    os.system('cls')
                    break
            except FileNotFoundError:
                print("Diretório não encontrado.")
            except PermissionError:
                print("Você não tem permissão para acessar este diretório.")

        elif menu == 3:
            os.system('cls')
            programa = input("Digite o nome do programa consoante extensão do programa\n(ex.: notepad.txt)\n")

            try:             
                os.system('cls')    
                os.system(f"start {programa}")
                print(f"{programa} iniciado com sucesso.")
                voltar = int(input("\n\n1. Voltar ao menu\n"))
                if voltar == 1:
                    os.system('cls')
                    break
            except FileNotFoundError:
                print("Diretório não encontrado.")
            except PermissionError:
                print("Você não tem permissão para acessar este diretório.")
        elif menu == 4:
            os.system('cls')
            print("Ajuda de comandos do Windows")
            ajuda = os.system("help")
            print(ajuda)
            voltar = int(input("\n\n1. Voltar ao menu\n"))
            if voltar == 1:
                os.system('cls')
                break
        elif menu == 5:
            os.system('cls')
            print("Hora atual do sistema")
            hora = os.system("time")
            print(hora)
            voltar = int(input("\n\n1. Voltar ao menu\n"))
            if voltar == 1:
                os.system('cls')
                break
        elif menu == 6:
            os.system('cls')
            print("Saindo")
            quit()
        else:
            os.system('cls')
            print("Digite uma opção válida!")
            break

        
