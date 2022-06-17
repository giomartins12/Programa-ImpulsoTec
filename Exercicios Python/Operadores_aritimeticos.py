cinco = 5
oito = 8

soma = cinco + oito
print(soma)

subtracao = 7 - 4
print(subtracao)

multiplicacao = 6 * 2
print(multiplicacao)

divisao = 10 / 2
print(divisao)

modulo = 8 % 2
print(modulo)

# Operadores Logícos

num = 7
num2 = 4

# and
print(num < num2 and num2 < 8)
print(num < num2 and num2 > 8)
print(num > num2 and num2 > 8)
print(num > num2 and num2 < 8)
#Falso e verdadeiro = Falso
#Falso e Falso = Falso
#Verdadeiro e Falso = Falso
#Verdadeiro e verdadeiro = Verdadeiro

# or
print(num < num2 or num2 < 8)
print(num < num2 or num2 > 8)
print(num > num2 or num2 > 8)
print(num > num2 or num2 < 8)
#Falso ou verdadeiro = verdadeiro
#Falso ou Falso = Falso
#Verdadeiro ou Falso = verdadeiro
#Verdadeiro e verdadeiro = Verdadeiro

# not
if not(num < num2 or num2 > 8):
       print('Imprimiu pq é verdadeiro!')
#Falso e verdadeiro = Falso (retorna verdadeiro)

# operadores de identidade

A = 20
B = 20
C = 22
D = 15
E = [10,20]
F= [10,20]

print(A is B)
print(A is C)
print(E is F)
print (E is not F)
print (C is not D)

# Operadores de associação
l = [20, 23, 26, 30]
print(20 in l)
print(21 in l)
print(21 not in l)

# Operadores de atribuição

x = 10
y = 10
x += 5 # Abreviação de x = x + 5
print(x)
x -= 5 # Abreviação de x = x - 5
print(x)
x *= 5 # Abreviação de x = x * 5
print(x)
x /= 5 # Abreviação de x = x / 5
print(x)
x %= 5 # Abreviação de x = x % 5
print(x)
y **= 5 # Abreviação de x = X** 5
print(y)

# Operadores relacionais

z = 10
w = 20

print(z == w)
print(z != w)
print(z > w)
print(z < w)
print(z >= w)
print(z <= w)
