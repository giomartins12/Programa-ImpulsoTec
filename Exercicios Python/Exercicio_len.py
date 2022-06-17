quant = 10
login = str(input("Digite o login"))
while len(login) != quant:
    print("Numero de caracteres não aceito (10 caracteres)")
    login = str(input("Digite o login: "))
else:
    print("Login correto!")

