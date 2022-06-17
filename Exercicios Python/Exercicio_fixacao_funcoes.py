#def boas_vindas(nome, idade):
    #print(f"\t olá {nome} você tem {str(idade)} anos")
#boas_vindas("Giovanni", 41)


def cadastrar(pessoas):
    cpf = input("\t Digite seu cpf: ")
    nome = input("\t Digite seu nome: ")
    idade = int(input("\t Digite sua idade: "))
    pessoas.append((cpf, nome, idade))

def listar(pessoas):
    for pessoa in pessoas:
        cpf, nome, idade = pessoa
        print(f"\t Nome: {nome} CPF: {cpf} idade: {idade} ")

def exibir_menu():
    print('''\t\n Escolha uma opção:
    1.Cadastra pessoa
    2. Listar pessoa
    3. sair''')

def main():
    pessoas = []
    flag = True
    while flag:
        exibir_menu()
        try:
            opcao = int(input("\t Digite a opção: "))
            if opcao == 1:
                cadastrar(pessoas)
            elif opcao == 2:
                listar(pessoas)
            elif opcao == 3:
                flag = False
            else:
                print("\t Opção invalida!")
        except ValueError:
            print("\t Digite somente números!")

main()