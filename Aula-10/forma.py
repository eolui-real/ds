class Forma:                        #### #SUPER CLASSE (CLASSE ANCESTRAL, COMEÇA COM A PRIMEIRA LETRA MAIUSCULA)
    def __init__(self,nome):
        self.nome = nome


    def calcula_area(self):
        raise NotImplementedError("O método deve ser implementado em subclasse")


    def calcula_perimetro(self):
        raise NotImplementedError("O método deve ser implementado em subclasse")


    def __str__(self):
        return f"Forma: {self.nome}"


   