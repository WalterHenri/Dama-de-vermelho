import pygame
import sys
from Constants import *
from Damas import Damas
from DrawTools import *


class MenuAdversarios:
    def __init__(self):
        pygame.init()
        self.background = pygame.image.load('Assets/background.jpg')
        self.dark_overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.dark_overlay.fill((0, 0, 0))
        self.dark_overlay.set_alpha(100)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Dama de Vermelho')

        self.adversarios = [
            {"nome": "Alcides", "dificuldade": 5, "Descricao": "Gosta de andar de skate e tocar teclado, mas tenha cuidado, sua grande habilidade em aprendizado por reforco o tornara um adversario duro de enfrentar",
             "pathFoto": 'Assets/alcides.jpg'},
            {"nome": "Raphael", "dificuldade": 3, "Descricao": "Amigavel e divertido, esse guitarriista provavelmente vai dar um show no tabuleiro",
             "pathFoto": 'Assets/raphael.jpg'},
            {"nome": "Methanias", "dificuldade": 5,
             "Descricao": "Amante das palavras e das mulheres, esse doutor, poetista e hedonista fara de tudo para colocar o maximo de damas possiveis em seu tabuleiro ",
             "pathFoto": 'Assets/methanias.jpeg'},
            {"nome": "Joseval", "dificuldade": 4,
             "Descricao": "DOUTOR Joseval, como gosta de ser chamado nao perdera para um simples mortal, suas capacidades defensivas vao alem da sua propria vontade de ganhar tornando apenas uma vontade de nao perder",
             "pathFoto": 'Assets/joseval.jpg'},
        ]
        self.adversarioSelecionado = 0

    def run(self):
        running = True

        while running:
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.dark_overlay, (0, 0))
            desenharTexto("Selecione o adversario", fonte_titulo, corBranca, self.screen, 50, 20)

            sairButton = pygame.Rect(50, SCREEN_HEIGHT - 100, 165, 40)
            desenharBotao(sairButton, corVermelha, "Sair", fonteGrande, corPreta, self.screen, 2, 165, 40)

            avancarButton = pygame.Rect(SCREEN_WIDTH - 200, SCREEN_HEIGHT - 100, 165, 40)
            desenharBotao(avancarButton, corVermelha, "Prosseguir", fonteGrande, corPreta, self.screen, 2, 165, 40)

            for i, adversario in enumerate(self.adversarios):
                posicaoY = 220 + i * 50
                button = pygame.Rect(90, posicaoY, 200, 40)
                if i == self.adversarioSelecionado:
                    cor = corVermelha
                else:
                    cor = corCinza
                desenharBotao(button, cor, adversario['nome'], fonteGrande, corPreta, self.screen, 2, 200, 40)

            areaDescricao = pygame.Rect(SCREEN_WIDTH / 2, 100, 450, 500)
            pygame.draw.rect(self.screen, corVermelhoEscuro, areaDescricao, border_radius=2)

            desenharTexto(self.adversarios[self.adversarioSelecionado]["nome"], fonteGrande, corBranca, self.screen,
                          areaDescricao.x, areaDescricao.y + 10, 450, 40)
            desenharTexto(self.adversarios[self.adversarioSelecionado]["Descricao"], fontePequena, corBranca,
                          self.screen, areaDescricao.x + 10, areaDescricao.y + 350, largura=400, larguraMaxima=400)

            imagemOriginal = pygame.image.load(self.adversarios[self.adversarioSelecionado]["pathFoto"])
            larguraImagem, alturaImagem = 250, 250
            imagemAdversario = pygame.transform.scale(imagemOriginal, (larguraImagem, alturaImagem))
            self.screen.blit(imagemAdversario,
                             ((areaDescricao.width - larguraImagem) / 2 + areaDescricao.x, areaDescricao.y + 80))
            desenharTexto("Dificuldade", fonteMedia, corBranca, self.screen, areaDescricao.x + 10, areaDescricao.y + 45)
            for indexStar in range(self.adversarios[self.adversarioSelecionado]["dificuldade"]):
                estrela = pygame.image.load('Assets/star.png')
                larguraEstrela, alturaEstrela = 30, 30
                imagemEstrela = pygame.transform.scale(estrela, (larguraEstrela, alturaEstrela))
                self.screen.blit(imagemEstrela, (
                    (areaDescricao.x + areaDescricao.width) - (indexStar * larguraEstrela + 40), areaDescricao.y + 40))

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    running = False
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    if sairButton.collidepoint(evento.pos):
                        running = False
                    elif avancarButton.collidepoint(evento.pos):
                        return self.start_game(self.adversarios[self.adversarioSelecionado]["nome"])
                    for indiceListaAdversario in range(len(self.adversarios)):
                        posicaoVertical = 220 + indiceListaAdversario * 50
                        botao = pygame.Rect(90, posicaoVertical, 200, 40)
                        if botao.collidepoint(evento.pos):
                            self.adversarioSelecionado = indiceListaAdversario

            pygame.display.flip()

    @staticmethod
    def start_game(nome_adversario):
        game = Damas(ONE_PLAYER, nome_adversario)
        game.run()
