lista1 = [1,2,3,4]

def multiplicacao(x):
    return x * 2

lista2 = map(multiplicacao, lista1)
lista3 = list(map(lambda x: x * 2, lista1))

print(list(lista2))
print(lista3)

usuarios = [("contato@gmail.com", True),
            ("adm@gmail.com", True),
            ("secretaria@gmail.com", False)]

def getEmail(usuario):
    return usuario[0]

def valido(usuario):
    return usuario[1] == True

print(list(filter(valido,usuarios)))
print(list(map(getEmail,usuarios)))

emails = list(map(getEmail,filter(valido,usuarios)))
print(emails)


