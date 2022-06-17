#try:
    #f = open("lista.txt", 'r', encoding='utf-8' )
#finally:
    #f.close()

#with open("lista.txt", 'r', encoding='utf-8' ) as f:
    #print(f.read())
    #print(f.readlines())
    #print(f.readline())

#with open("lista.txt", 'r', encoding='utf-8' ) as f:
    #for linha in f:
        #print(linha)

# escreva
#with open("lista.txt", 'w', encoding='utf-8' ) as lista:
    #lista.write("nova lista")
listaA = ('Cavalo', 'cachorro', 'gato')
with open("lista.txt", 'a', encoding='utf-8' ) as lista:
        for item in listaA:
            lista.write(item)

