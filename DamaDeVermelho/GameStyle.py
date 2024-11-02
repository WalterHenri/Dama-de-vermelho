import json
import numpy as np

NEGATIVE_INFINITY = -1000000
POSITIVE_INFINITY = 1000000


class GameStyle:
    def __init__(self, comer, perder_peca, virar_dama, inimigo_fazer_dama, tomar_dama, perder_dama, neutro=0,
                 perder=NEGATIVE_INFINITY,
                 ganhar=POSITIVE_INFINITY, empate=0):
        self.perder = perder
        self.ganhar = ganhar
        self.empate = empate
        self.neutro = neutro
        self.comer = comer
        self.virar_dama = virar_dama
        self.inimigo_fazer_dama = inimigo_fazer_dama
        self.perder_peca = perder_peca
        self.tomar_dama = tomar_dama
        self.perder_dama = perder_dama

    def save_style(self, filename='style.json'):
        with open(filename, 'w') as f:
            json.dump(self.__dict__, f)

    @staticmethod
    def load_style(filename='style.json'):
        with open(filename, 'r') as f:
            style = json.load(f)
        return GameStyle(**style)
