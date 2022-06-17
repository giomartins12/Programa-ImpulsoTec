# Programa converta para metros.

print('\t ---------Conversão de medidas-----------')

distancia = ('km', 'cm', 'mm')


medida = str(input("Digite qual medida será convertida para metro (km, cm ou mm): "))

if medida in distancia:
    convert = int(input("Digite o valor a ser convertido: "))
    if medida == "km":
        metros = (convert * 1000)
        print(convert ,"km corresponde a", metros, "metros.")
    if medida == "cm":
        metros = (convert / 100)
        print(convert, "Cm corresponde a", metros, "metros.")
    if medida == "mm":
        metros = (convert / 1000)
        print(convert, "mm corresponde a", metros, "metros.")
else:
    print("unidade não encontrada!")

