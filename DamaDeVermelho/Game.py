import MenuAdversarios
from Constants import *
import pygame

from Damas import Damas


def play_action():
    game = Damas()
    game.run()


def bots_action():
    menu = MenuAdversarios.MenuAdversarios()
    menu.run()


class Game:
    def __init__(self):
        pygame.init()
        self.background = pygame.image.load('Assets/background.jpg')
        self.dark_overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.dark_overlay.fill((0, 0, 0))
        self.dark_overlay.set_alpha(100)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.title = 'Damas de Vermelho'
        pygame.display.set_caption(self.title)
        self.fonte_titulo = pygame.font.Font('Fonts/Nightcore Demo.ttf', 80)
        self.fonte_menu = pygame.font.Font('Fonts/The Wild Breath of Zelda.otf', 30)

        self.buttons = {
            'play': pygame.Rect(SCREEN_WIDTH // 1.5, 200, 200, 50),
            'settings': pygame.Rect(SCREEN_WIDTH // 1.5, 270, 200, 50),
            'bots': pygame.Rect(SCREEN_WIDTH // 1.5, 340, 200, 50),
            'exit': pygame.Rect(SCREEN_WIDTH // 1.5, 410, 200, 50)
        }
        self.button_actions = {
            'play': play_action,
            'settings': self.settings_action,
            'bots': bots_action,
            'exit': self.exit_action
        }
        self.running = True

    def draw_title(self):
        titulo = self.fonte_titulo.render(self.title, True, (255, 255, 255))
        self.screen.blit(titulo, (SCREEN_WIDTH // 4 - titulo.get_width() // 3, titulo.get_height() // 2))

    def draw_buttons(self):
        button_texts = {
            'play': 'Jogar',
            'settings': 'Configuracoes',
            'bots': 'Inimigos',
            'exit': 'Sair'
        }

        for key, rect in self.buttons.items():
            color = (200, 0, 0) if rect.collidepoint(pygame.mouse.get_pos()) else (255, 0, 0)
            pygame.draw.rect(self.screen, color, rect)
            text = self.fonte_menu.render(button_texts[key], True, (255, 255, 255))
            self.screen.blit(
                text,
                (rect.x + rect.width // 2 - text.get_width() // 2,
                 rect.y + rect.height // 2 - text.get_height() // 2)
            )

    def handle_button_clicks(self, pos):
        for key, rect in self.buttons.items():
            if rect.collidepoint(pos):
                self.button_actions[key]()

    def settings_action(self):
        pass

    def exit_action(self):
        self.running = False

    def run(self):
        while self.running:
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.dark_overlay, (0, 0))
            self.draw_title()
            self.draw_buttons()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_button_clicks(event.pos)

            pygame.display.update()
            self.clock.tick(FPS)

        pygame.quit()



