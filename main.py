import os
import cartas
from random import randint

class Carta:
    def __init__(self, nome, numero, naipe, valor):
        self.nome = nome
        self.numero = numero
        self.naipe = naipe
        self.valor = valor

def select_area():
    print('digite 1 para: [area amorosa].\ndigite 2 para: [area profissional].\ndigite 3 para: [area financeira]\ndigite 0 para: [sair]')
    area = int(input('digite a sua oção e pressione enter:'))
    return area

def random_card():
    carta_num= randint(0, len(cartas.baralho))
    carta = cartas.baralho[carta_num]
    return carta

def jogo_simples():
    cartas = []
    for i in range(0, 3):
        carta = random_card()
        cartas.append(carta)
    return cartas

def createCard(cardlist):
    os.system('cls')
    for card in cardlist:
        print (f'carta: {card['nome']}\nnúmero: {card['número']}\ncarta do baralh0: {card['valor']} {card['naipe']}\n')



leitura = []
opc = -1
while opc != 0:
    os.system('cls')
    print('|-----------------------------|')
    print('seleciaone a area desejada:')
    Global_area = select_area()
    if Global_area == 0:
        os.system('cls')
        print('obrigado por utiliar!')
        opc = 0
    elif Global_area > 3:
        os.system('cls')
        print('valor inválido!')
        input('pressione enter para continuar...')
        os.system('cls')
    if Global_area == 1:
        os.system('cls')
        cards_from_game = jogo_simples()
        createCard(cards_from_game)
        input('pressione enter para continuar...')