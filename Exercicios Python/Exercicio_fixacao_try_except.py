try:
    letras = ["a", "b", "c"]
    print(letras[3])
except IndexError:
    print("Esse elemento não existe na lista")


try:
    nota = int(input("\t Digite a nota do aluno: "))
except ValueError:
    condicao = True
    while condicao != False:

       print("\t Valor não aceito! somente numeros")
else:
    if nota >= 60: print("\t Aluno aprovado!")
    elif (nota >= 40) and (nota < 60): print("\t Aluno em recuperação!")
    else: print("\t Aluno reprovado!")
finally:
    print("\t Volte sempre!")


