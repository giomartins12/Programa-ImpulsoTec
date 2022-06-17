# Uso do If e else

idade = 30
mediaidade = 30

# if idade < mediaidade: print("A idade é menor que a media")

if idade < mediaidade:
    print("A idade é menor que a média")
elif idade > mediaidade:
    print("A idade é maior que a média")
else:
    print("A idade é igual a media")

idade1 = 80
idade2 = 70
medianova = 35
if (idade1 < idade2):
    print("Você é mas novo!")
    if idade1 < 30:
        print("Você está em uma idade excelente!")
else:
    print("Você está bem velhinho!")

if idade1 > medianova and idade2 > medianova:
    print("Você se enquandra no perfl da empresa!")
else:
    print("Você não se enquadra no perfil!")

cores = ['amarelo', 'verde','azul', 'vermelho']

if 'amarelo' in cores:
    print("possui")
else:
    print("Não possui")

cor_cliente = input("digite a cor do desejada")

if cor_cliente.lower() in cores:
    print("cor cadastrada")
else:
    print("cor não cadastrada")
