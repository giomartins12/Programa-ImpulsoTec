#Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual
# de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%.
# Faça um programa que calcule e escreva o número de anos necessários para que a população do país A
# ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

#Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais.
# Valide a entrada e permita repetir a operação.

pais_a = (input("\t Digite o nome do primeiro país: "))
pais_b = (input("\t Digite o nome do segundo país: "))
populacao_A = float(input("\t Digite o numero de habitantes do 1º país: "))
populacao_B = float(input("\t Digite o numero de habitantes do 2º país: "))
taxa_a = float(input("\t Digite a taxa de crescimento anual do 1º país (%): "))
taxa_b = float(input("\t Digite a taxa de crescimento anual do 2º país (%): "))

convert_taxa_a = taxa_a / 100
convert_taxa_b = taxa_b / 100
crescimento_A = populacao_A * convert_taxa_a
crescimento_B = populacao_B * convert_taxa_b
cont_ano = 0

while populacao_A < populacao_B:
    populacao_A = populacao_A + crescimento_A
    crescimento_A = populacao_A * convert_taxa_a
    populacao_B = populacao_B + crescimento_B
    crescimento_B = populacao_B * convert_taxa_b
    cont_ano = cont_ano + 1


print("\t O país A alcançará o país B em ", cont_ano,"anos.")
print(round(populacao_A))
print(round(populacao_B))
print(cont_ano)
