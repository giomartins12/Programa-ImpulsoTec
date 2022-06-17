from exemploObjeto import Pessoa


class PessoaFisica(Pessoa):

    def __init__(self, CPF, nome, idade):
        super().__init__(nome, idade)
        self.cpf = CPF

    def getCPF(self):
        return self.cpf

    def setCPF(self, CPF):
        self.cpf = CPF


pessoafisica = PessoaFisica("01381647626", "Giovanni", 41)
print(pessoafisica.getNome())
print((pessoafisica.getCPF()))
print(pessoafisica.getIdade())
