import pygame
import sys
from Constants import *

class MenuAdversarios:
    def __init__(self):
        pygame.init()
        self.background = pygame.image.load('Assets/background.jpg')
        self.dark_overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.dark_overlay.fill((0, 0, 0))
        self.dark_overlay.set_alpha(100)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Dama de Vermelho')

        #definindo as cores
        self.corBranca = (255, 255, 255)
        self.corCinza = (220, 220, 220)
        self.corCinzaEscuro = (150, 150, 150)
        self.corAzul = (0, 150, 255)
        self.corVermelha = (255, 0, 0)
        self.corRosa = (255, 0, 255)
        self.corPreta = (0, 0, 0)

        #definindo as fontes
        self.fonte_titulo = pygame.font.Font('Fonts/Nightcore Demo.ttf', 60)
        self.fonte_menu = pygame.font.Font('Fonts/The Wild Breath of Zelda.otf', 30)
        self.fonte_descricao = pygame.font.Font('Fonts/The Wild Breath of Zelda.otf', 20)

        #adversarios
        self.adversarios = [
            {"nome": "Alcides", "dificuldade": 1, "Descricao": "Imagine uma grande descrição"},
            {"nome": "Raphael", "dificuldade": 3, "Descricao": "Imagine uma grande descrição"},
            {"nome": "Methanias", "dificuldade": 5, "Descricao": "Imagine uma grande descrição"},
            {"nome": "Joseval", "dificuldade": 4, "Descricao": "Imagine uma grande descrição"},
            {"nome": "Dosea", "dificuldade": 5, "Descricao": "Imagine uma grande descrição"},

        ]
        self.adversarioSelecionado = 0

    def desenharTexto(self, texto, fonte, cor, superficie, x, y, largura = 0, altura = 0):
        text_obj = fonte.render(texto, True, cor)
        text_Rect = text_obj.get_rect()
        if largura > 0 and altura > 0:
            text_Rect.topleft = ((largura - text_obj.get_width())/2 + x, (altura - text_obj.get_height())/2 + y)
        else:
            text_Rect.topleft = (x, y)
        superficie.blit(text_obj, text_Rect)

    def desenharBotao(self, retangulo, cor, texto, fonte, corTexto, superficie, borderRadius=10):
        pygame.draw.rect(superficie, cor, retangulo, border_radius=borderRadius)
        self.desenharTexto(texto, fonte, corTexto, superficie, retangulo.x + (20), retangulo.y + 7)

    def run(self):
        running = True

        while running:
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.dark_overlay, (0, 0))
            self.desenharTexto("Selecione o adversário", self.fonte_titulo, self.corBranca, self.screen, 50, 20)

            sairButton = pygame.Rect(50, SCREEN_HEIGHT - 100, 95, 40)
            self.desenharBotao(sairButton, self.corVermelha, "Sair", self.fonte_menu, self.corPreta, self.screen, 2)

            avancarButton = pygame.Rect(SCREEN_WIDTH - 200, SCREEN_HEIGHT - 100, 165, 40)
            self.desenharBotao(avancarButton, self.corVermelha, "Prosseguir", self.fonte_menu, self.corPreta, self.screen, 2)

            for i, adversario in enumerate(self.adversarios):
                posicaoY = 220 + i * 50
                button = pygame.Rect(50, posicaoY, 155, 40)
                if i == self.adversarioSelecionado:
                    cor = self.corVermelha
                else:
                    cor = self.corCinza
                self.desenharBotao(button, cor, adversario['nome'], self.fonte_menu, self.corPreta, self.screen, 2)

            #area da descrição
            areaDescricao = pygame.Rect(SCREEN_WIDTH/2, 100, 450, 500)
            pygame.draw.rect(self.screen, self.corCinzaEscuro, areaDescricao)
            pygame.draw.rect(self.screen, self.corCinzaEscuro, areaDescricao)

            #nome do adversario
            self.desenharTexto(self.adversarios[self.adversarioSelecionado]["nome"], self.fonte_menu, self.corPreta, self.screen, areaDescricao.x, areaDescricao.y + 10, 450, 40)
            self.desenharTexto(self.adversarios[self.adversarioSelecionado]["Descricao"], self.fonte_descricao, self.corPreta, self.screen, areaDescricao.x + 10, areaDescricao.y + 400, )

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    running = False
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    if sairButton.collidepoint(evento.pos):
                        pygame.quit()
                        sys.exit()
                    elif avancarButton.collidepoint(evento.pos):
                        print(
                            f"avançando para a proxima etapa, adversário {self.adversarios[self.adversarioSelecionado]["nome"]}")
                    for indiceListaAdversario in range(len(self.adversarios)):
                        posicaoVertical = 220 + indiceListaAdversario * 50
                        botao = pygame.Rect(50, posicaoVertical, 155, 40)
                        if botao.collidepoint(evento.pos):
                            self.adversarioSelecionado = indiceListaAdversario

            pygame.display.flip()
        pygame.quit()
