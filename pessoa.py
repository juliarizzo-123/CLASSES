
# criar uma classe q represente uma pessoa
#os atributos sao:
#nome 
#idade
#peso
#altura

#metodos:
#envelhecer
#engordar
#emagrecer
#crescer
#mostrar informaçoe

#obs: por padrao a cada ano q a pessoa envelhece sendo a idade dela menor q 21 anos ela deve crescer 0,5cm
# (a classe deve estar em um arquivo separado)
#codigo principal
#precisa criar um obj do tipo pessoa mostra um menu pro usuario informaçoes da pessoa e opçoes para q seja alterado os valores

class Humano(object):
    def __init__(self,nome,idade,peso,altura):
        self.nome = nome    
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        self.idade(int(input('Quanto anos voce quer envlhecer: ')))
        self.idade = self.idade + self.idade

    def engordar(self):
        self.peso(int(input("Quanto voce quer engordar: ")))
        self.peso =  self.peso + self.peso

    def emagrecer(self):
        self.peso = (int(input("Quanto voce quer emagecer: ")))
        self.peso =  self.peso + self.peso

    def crescer(self):
        self.altura = (int(input("Quanto  voce quer crescer")))
        self.altura =  self.altura + self.altura
    


   # def info(self):
    #    print("O nome : {}".format(self.nome))
     #   print("A idade: {}".format(self.idade))
      #  print("O peso : {} Kg".format(self.peso))
       # print("A altura: {} cm".format(self.altura))