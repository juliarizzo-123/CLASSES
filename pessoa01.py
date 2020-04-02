from pessoa import Humano
op = 5

nome = input('Digite seu nome: ')
idade = int(input("Digite sua idade: "))
peso = int(input("Digite seu peso: "))
altura = int(input("Digite sua altura: "))
h = Humano(nome,idade,peso,altura)
while op != 0:

#pessoa = Humano(nome,idade,peso,altura)

    op = int(input("O que voce deseja fazer?: \n [1] - envelhecer \n [2] - engordar \n [3] - emagrecer \n [4] - crescer \n qual sua opçao?: "))

    if op == 1:
        anos = int(input("Digite a quantidades de ano a ser envelhecido: "))
        h.envelhecer(anos)
        print("A nova idade  é:{0}".format(h.getIdade()))
        print("A nova altura  é:{0}".format(h.getAltura()))

    elif op == 2:
        kg = int(input("quantos quilos voce quer engordar: "))
        h.engordar(kg)
        print("A novo peso é: {0}".format(h.getPeso()))


    elif op == 3:
        kg = int(input("quantos quilos voce quer emarecer: "))
        h.emagrecer(kg)
        print("A novo peso é: {0}".format(h.getPeso()))

    elif op == 4:
        cm = int(input("quanto voce quer crescer: "))
        h.crescer(cm)
        print("A nova altura é: {0}".format(h.getAltura()))

    

