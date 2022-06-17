nome_aluno = input('Digite o nome do aluno: ')
nota_aluno = int(input('Digite a nota do aluno: '))
aluno = {'nome': nome_aluno, 'nota': nota_aluno}

if nota_aluno >= 60:
    print('Aluno aprovado!')
else:
    print('Aluno reprovado')

