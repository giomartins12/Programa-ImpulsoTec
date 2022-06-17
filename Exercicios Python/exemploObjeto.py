class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def setNome(self, nome):
        self.nome = nome

    def getNome(self):
        return self.nome

    def setIdade(self, idade):
        self.idade = idade

    def getIdade(self):
        return self.idade

#pessoaGiovanni = Pessoa("Giovanni", 33)
#pessoaGiovanni.setNome("Giovanni Martins")
#pessoaGiovanni.setIdade(41)
#print(pessoaGiovanni.getNome())
#print(pessoaGiovanni.getIdade())

#pessoaLucas = Pessoa("Lucas", 26)
#print(pessoaLucas.getNome())
#print(pessoaLucas.getIdade())

