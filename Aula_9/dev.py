from aula_9 import Pessoa
class Dev(Pessoa):

    nome = ""
    função = ""
    cpf = ""
    email = ""

    def apresentarSe(self):
        print(f"Olá, sou um desenvolvedor, Meu nome é {self.nome}!")