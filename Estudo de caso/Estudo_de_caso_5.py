# Estudo de caso 5 - Faça um algoritimo que calcule a enesimo numero de sequencia de fibonanci

condicao = True
while condicao != False:
    try:
        enesimo = int(input("Digite o enesimo numero desejado da sequencia de Fibonanci: "))
        var1 = 1
        var2 = 1
        var3 = 0
        cont = 1

        while enesimo >= cont:
            var3 = (var1 + var2)
            var2 = (var1)
            var1 = (var3)
            cont = (cont +1)

        else:
            print("O enesimo numero da sequencia de", enesimo, "numeros é: ", var3)
        break

    except ValueError:
            print("somente numeros!")


