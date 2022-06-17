aluno = {'nome:' : 'Lucas', 'idade:' : 29, 'Conceito:' : 'A'}
print(aluno)
print(aluno['nome:'])
aluno['nome:'] = "Arthur"
print(aluno['nome:'])

aluno.update({'nome:' : 'Antonio', 'Conceito:' : 'B'})
print(aluno)
aluno.update({'Endereço:' : 'Rua alberto De Oliveira'})
print(aluno)

del aluno['idade:']
print(aluno)

for keys, values in aluno.items():
    print(keys, values)