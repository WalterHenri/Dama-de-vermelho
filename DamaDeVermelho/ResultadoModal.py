import pygame
from Constants import *
from DrawTools import *


class ResultadoModal:
    def __init__(self, screen, resultado):
        self.screen = screen
        self.resultado = resultado

    def run(self):
        running = True
        while running:
            if self.resultado:
                desenharTexto("Voce Ganhou!", fonte_tituloGG, corVermelha, self.screen, 50, 20, largura=SCREEN_WIDTH,
                              altura=200)
                desenharTexto("Voce Ganhou!", fonte_tituloGrande, corBranca, self.screen, 50, 20, largura=SCREEN_WIDTH,
                              altura=200)
            else:
                desenharTexto("Voce Perdeu", fonte_tituloGG, corVermelha, self.screen, 50, 20, largura=SCREEN_WIDTH,
                              altura=200)
                desenharTexto("Voce Perdeu", fonte_tituloGrande, corBranca, self.screen, 50, 20, largura=SCREEN_WIDTH,
                              altura=200)

            menuInicialButton = pygame.Rect((SCREEN_WIDTH - 165) / 2, 400, 165, 40)
            desenharBotao(menuInicialButton, corVermelha, "Voltar ao Inicio", fonteMedia, corBranca, self.screen, 10,
                          165, 40)

            rematchButton = pygame.Rect((SCREEN_WIDTH - 165) / 2, 460, 165, 40)
            desenharBotao(rematchButton, corVermelha, "Revanche", fonteMedia, corBranca, self.screen, 10,
                          165, 40)
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    running = False
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    if menuInicialButton.collidepoint(evento.pos):
                        return "menu"
                    elif rematchButton.collidepoint(evento.pos):
                        return "rematch"

            pygame.display.flip()
