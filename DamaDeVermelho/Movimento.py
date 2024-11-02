from Casas import *


class Movimento:
    def __init__(self, i, j, i_final, j_final, cor, tipo_movimento, peca_comida_i=None, peca_comida_j=None):
        self.i = i
        self.j = j
        self.i_final = i_final
        self.j_final = j_final
        self.cor = cor
        self.tipo_movimento = tipo_movimento
        self.peca_comida_i = peca_comida_i
        self.peca_comida_j = peca_comida_j

    @staticmethod
    def calcular_movimentos_possiveis(board, cor):

        if cor == PECA_BRANCA_SELECIONADA or cor == PECA_BRANCA:
            direcoes = ((-1, -1), (-1, 1))
        elif cor == PECA_PRETA_SELECIONADA or cor == PECA_PRETA:
            direcoes = ((1, -1), (1, 1))
        elif cor == PECA_BRANCA_DAMA_SELECIONADA or cor == PECA_PRETA_DAMA_SELECIONADA or cor == PECA_BRANCA_DAMA or cor == PECA_PRETA_DAMA:
            direcoes = ((-1, -1), (-1, 1), (1, -1), (1, 1))
        else:
            return None

        movimentos = []

        for i in range(8):
            for j in range(8):
                if board[i][j] != CASA_VAZIA and color(cor) == color(board[i][j]):
                    for direcao in direcoes:
                        i_aux = i + direcao[0]
                        j_aux = j + direcao[1]
                        if 0 <= i_aux < 8 and 0 <= j_aux < 8 and (board[i_aux][j_aux] == CASA_VAZIA):
                            movimentos.append(Movimento(i, j, i_aux, j_aux, cor, MOVIMENTO_NORMAL))
                        else:
                            i_aux += direcao[0]
                            j_aux += direcao[1]
                            if 0 <= i_aux < 8 and 0 <= j_aux < 8 and board[i_aux][j_aux] == CASA_VAZIA:
                                cor_comida = board[i + direcao[0]][j + direcao[1]]
                                if cor == PECA_BRANCA_SELECIONADA or cor == PECA_BRANCA or cor == PECA_BRANCA_DAMA_SELECIONADA or cor == PECA_BRANCA_DAMA:
                                    if cor_comida == PECA_PRETA_SELECIONADA or cor_comida == PECA_PRETA or cor_comida == PECA_PRETA_DAMA_SELECIONADA or cor_comida == PECA_PRETA_DAMA:
                                        movimentos.append(
                                            Movimento(i, j, i_aux, j_aux, cor, MOVIMENTO_COMER, i + direcao[0],
                                                      j + direcao[1]))
                                if cor == PECA_PRETA_SELECIONADA or cor == PECA_PRETA or cor == PECA_PRETA_DAMA_SELECIONADA or cor == PECA_PRETA_DAMA:
                                    if cor_comida == PECA_BRANCA_SELECIONADA or cor_comida == PECA_BRANCA or cor_comida == PECA_BRANCA_DAMA_SELECIONADA or cor_comida == PECA_BRANCA_DAMA:
                                        movimentos.append(
                                            Movimento(i, j, i_aux, j_aux, cor, MOVIMENTO_COMER, i + direcao[0],
                                                      j + direcao[1]))

        if len(movimentos) == 0:
            return None

        movimentos_comer = []
        for movimento in movimentos:
            if movimento.tipo_movimento == MOVIMENTO_COMER:
                movimentos_comer.append(movimento)
                print('Movimento comer: ', movimento.i, movimento.j, movimento.i_final, movimento.j_final,
                      movimento.cor)
        if len(movimentos_comer) > 0:
            return movimentos_comer
        return movimentos

    def to_string(self):
        return (f'{self.i},{self.j},{self.i_final},{self.j_final},{self.cor},{self.tipo_movimento},{self.peca_comida_i},'
                f'{self.peca_comida_j}')

    @staticmethod
    def from_string(movimento_str):
        movimento = movimento_str.split(',')
        return Movimento(int(movimento[0]), int(movimento[1]), int(movimento[2]), int(movimento[3]), int(movimento[4]),
                         int(movimento[5]), int(movimento[6]), int(movimento[7]))