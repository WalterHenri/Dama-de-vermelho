import pygame
from Constants import *
from DrawTools import *

class Resultado:
    def __init__(self):
        pygame.init()
        self.background = pygame.image.load('Assets/background.jpg')
        self.dark_overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.dark_overlay.fill((0, 0, 0))
        self.dark_overlay.set_alpha(100)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Dama de Vermelho')

    def run(self, resultado):
        running = True
        while running:
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.dark_overlay, (0, 0))

            if resultado == True:
                desenharTexto("Voce Ganhou!", fonte_tituloGrande, corBranca, self.screen, 50, 20, largura=SCREEN_WIDTH, altura=200)
            else:
                desenharTexto("Voce Perdeu", fonte_tituloGrande, corBranca, self.screen, 50, 20, largura=SCREEN_WIDTH, altura=200)


            menuInicialButton = pygame.Rect((SCREEN_WIDTH - 165)/2, 400, 165, 40)
            desenharBotao(menuInicialButton, corVermelha, "Voltar ao Inicio", fonteMedia, corBranca, self.screen, 10,
                          165, 40)

            rematchButton = pygame.Rect((SCREEN_WIDTH - 165)/2, 460, 165, 40)
            desenharBotao(rematchButton, corVermelha, "Revanche", fonteMedia, corBranca, self.screen, 10,
                          165, 40)
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    running = False
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    if menuInicialButton.collidepoint(evento.pos):
                        running = False
                    elif rematchButton.collidepoint(evento.pos):
                        #chamar partida de revanche
                        pass

            pygame.display.flip()
