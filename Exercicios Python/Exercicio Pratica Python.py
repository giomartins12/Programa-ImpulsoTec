# Programa que recebe um numero real e verifica se ele é
# Positivo, negativo ou zero - Giovanni Pereira Martins: data de entrega: 04/04/2022

print("\t--------Teste numeros--------")

cont = 0
quant = float(input("\t digite a quantidade de testes: "))

while cont < quant:
    cont = (cont + 1)
    num = float(input("\t Digite o numero: "))

    if (num > 0):
        print("\t numero positivo!")
    elif (num < 0):
        print("\t Numero negativo!")
    else:
        print("\t Numero igual a zero!")

else:
    print('\t--------seção encerrada! Obrigado!--------')

