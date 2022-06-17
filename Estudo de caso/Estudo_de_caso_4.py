# Estudo de caso 4 -Crie um arquivo texto vazio e acrescente o texto abaixo no arquivo:

input("\t Digite o texto:")
with open("texto_exercicio.txt", 'a', encoding='utf-8') as arquivo:
        arquivo.writelines(input('\t'))
        arquivo = open("texto_exercicio.txt", 'r')
        for linha in arquivo:
            linha = linha.rstrip()
            print(linha)
        arquivo.close()

