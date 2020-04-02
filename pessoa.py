
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


    def envelhecer(self,anos):
        self.i=0
        for self.i in range(anos):
            if(anos<=21):
                self.y=+1         
                self.idade = +1
                self.altura=0.5*self.y+self.altura
            
            else:
                self.idade = self.idade + anos
  

    def engordar(self,kg):
        self.peso =  self.peso + kg
        

    def emagrecer(self,kg):
        self.peso =  self.peso - kg
       


    def crescer(self,cm):
        self.altura =  self.altura + cm
        

    
    def getNome(self):
        return self.nome
    def getIdade(self):
        return self.idade
    def getPeso(self):
        return self.peso
    def getAltura(self):
        return self.altura

   # def info(self):
    #   print("O nome : {}".format(self.nome))
     #  print("A idade: {}".format(self.idade))
      # print("O peso : {} Kg".format(self.peso))
       #print("A altura: {} cm".format(self.altura))