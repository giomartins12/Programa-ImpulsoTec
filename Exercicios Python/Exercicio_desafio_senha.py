#Faça um programa que leia um nome de usuário e a sua senha e
# não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro
# e voltando a pedir as informações.

nome_usuario = input("\t Digite o nome de usuario: ")
senha_usuario = input("\t Digite a senha para cadastro: ")

while senha_usuario == nome_usuario:
    print("\t A senha não pode ser igual ao nome de usuario! Digite novamente!")
    senha_usuario = input("\t Digite a senha para cadastro: ")

print("\t senha cadastrada com sucesso!")