import pygame
from Casas import *
from Movimento import *


class Damas:
    def __init__(self):
        self.board = [[0 for _ in range(8)] for _ in range(8)]
        self.inicializar_tabuleiro()
        pygame.init()
        pygame.display.set_caption('Dama de Vermelho')
        self.screen = pygame.display.set_mode((800, 800))
        self.selecionada = None
        self.movimentos = None

    def inicializar_tabuleiro(self):
        self.board[0][0] = PECA_PRETA
        self.board[0][2] = PECA_PRETA
        self.board[0][4] = PECA_PRETA
        self.board[0][6] = PECA_PRETA

        self.board[1][1] = PECA_PRETA
        self.board[1][3] = PECA_PRETA
        self.board[1][5] = PECA_PRETA
        self.board[1][7] = PECA_PRETA

        self.board[2][0] = PECA_PRETA
        self.board[2][2] = PECA_PRETA
        self.board[2][4] = PECA_PRETA
        self.board[2][6] = PECA_PRETA

        self.board[5][1] = PECA_BRANCA
        self.board[5][3] = PECA_BRANCA
        self.board[5][5] = PECA_BRANCA
        self.board[5][7] = PECA_BRANCA

        self.board[6][0] = PECA_BRANCA
        self.board[6][2] = PECA_BRANCA
        self.board[6][4] = PECA_BRANCA
        self.board[6][6] = PECA_BRANCA

        self.board[7][1] = PECA_BRANCA
        self.board[7][3] = PECA_BRANCA
        self.board[7][5] = PECA_BRANCA
        self.board[7][7] = PECA_BRANCA

    def print_tabuleiro(self):
        for i in range(8):
            for j in range(8):
                print(self.board[i][j], end=' ')
            print()

    def desenhar_tabuleiro(self):
        cont = 0
        for i in range(8):
            for j in range(8):
                if cont % 2 == 0 and i % 2 == 0 or cont % 2 != 0 and i % 2 != 0:
                    pygame.draw.rect(self.screen, (255, 255, 255), (j * 100, i * 100, 100, 100))
                else:
                    pygame.draw.rect(self.screen, (0, 0, 0), (j * 100, i * 100, 100, 100))

                if self.board[i][j] == PECA_BRANCA:
                    pygame.draw.circle(self.screen, (255, 0, 0), (j * 100 + 50, i * 100 + 50), 40)
                elif self.board[i][j] == PECA_PRETA:
                    pygame.draw.circle(self.screen, (0, 0, 255), (j * 100 + 50, i * 100 + 50), 40)
                elif self.board[i][j] == PECA_BRANCA_SELECIONADA:
                    pygame.draw.circle(self.screen, (255, 255, 0), (j * 100 + 50, i * 100 + 50), 40)
                elif self.board[i][j] == PECA_PRETA_SELECIONADA:
                    pygame.draw.circle(self.screen, (0, 255, 255), (j * 100 + 50, i * 100 + 50), 40)

                if self.board[i][j] == PECA_BRANCA_DAMA:
                    pygame.draw.circle(self.screen, (255, 0, 0), (j * 100 + 50, i * 100 + 50), 40)
                    pygame.draw.circle(self.screen, (255, 255, 255), (j * 100 + 50, i * 100 + 50), 30)
                elif self.board[i][j] == PECA_PRETA_DAMA:
                    pygame.draw.circle(self.screen, (0, 0, 255), (j * 100 + 50, i * 100 + 50), 40)
                    pygame.draw.circle(self.screen, (255, 255, 255), (j * 100 + 50, i * 100 + 50), 30)

                if self.board[i][j] == CASA_MOVIMENTO:
                    pygame.draw.circle(self.screen, (0, 255, 0), (j * 100 + 50, i * 100 + 50), 12)
                cont += 1

    def run(self):

        clock = pygame.time.Clock()
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    self.selecionar_peca(x, y)

            self.screen.fill((0, 0, 0))
            self.desenhar_tabuleiro()
            pygame.display.flip()
            clock.tick(60)
        pygame.quit()
        quit()

    def selecionar_peca(self, x, y):
        i = y // 100
        j = x // 100

        if self.board[i][j] == CASA_MOVIMENTO:
            self.mover_peca(i, j)
            return

        self.desmarcar_selecionada()
        self.marcar_selecionada(i, j)

    def mover_peca(self, i, j):
        selecionada_i = self.selecionada[0]
        selecionada_j = self.selecionada[1]
        cor = self.board[selecionada_i][selecionada_j]
        if cor == PECA_BRANCA_SELECIONADA:
            cor = PECA_BRANCA
        elif cor == PECA_PRETA_SELECIONADA:
            cor = PECA_PRETA
        self.board[i][j] = cor

        movimento = self.obter_movimento_da_jogada(i, j, selecionada_i, selecionada_j)
        if movimento is not None:
            if movimento.tipo_movimento == MOVIMENTO_COMER:
                self.board[movimento.peca_comida_i][movimento.peca_comida_j] = CASA_VAZIA
            else:
                self.board[selecionada_i][selecionada_j] = CASA_VAZIA
        self.tornar_dama(i, j)
        self.desmarcar_selecionada()

    def obter_movimento_da_jogada(self, i, j, selecionada_i, selecionada_j):
        if self.movimentos is not None:
            for m in self.movimentos:
                if m.i_final == i and m.j_final == j and m.i == selecionada_i and m.j == selecionada_j:
                    return m
        return None

    def tornar_dama(self, i, j):
        if self.board[i][j] == PECA_BRANCA and i == 0:
            self.board[i][j] = PECA_BRANCA_DAMA
        elif self.board[i][j] == PECA_PRETA and i == 7:
            self.board[i][j] = PECA_PRETA_DAMA

    def desmarcar_selecionada(self):
        if self.selecionada is not None:
            i = self.selecionada[0]
            j = self.selecionada[1]
            if self.board[i][j] == PECA_BRANCA_SELECIONADA:
                self.board[i][j] = PECA_BRANCA
            elif self.board[i][j] == PECA_PRETA_SELECIONADA:
                self.board[i][j] = PECA_PRETA
            self.selecionada = None
        for i in range(8):
            for j in range(8):
                if self.board[i][j] == CASA_MOVIMENTO:
                    self.board[i][j] = CASA_VAZIA

    def marcar_selecionada(self, i, j):
        if self.board[i][j] == PECA_BRANCA:
            self.board[i][j] = PECA_BRANCA_SELECIONADA
        elif self.board[i][j] == PECA_PRETA:
            self.board[i][j] = PECA_PRETA_SELECIONADA
        self.selecionada = (i, j)
        movimentos = Movimento.calcular_movimentos_possiveis(self.board, i, j)
        self.movimentos = movimentos
        if movimentos is None:
            print('Nenhum movimento possível')
            return

        for movimento in movimentos:
            i_aux = movimento.i_final
            j_aux = movimento.j_final
            print(f'Movimento: {i} {j} -> {i_aux} {j_aux}')
            self.board[i_aux][j_aux] = CASA_MOVIMENTO