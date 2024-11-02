import Game
import GameStyle


def salvar_estilos():
    # estilo methanias
    style = GameStyle.GameStyle(10000, 1, 10000, 1, 10000, -10000, -1, -200, 200, 0)
    style.save_style('methanias.json')
    # estilo alcides
    style = GameStyle.GameStyle(1000, -100, 1000, -100, 10000, -100)
    style.save_style('alcides.json')
    # estilo joseval
    style = GameStyle.GameStyle(1, -1000, 1, -1000, -1, -1000000, 0, -100000, 100, -100000)
    style.save_style('joseval.json')
    # estilo raphael
    style = GameStyle.GameStyle(100, -100, 100, -100, 100, -100, 0, -100, 100, 0)
    style.save_style('raphael.json')


if __name__ == '__main__':
    salvar_estilos()
    game = Game.Game()
    game.run()
