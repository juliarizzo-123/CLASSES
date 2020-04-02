#criar uma classe que modele um retangulo 
# atributos: lado a, lado b 
# metodos: mudar o valor dos lados 
# retornar o valor dos lados 
# calcular o valor dos lados 
# calcular a area 
# calcular o perimetro

class Retangulo():
    ladoA=0
    ladoB=0
    area=0
    perimetro=0

    def lados(self):
        self.ladoA = int(input('digite um lado: '))
        self.ladoB = int(input('digite um lado: '))

    def area(self):
        self.area = (self.ladoA * self.ladoB)
        print ('a area é: {}'.format(self.area))

    def perimetro(self):
        self.perimetro = ((2*self.ladoA)+(2*self.ladoB))
        print ('o perimetro é: {} '.format(self.perimetro))

    def retorv(self):
        print (self.ladoA)
        print (self.ladoB)
     
        
        

x = Retangulo()
x.lados()
x.area()
x.perimetro()


