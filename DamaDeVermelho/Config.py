import json
import pygame
from DrawTools import *

from Constants import *


class ConfigScreen:
    def __init__(self):
        self.config = Config.load_config()
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Configuracoes')
        self.background = pygame.image.load('Assets/background.jpg')
        self.dark_overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.dark_overlay.fill((0, 0, 0))
        self.dark_overlay.set_alpha(100)
        self.skin = self.config.skin
        self.volume = self.config.volume
        self.sprites = {
            "Player1": pygame.image.load('Assets/Pecas/Player1.png'),
            "Player2": pygame.image.load('Assets/Pecas/Player2.png'),
            "Player3": pygame.image.load('Assets/Pecas/Player3.png'),
            "Player4": pygame.image.load('Assets/Pecas/Player4.png'),
            "Player5": pygame.image.load('Assets/Pecas/Player5.png'),
            "Player6": pygame.image.load('Assets/Pecas/Player6.png'),
            "Player7": pygame.image.load('Assets/Pecas/Player7.png'),
            "Player8": pygame.image.load('Assets/Pecas/Player8.png'),
        }
        self.button_left = pygame.Rect(50, 200, 50, 50)
        self.button_right = pygame.Rect(SCREEN_WIDTH - 100, 200, 50, 50)
        self.button_volume_left = pygame.Rect(50, 300, 50, 50)
        self.button_volume_right = pygame.Rect(SCREEN_WIDTH - 100, 300, 50, 50)
        self.button_save = pygame.Rect(SCREEN_WIDTH / 2 - 100, 400, 200, 50)
        self.button_back = pygame.Rect(SCREEN_WIDTH / 2 - 100, 500, 200, 50)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button_left.collidepoint(event.pos):
                        self.skin = self.get_previous_skin()
                    elif self.button_right.collidepoint(event.pos):
                        self.skin = self.get_next_skin()
                    elif self.button_volume_left.collidepoint(event.pos):
                        self.volume = max(0, self.volume - 0.1)
                    elif self.button_volume_right.collidepoint(event.pos):
                        self.volume = min(1, self.volume + 0.1)
                    elif self.button_save.collidepoint(event.pos):
                        self.config.skin = self.skin
                        self.config.volume = self.volume
                        self.config.save_config()
                    elif self.button_back.collidepoint(event.pos):
                        return
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.dark_overlay, (0, 0))
            desenharTexto("Configuracoes", fonte_titulo, corBranca, self.screen, 50, 20)
            desenharTexto("Skin", fonteMedia, corBranca, self.screen, 50, 200)
            self.screen.blit(self.sprites[self.skin], (SCREEN_WIDTH / 2 - 50, 200))
            desenharTexto("Volume", fonteMedia, corBranca, self.screen, 50, 300)
            desenharTexto(f"{self.volume:.1f}", fonteMedia, corBranca, self.screen, SCREEN_WIDTH / 2 - 50, 300)
            desenharBotao(self.button_left, corVermelha, "<", fonteMedia, corBranca, self.screen, 2, 50, 50)
            desenharBotao(self.button_right, corVermelha, ">", fonteMedia, corBranca, self.screen, 2, 50, 50)
            desenharBotao(self.button_volume_left, corVermelha, "<", fonteMedia, corBranca, self.screen, 2, 50, 50)
            desenharBotao(self.button_volume_right, corVermelha, ">", fonteMedia, corBranca, self.screen, 2, 50, 50)
            desenharBotao(self.button_save, corVermelha, "Salvar", fonteMedia, corBranca, self.screen, 2, 200, 50)
            desenharBotao(self.button_back, corVermelha, "Voltar", fonteMedia, corBranca, self.screen, 2, 200, 50)
            pygame.display.flip()

    def get_previous_skin(self):
        skins = list(self.sprites.keys())
        index = skins.index(self.skin)
        return skins[index - 1] if index > 0 else skins[-1]

    def get_next_skin(self):
        skins = list(self.sprites.keys())
        index = skins.index(self.skin)
        return skins[index + 1] if index < len(skins) - 1 else skins[0]


class Config:
    def __init__(self, skin="Player1", volume=0.5):
        self.skin = skin
        self.volume = volume

    def save_config(self, filename='config.json'):
        with open(filename, 'w') as f:
            json.dump(self.__dict__, f)

    @staticmethod
    def load_config(filename='config.json'):
        try:
            with open(filename, 'r') as f:
                config = json.load(f)
            return Config(**config)
        except FileNotFoundError:
            return Config()
