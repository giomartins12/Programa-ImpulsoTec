#Faça um programa que peça uma nota, entre zero e dez.
# Mostre uma mensagem caso o valor seja inválido e continue
# pedindo até que o usuário informe um valor válido.


nota = float(input("\t Insira uma nota (entre 0 e 10): "))

while (nota < 0) or (nota > 10):
    print("\t nota invalida!")
    nota = float(input("\t Insira uma nota (entre 0 e 10): "))

print("\t A nota digitada está dentro dos parâmetros: ", nota)
