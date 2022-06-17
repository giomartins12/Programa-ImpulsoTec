valor = 100

while valor > 20:
    print(valor)
    valor -= 5

print("\t")

lista = [1,2,3,4,5]
tamanho = len(lista)
x = 0

while (x < tamanho):
    print(lista[x])
    x += 1

print("\t")

#a = 10
#i = 5
#while i <= a: print(a); a -= 1

a = 10
i = 5
while i <= a:
    a -= 1
    if a == 7:
        print("Chegamos no 7")
        continue
    print(a)

print("\t")

a = 10
i = 5
while i <= a:
    a -= 1
    if a == 7:
        print("Chegamos no 7")
        break
    print(a)

print("\t")


i = 10
while i <= 15:
    print(i)
    i += 1
else:
    print("Chegamos no final do while")

print("\t")

pontos = 0
questão = 1

while questão <= 3:
    resposta = input(f"Resposta da questão {questão}: ")
    if questão == 1 and (resposta == "b" or resposta == "B"):
        pontos = pontos + 1
    if questão == 2 and (resposta == "a" or resposta == "A"):
        pontos = pontos + 1
    if questão == 3 and (resposta == "d" or resposta == "D"):
        pontos = pontos + 1
    questão = questão + 1

print (f"O aluno teve {pontos} pontos")









