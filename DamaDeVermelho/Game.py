import pygame
from Constants import *


class Game:
    def __init__(self):
        pygame.init()
        self.background = pygame.image.load('Assets/background.jpg')
        self.dark_overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.dark_overlay.fill((0, 0, 0))  # Preenchendo de preto
        self.dark_overlay.set_alpha(100)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.title = 'Dama de Vermelho'
        pygame.display.set_caption(self.title)
        self.fonte_titulo = pygame.font.Font('Fonts/Nightcore Demo.ttf', 80)
        self.fonte_menu = pygame.font.Font('Fonts/The Wild Breath of Zelda.otf', 30)
        self.running = True

    def draw_title(self):
        titulo = self.fonte_titulo.render(self.title, True, (255, 255, 255))
        self.screen.blit(titulo, (SCREEN_WIDTH // 4 - titulo.get_width() // 3, titulo.get_height() // 2))

    def run(self):
        while self.running:
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.dark_overlay, (0, 0))
            self.draw_title()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            pygame.display.update()
            self.clock.tick(FPS)
        pygame.quit()
        quit()



