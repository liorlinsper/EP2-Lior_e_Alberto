import Funcoes_EP2
import random
# Misturando baralho
baralho = Funcoes_EP2.cria_baralho()
random.shuffle(baralho)
#Colocando o baralho em ordem
i = 0
while i < len(baralho):
    print("{0}. {1}".format(i+1,baralho[i]))
    i+=1

#JOGO:
 
pode_jogar = Funcoes_EP2.possui_movimentos_possiveis(baralho)

while pode_jogar == True:
    esc_carta = int(input("Escolha uma carta( digite um numero entre 1 e 52):"))
    if esc_carta < 0 or esc_carta > 52:
        print("Movimento Inválido")
