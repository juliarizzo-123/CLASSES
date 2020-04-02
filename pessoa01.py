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
        h.envelhecer()

    elif op == 2:
        h.engordar()

    elif op == 3:
        h.emagrecer()

    elif op == 4:
        h.crescer()



