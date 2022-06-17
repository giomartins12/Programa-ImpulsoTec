#Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';
#Use a função len(string) para saber o tamanho de um texto (número de caracteres).

nome = input("\t Digite o nome (Insira pelo menos 4 caracteres): ")

while nome.__len__() < 4:    # Tambem serve len(nome)
    print("\t Insira pelo menos 4 caracteres")
    nome = input("\t Digite o nome: ")

idade = float(input("\t Digite a idade (entre 1 e 100 anos): "))

while (idade <= 0) or (idade > 100):
    print("\t Idade fora dos parametros! (entre 1 e 100): ")
    idade = float(input("\t Digite a idade (entre 0 e 150 anos) : "))

salario = float(input("\t Digite o salario (maior que zero): "))

while (salario <= 0):
    print("\t Insira um valor valido!")
    salario = float(input("\t Digite o salario (maior que zero): "))

sexo = input("\t Digite o sexo ('f' p/ feminino e 'm' p/ masculino): ")

while (sexo != 'f') and (sexo != 'm'):
    print("\t Insira um valor valido!")
    sexo = input("\t Digite o sexo ('f' p/ feminino e 'm' p/ masculino): ")

estado_civil = input("\t Digite o estado civil ('s' p/ solteiro, 'c' p/ casado, 'v' p/ viuvo e 'd' p/ divorciado): ")

while estado_civil != 's' and estado_civil != 'c' and estado_civil != 'v' and estado_civil != 'd':
    print("\t Insira um valor valido!")
    estado_civil = input("\t Digite o estado civil ('s' p/ solteiro, 'c' p/ casado, 'v' p/ viuvo e 'd' p/ divorciado): ")

print("\t Nome: ",nome)
print("\t Idade: ", idade)
print("\t Salario: ", salario)
print("\t Sexo: ", sexo)
print("\t Estado civil: ", estado_civil)
