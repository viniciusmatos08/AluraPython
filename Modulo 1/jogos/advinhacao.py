import random

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = random.randrange(1,101)
total_de_rodadas = 3
pontos = 1000

print("Qual nivel de dificuldade?")
print("(1) Facil (2) Medio (3) Dificil")

nivel = int(input("Define o nivel: "))

if(nivel == 1):
    total_de_rodadas = 20
elif(nivel == 2):
    total_de_rodadas = 10
else:
    total_de_rodadas = 5

for rodada in range(1, total_de_rodadas + 1):
    print("Tentatiava {} de {}".format(rodada, total_de_rodadas))

    chute = int(input("Voce deve digitar um numero entre 1 e 100!: "))

    print("Você digitou ", chute)

    if (chute < 1 or chute > 100):
        print("Voce deve digitar um numero entre 1 e 100!")
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto


    if(acertou):
        print("Você acertou e fez {} pontos".format(pontos))
        break
    else:
        if(maior):
            print("Você errou! o chute é maior do que o numero secreto")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
        elif(menor):
            print("Você errou! o chute é menor do que o numero secreto")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

print("fim do jogo")