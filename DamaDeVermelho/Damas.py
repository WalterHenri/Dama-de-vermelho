import pygame
import os
from datetime import timedelta
from Bot import Bot
from Config import Config
from GameStyle import GameStyle
from Movimento import *
from Constants import *
from DrawTools import *
from ResultadoModal import ResultadoModal

class Damas:
    def __init__(self, mode=TWO_PLAYER, nome_bot=""):
        self.running = False
        self.tabuleiroCarregado = False
        self.tempoInicial = None
        self.tempoTotal = timedelta(seconds=0)
        self.board = [[0 for _ in range(8)] for _ in range(8)]
        self.inicializarJogo()
        pygame.init()
        pygame.display.set_caption('Dama de Vermelho')
        self.background = pygame.image.load('Assets/background.jpg')
        self.dark_overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.dark_overlay.fill((0, 0, 0))
        self.dark_overlay.set_alpha(100)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.selecionada = None
        self.movimentos = None
        self.turno = 0
        self.vencedor = None
        self.jogador1 = 'Branco'
        self.jogador2 = 'Preto'
        self.mode = mode
        self.bot = Bot()
        self.config = Config.load_config()

        if self.mode == ONE_PLAYER:
            self.bot.set_name(nome_bot)
            self.bot.set_style(GameStyle.load_style(nome_bot + ".json"))
            self.bot.load_learning(nome_bot + "_data.txt")
            sprite = pygame.image.load('Assets/Pecas/' + nome_bot + '.png')
        else:
            # pega o ultimo caractere da string
            skin = int(self.config.skin[-1]) % 8 + 1
            sprite = pygame.image.load('Assets/Pecas/Player' + str(skin) + '.png')

        sprite = pygame.transform.scale(sprite, (TAMANHO_CASA * 2, TAMANHO_CASA))
        self.sprite_pretas = sprite.subsurface((0, 0, TAMANHO_CASA, TAMANHO_CASA))
        self.sprite_dama_pretas = sprite.subsurface((TAMANHO_CASA, 0, TAMANHO_CASA, TAMANHO_CASA))

        sprite = pygame.image.load('Assets/Pecas/' + self.config.skin + '.png')
        sprite = pygame.transform.scale(sprite, (TAMANHO_CASA * 2, TAMANHO_CASA))
        self.sprite_brancas = sprite.subsurface((0, 0, TAMANHO_CASA, TAMANHO_CASA))
        self.sprite_dama_brancas = sprite.subsurface((TAMANHO_CASA, 0, TAMANHO_CASA, TAMANHO_CASA))

    def inicializarJogo(self):
        try:
            self.carregar_jogo()
        except FileNotFoundError:
            self.inicializar_tabuleiro()

    def inicializar_tabuleiro(self):
        if not self.tabuleiroCarregado:
            self.board = [[CASA_VAZIA for _ in range(8)] for _ in range(8)]
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

    def salvar_jogo(self, turno, tempocorrido, tabuleiro, nome_arquivo="jogo_salvo.txt"):
        with open(nome_arquivo, "w") as arquivo:
            # Salvando turno
            arquivo.write("#turno\n")
            arquivo.write(f"{turno}\n\n")

            # Salvando tempo corrido
            arquivo.write("#tempocorrido\n")
            arquivo.write(f"{tempocorrido}\n\n")

            # Salvando tabuleiro
            arquivo.write("#tabuleiro\n")
            for i in range(8):
                for j in range(8):
                    arquivo.write(str(self.board[i][j]) + ' ')
                arquivo.write('\n')

    def carregar_jogo(self, nome_arquivo="jogo_salvo.txt"):
        with open(nome_arquivo, "r") as arquivo:
            linhas = arquivo.readlines()

        turnoP = None
        tempoCorridoSalvo = None

        # Processar linhas do arquivo
        i = 0
        while i < len(linhas):
            linha = linhas[i].strip()

            if linha == "#turno":
                i += 1
                turnoP = int(linhas[i].strip())

            elif linha == "#tempocorrido":
                i += 1
                tempoCorridoSalvo = int(linhas[i].strip())

            elif linha == "#tabuleiro":
                i += 1
                self.board = [[int(cell.strip()) for cell in line.split()]
                              for line in arquivo]

            i += 1
        self.turno = turnoP
        self.tempocorrido = tempoCorridoSalvo
        self.tabuleiroCarregado = True

    def desenhar_tabuleiro(self):
        x = SCREEN_WIDTH // 2 - 4 * TAMANHO_CASA
        y = SCREEN_HEIGHT // 2 - 4 * TAMANHO_CASA
        cont = 0
        for i in range(8):
            for j in range(8):
                if cont % 2 == 0 and i % 2 == 0 or cont % 2 != 0 and i % 2 != 0:
                    pygame.draw.rect(self.screen, (255, 255, 255),
                                     (x + j * TAMANHO_CASA, y + i * TAMANHO_CASA, TAMANHO_CASA, TAMANHO_CASA))
                else:
                    pygame.draw.rect(self.screen, (0, 0, 0),
                                     (x + j * TAMANHO_CASA, y + i * TAMANHO_CASA, TAMANHO_CASA, TAMANHO_CASA))

                if self.board[i][j] == PECA_BRANCA:
                    self.screen.blit(self.sprite_brancas, (x + j * TAMANHO_CASA, y + i * TAMANHO_CASA))
                elif self.board[i][j] == PECA_PRETA:
                    self.screen.blit(self.sprite_pretas, (x + j * TAMANHO_CASA, y + i * TAMANHO_CASA))
                elif self.board[i][j] == PECA_BRANCA_SELECIONADA:
                    pygame.draw.rect(self.screen, (255, 0, 0),
                                     (x + j * TAMANHO_CASA, y + i * TAMANHO_CASA, TAMANHO_CASA, TAMANHO_CASA))
                    self.screen.blit(self.sprite_brancas, (x + j * TAMANHO_CASA, y + i * TAMANHO_CASA))
                elif self.board[i][j] == PECA_PRETA_SELECIONADA:
                    pygame.draw.rect(self.screen, (255, 0, 0),
                                     (x + j * TAMANHO_CASA, y + i * TAMANHO_CASA, TAMANHO_CASA, TAMANHO_CASA))
                    self.screen.blit(self.sprite_pretas, (x + j * TAMANHO_CASA, y + i * TAMANHO_CASA))

                if self.board[i][j] == PECA_BRANCA_DAMA:
                    self.screen.blit(self.sprite_dama_brancas, (x + j * TAMANHO_CASA, y + i * TAMANHO_CASA))
                elif self.board[i][j] == PECA_PRETA_DAMA:
                    self.screen.blit(self.sprite_dama_pretas, (x + j * TAMANHO_CASA, y + i * TAMANHO_CASA))
                elif self.board[i][j] == PECA_BRANCA_DAMA_SELECIONADA:
                    pygame.draw.rect(self.screen, (255, 0, 0),
                                     (x + j * TAMANHO_CASA, y + i * TAMANHO_CASA, TAMANHO_CASA, TAMANHO_CASA))
                    self.screen.blit(self.sprite_dama_brancas, (x + j * TAMANHO_CASA, y + i * TAMANHO_CASA))
                elif self.board[i][j] == PECA_PRETA_DAMA_SELECIONADA:
                    pygame.draw.rect(self.screen, (255, 0, 0),
                                     (x + j * TAMANHO_CASA, y + i * TAMANHO_CASA, TAMANHO_CASA, TAMANHO_CASA))
                    self.screen.blit(self.sprite_dama_pretas, (x + j * TAMANHO_CASA, y + i * TAMANHO_CASA))
                if self.board[i][j] == CASA_MOVIMENTO:
                    pygame.draw.circle(self.screen, (0, 255, 0), (x + j * TAMANHO_CASA + 50, y + i * TAMANHO_CASA + 50), 12)
                cont += 1

    def board_to_state(self):
        return tuple(tuple(row) for row in self.board)

    def get_all_possible_moves_for_bot(self):
        possible_moves = []

        for i in range(8):
            for j in range(8):
                if self.board[i][j] in [PECA_PRETA, PECA_PRETA_DAMA]:
                    moves = Movimento.calcular_movimentos_possiveis(self.board, self.board[i][j])
                    if moves is not None:
                        for move in moves:
                            if move.i == i and move.j == j:
                                possible_moves.append(move)
        return possible_moves

    def bot_move(self):
        state = self.board_to_state()
        actions = self.get_all_possible_moves_for_bot()
        action = self.bot.choose_action(state, actions)
        self.apply_move(action)

        next_state = self.board_to_state()
        reward = self.calculate_reward(state, next_state)
        next_actions = self.get_all_possible_moves_for_bot()
        self.bot.update_q_value(state, action, reward, next_state, next_actions)

    @staticmethod
    def deletar_arquivo_tabuleiro():
        try:
            os.remove('tabuleiroSalvo.txt')
        except FileNotFoundError:
            pass

    def run(self):
        clock = pygame.time.Clock()
        self.running = True
        while self.running:

            if self.vencedor is None and self.turno % 2 == 1 and self.mode == ONE_PLAYER:
                self.bot_move()
                self.turno += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if voltarButton.collidepoint(event.pos):
                        self.salvar_jogo(self.turno, self.tempoTotal, self.board, 'tabuleiroSalvo.txt')
                        running = False
                    elif empateButton.collidepoint(event.pos):
                        pass
                    elif desistirButton.collidepoint(event.pos):
                        self.deletar_arquivo_tabuleiro()
                        self.running = False
                    else:
                        x, y = pygame.mouse.get_pos()
                        self.selecionar_peca(x, y)

            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.dark_overlay, (0, 0))

            voltarButton = pygame.Rect(10, SCREEN_HEIGHT - 70, 160, 40)
            desenharBotao(voltarButton, corVermelha, "Voltar", fonteMedia, corBranca, self.screen, 2, 160, 40)

            empateButton = pygame.Rect(SCREEN_WIDTH - 180, SCREEN_HEIGHT - 130, 160, 40)
            desenharBotao(empateButton, corVermelha, "Pedir Empate", fonteMedia, corBranca, self.screen, 2, 160, 40)

            desistirButton = pygame.Rect(SCREEN_WIDTH - 180, SCREEN_HEIGHT - 70, 160, 40)
            desenharBotao(desistirButton, corVermelha, "Desistir", fonteMedia, corBranca, self.screen, 2, 160, 40)

            self.desenhar_tabuleiro()

            tempoCorrente = pygame.time.get_ticks()
            if self.tempoInicial is None:
                self.tempoInicial = tempoCorrente
            elapsed_time = tempoCorrente - self.tempoInicial
            self.tempoTotal += timedelta(milliseconds=elapsed_time)

            hours, remainder = divmod(self.tempoTotal.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)

            font = pygame.font.Font(None, 36)
            text = font.render(f"{int(hours):02d}:{minutes:02d}:{seconds:02d}", True, (255, 255, 255))
            self.screen.blit(text, (10, 10))

            if self.vencedor is not None:
                font = pygame.font.Font(None, 74)
                text = font.render(f'Vencedor: {self.vencedor}', True, (255, 255, 255))
                self.screen.blit(text, (200, 300))
            pygame.display.flip()
            clock.tick(FPS)

    def selecionar_peca(self, x, y):

        i = (y - (SCREEN_HEIGHT // 2 - 4 * TAMANHO_CASA)) // TAMANHO_CASA
        j = (x - (SCREEN_WIDTH // 2 - 4 * TAMANHO_CASA)) // TAMANHO_CASA

        if i < 0 or i >= 8 or j < 0 or j >= 8:
            return

        if self.turno % 2 == 0:
            if color(self.board[i][j]) == PECA_PRETA:
                return
        else:
            if color(self.board[i][j]) == PECA_BRANCA:
                return
        print(f'Peça selecionada: {i} {j}')

        if self.board[i][j] == CASA_VAZIA:
            self.desmarcar_selecionada()
            return

        if self.board[i][j] == CASA_MOVIMENTO:
            self.print_tabuleiro()
            self.mover_peca(i, j)
            self.turno += 1
            cont_branca = self.num_pecas(PECA_BRANCA)
            if cont_branca == 0:
                resultadoModal = ResultadoModal(self.screen, False)
                resposta = resultadoModal.run()
                if resposta == "menu":
                    self.running = False
                    return
                elif resposta == "rematch":
                    self.rematch()
                    return

            cont_preta = self.num_pecas(PECA_PRETA)
            if cont_preta == 0:
                resultadoModal = ResultadoModal(self.screen, True)
                resposta = resultadoModal.run()
                if resposta == "menu":
                    self.running = False
                    return
                elif resposta == "rematch":
                    self.rematch()
                    return
            return

        self.desmarcar_selecionada()
        self.print_tabuleiro()
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
        movimentos = Movimento.calcular_movimentos_possiveis(self.board, self.board[i][j])
        if movimentos is None or len(movimentos) == 0:
            self.vencedor = self.jogador2 if self.turno % 2 == 0 else self.jogador1
            print(f'Vencedor: {self.vencedor}')
            return

        self.movimentos = []
        for movimento in movimentos:
            if movimento.i == i and movimento.j == j:
                self.movimentos.append(movimento)

        if len(self.movimentos) == 0:
            print('Nenhum movimento possível')
            return

        for movimento in self.movimentos:
            i_aux = movimento.i_final
            j_aux = movimento.j_final
            print(f'Movimento: {i} {j} -> {i_aux} {j_aux}')
            self.board[i_aux][j_aux] = CASA_MOVIMENTO

    def num_pecas(self, cor):
        cont = 0
        for i in range(8):
            for j in range(8):
                if color(self.board[i][j]) == color(cor):
                    cont += 1
        return cont

    def apply_move(self, action):
        self.board[action.i_final][action.j_final] = self.board[action.i][action.j]
        self.board[action.i][action.j] = CASA_VAZIA

        if action.tipo_movimento == MOVIMENTO_COMER:
            self.board[action.peca_comida_i][action.peca_comida_j] = CASA_VAZIA

        if self.board[action.i_final][action.j_final] == PECA_PRETA and action.i_final == 7:
            self.board[action.i_final][action.j_final] = PECA_PRETA_DAMA
        elif self.board[action.i_final][action.j_final] == PECA_BRANCA and action.i_final == 0:
            self.board[action.i_final][action.j_final] = PECA_BRANCA_DAMA

    def calculate_reward(self, state, next_state):
        reward = 0

        if self.vencedor == self.jogador2:
            return self.bot.style.ganhar
        elif self.vencedor == self.jogador1:
            return self.bot.style.perder

        if state.count(PECA_BRANCA) + state.count(PECA_BRANCA_DAMA) > next_state.count(PECA_BRANCA) + next_state.count(PECA_BRANCA_DAMA):
            reward += self.bot.style.comer
        elif state.count(PECA_PRETA) + state.count(PECA_PRETA_DAMA) < next_state.count(PECA_PRETA) + next_state.count(PECA_PRETA_DAMA):
            reward += self.bot.style.perder_peca

        if state.count(PECA_BRANCA_DAMA) < next_state.count(PECA_BRANCA_DAMA):
            reward += self.bot.style.inimigo_fazer_dama
        elif state.count(PECA_PRETA_DAMA) < next_state.count(PECA_PRETA_DAMA):
            reward += self.bot.style.virar_dama

        if state.count(PECA_BRANCA_DAMA) > next_state.count(PECA_BRANCA_DAMA):
            reward += self.bot.style.tomar_dama

        if state.count(PECA_PRETA_DAMA) > next_state.count(PECA_PRETA_DAMA):
            reward += self.bot.style.perder_dama

        return reward

    def rematch(self):
        self.tabuleiroCarregado = False
        self.inicializar_tabuleiro()
        self.turno = 0
        self.vencedor = None
        self.tempoInicial = None
        self.tempoTotal = timedelta(seconds=0)
        self.desmarcar_selecionada()
        self.run()












