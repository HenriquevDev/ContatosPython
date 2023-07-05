def cadastrar_contato():
    nome = input("Digite o nome: ")
    telefone = input("Digite o telefone: ")
    contato = nome + ":" + telefone + "\n"
    
    with open("contatos.txt", "a") as arquivo:
        arquivo.write(contato)
    
    print("Contato cadastrado com sucesso!")

def consultar_contato():
    nome = input("Digite o nome do contato a ser consultado: ")
    encontrado = False
    
    with open("contatos.txt", "r") as arquivo:
        for linha in arquivo:
            if nome in linha:
                print("Telefone: ", linha.split(":")[1])
                encontrado = True
                break
    
    if not encontrado:
        print("Contato não encontrado.")

def exibir_menu():
    print("1. Cadastrar novo contato")
    print("2. Consultar contato")
    print("3. Sair")

def main():
    while True:
        exibir_menu()
        opcao = input("Digite a opção desejada: ")
        
        if opcao == "1":
            cadastrar_contato()
        elif opcao == "2":
            consultar_contato()
        elif opcao == "3":
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Digite novamente.")

if __name__ == "__main__":
    main()
