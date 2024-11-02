import json
import numpy as np


class GameStyle:
    def __init__(self, comer, perder_peca, virar_dama, inimigo_fazer_dama, perder=0, ganhar=1, empate=0.5):
        self.perder = perder
        self.ganhar = ganhar
        self.empate = empate
        self.comer = self.sigmoid(comer)
        self.virar_dama = self.sigmoid(virar_dama)
        self.inimigo_fazer_dama = self.sigmoid(inimigo_fazer_dama)
        self.perder_peca = self.sigmoid(perder_peca)

    @staticmethod
    def sigmoid(x):
        return 1 / (1 + np.exp(-x))

    def save_style(self, filename='style.json'):
        with open(filename, 'w') as f:
            json.dump(self.__dict__, f)

    @staticmethod
    def load_style(filename='style.json'):
        with open(filename, 'r') as f:
            style = json.load(f)
        return GameStyle(**style)

