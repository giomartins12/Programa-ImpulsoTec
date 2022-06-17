#Exercicios de função "print"
print('hello Word!')
print("hello!")
print('Giovanni tem ' + '41 anos')
nome = "Giovanni Martins"
idade = 41

print ("meu nome é " + nome + " e tenho a idade de " + str(idade) + " anos")

texto = f"nome {nome} e idade {idade}"
print(texto)

print(nome.lower())
print(nome.upper())
print(len(nome))
print(nome[4])
print(nome[1:4])
print(nome[0:4])
print(nome.count('o'))

#Exercicio de variaveis

email = 'giovanni@accenture.com'
usuario, dominio = email.split("@")
print(usuario)
print(dominio)

frase = "Atletico, gostamos muito de você!"
print(frase.find('Atletico'))
print(frase.replace('gostamos', 'gosto'))

print(4 + 2)
print(4 + 2.35)
print(2 * (2 + 6))
print(2 * 5 * 2)

i = 5
y = 9
soma = i + y
print(soma)

num_x = 3
print(num_x + num_x)
print(str(num_x) + str(num_x))
print(str(y) + " Esse é o numero!")
print(min(3,6))
print(round(12.4))

#cidade = input("Digite a sua cidade ")
#print(" A cidade do usuario é: " +cidade)

#num1 = input("digite o primeiro numero ")
#num2 = input("digite o segundo numero ")
#resultado = int(num1) + int(num2)
#print("O resultado é ", resultado)

amigos =["João", "Luiz", "Julia","Fabio", "Lucas"]
print(amigos)
print(amigos[4])
print(amigos[-3])
amigos[1] = "Silvana"
print(amigos)
print(amigos[1:3])
print(amigos[2:])
amigos.append("Marcio")
print(amigos)
amigos.remove("Julia")
print(amigos)
amigos.pop(3)
print(amigos)

numeros =[10, 8, 5, 9, 6, 4, 1, 0, 3, 2]
numeros.sort()
print(numeros)






