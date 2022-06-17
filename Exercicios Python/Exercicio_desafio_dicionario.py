nome_aluno = input("digite o nome do aluno ")
serie_aluno = input("digite o ano do aluno ")
nota1 = input("digite a 1ª nota ")
nota2 = input("digite a 2ª nota ")
nota3 = input("digite a 3ª nota ")
falta_aluno = input("digite o numero de faltas do aluno ")

aluno = {'nome': nome_aluno, 'serie': serie_aluno, 'nota 1': nota1, 'nota 2' : nota2, 'nota 3' : nota3, 'falta' : falta_aluno}

soma = (int(nota1) + int(nota2) + int(nota3))
media = (soma / 3)

if (soma >= 60 and int(falta_aluno) < 10):
    print("Aluno aprovado! nota total do semestre é: " + str(soma), "e a média das notas é " + str(media))
if (soma < 60 and int(falta_aluno) < 10):
    print("Aluno reprovado por nota! nota total do semestre é: " + str(soma), "e a média das notas é " + str(media))
if (soma >=60 and int(falta_aluno) >= 10):
    print("Aluno reprovado por falta! nota total do semestre é: " + str(soma), "e a média das notas é " + str(media))
if (soma < 60 and int(falta_aluno) >= 10):
    print("Aluno reprovado por nota e falta! nota total do semestre é: " + str(soma), "e a média das notas é " + str(media))

for keys, values in aluno.items():
    print(keys, values)



