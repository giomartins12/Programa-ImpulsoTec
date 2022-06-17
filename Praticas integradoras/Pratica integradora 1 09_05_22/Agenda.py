from tabulate import tabulate
import os

########Lista de funções##########

def Cadastro(Contatos):
    nome = input("Digite o Nome: ")
    ddd = int(input("Digite o DDD: "))
    telefone = int(input("Digite o telefone (somente numeros: "))
    email = input("Digite o email: ")
    Contatos.append((nome, ddd, telefone, email))

def Listar(Contatos):
    for contato in Contatos:
        nome, ddd, telefone, email = contato
        print(tabulate(Contatos, headers=["nome", "DDD", "Telefone", "email"]))

def Listar_contato(Contatos):
     contato_ind = "Digite o contato que deseja verificar: "
     for contato in Contatos:
         if contato_ind == contato:
            for cont in Contatos:
                print(tabulate(cont, headers=["nome", "DDD", "Telefone", "email\n"]))
         else:
             input("Contato não localizado")

def excluir_all(Contatos):
        exclusao = input("Deseja realmente apagar todos os contatos (1 p/ sim 2 p/ não)? ")
        if exclusao == 1:
            for contato in Contatos:
                Contatos.clear()
                print("Contatos apagados!")
        else:
            print("Nenhum contato foi apagado!")


def excluir_contatos(Contatos):
   for nome in Contatos:
       apagar = input("Digite o nome do contato a ser apagado: ")
       if nome == apagar:
         Contatos.remove(apagar)
         print("Contato apagado!")
       else:
            print("Contato não encontrado!")



def menu_contatos():
    print("Escolha uma opção:\n ")
    print("1.Cadastra contato:\n ")
    print("2.listar contatos:\n ")
    print("3. Apagar contatos:\n ")
    print("4. sair")

Contatos = []
flag = True
while flag:
    menu_contatos()
    try:

            opcao = int(input("\t Digite a opção: "))
            if opcao == 1:
                Cadastro(Contatos)
            elif opcao == 2:
                 Listar(Contatos)
            elif opcao == 3:
                 ex_opcao = int(input("Digite a opção para excluir (1 p/ exclusão da agenda - 2 p/ exclusão do contato): "))
                 if ex_opcao == 1:
                    excluir_all(Contatos)
                 else:
                    excluir_contatos(Contatos)
            elif opcao == 4:
                flag = False
                with open("Agenda.txt", 'a', encoding='utf-8') as arquivo:
                    for item in Contatos:
                        arquivo.writelines(f"\n Nome {item[0]} ddd {item[1]} telefone {item[2]} Email {item[3]}")
                        print("Log gerado no texto Agenda.txt")
            else:
                print("Opção invalida!")
    except ValueError:
            print("\t Digite somente números!")


