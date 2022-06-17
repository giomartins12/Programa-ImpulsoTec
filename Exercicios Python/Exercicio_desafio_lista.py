# Exercicio desafio material de apoio (utilização de listas)

print('\t--------------------------------Desafio lista--------------------------------------------------')

funcionario = ['Sasha']
func_noite = ['Everson', 'Rever', 'Alonso']
func_dia = ['Guilherme', 'Jair', 'Keno', 'Mariano']
func_carro_noite = ['Rever', 'Alonso']
func_carro_dia = ['Jair','Mariano']
func_s_carro = ['Everson', 'Guilherme','Sasha']

funcionario.append(func_dia + func_noite)
print("\t lista de funcionários: ", funcionario)
funcionario.clear()
funcionario.append(func_dia)
print("\t lista de funcionários do dia: ", funcionario)
funcionario.clear()
funcionario.append(func_noite)
print("\t lista de funcionários da noite: ", funcionario)
funcionario.clear()
funcionario.append(func_carro_noite + func_carro_dia)
print("\t lista de funcionários de carro: ", funcionario)
funcionario.clear()
funcionario.append(func_s_carro)
print("\t lista de funcionários sem carro: ", funcionario)

print('\t------------------------------------------------------------------------------------------------')


