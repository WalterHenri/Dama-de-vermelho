import pygame

pygame.init()
#definindo as cores
corBranca = (255, 255, 255)
corCinza = (220, 220, 220)
corCinzaEscuro = (150, 150, 150)
corAzul = (0, 150, 255)
corVermelha = (255, 0, 0)
corVermelhoEscuro = (53, 3, 1)
corRosa = (255, 0, 255)
corPreta = (0, 0, 0)

#definindo as fontes
fonte_titulo = pygame.font.Font('Fonts/Nightcore Demo.ttf', 60)
fonteGrande = pygame.font.Font('Fonts/The Wild Breath of Zelda.otf', 30)
fonteMedia = pygame.font.Font('Fonts/The Wild Breath of Zelda.otf', 25)
fontePequena = pygame.font.Font('Fonts/The Wild Breath of Zelda.otf', 20)

#para por texto na tela, os dois ultimos parametros só devem ser informados caso deseje deixar o texto centralizado
def desenharTexto(texto, fonte, cor, superficie, x, y, largura=0, altura=0):
    text_obj = fonte.render(texto, True, cor)
    text_Rect = text_obj.get_rect()
    if largura > 0 and altura > 0:
        text_Rect.topleft = ((largura - text_obj.get_width()) / 2 + x, (altura - text_obj.get_height()) / 2 + y)
    else:
        text_Rect.topleft = (x, y)
    superficie.blit(text_obj, text_Rect)

#desenha um botao, havendo a possibilidade de por uma borda arredondada, os dois ultimos parametros só devem ser informados caso o texto do botao deva ficar centralizado
def desenharBotao(retangulo, cor, texto, fonte, corTexto, superficie, borderRadius=10, larguraTexto  = 0, alturaTexto = 0):
    pygame.draw.rect(superficie, cor, retangulo, border_radius=borderRadius)
    desenharTexto(texto, fonte, corTexto, superficie, retangulo.x, retangulo.y, larguraTexto, alturaTexto)