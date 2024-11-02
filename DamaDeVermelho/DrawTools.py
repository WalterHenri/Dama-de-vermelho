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
fonte_tituloGrande = pygame.font.Font('Fonts/Nightcore Demo.ttf', 90)
fonteGrande = pygame.font.Font('Fonts/The Wild Breath of Zelda.otf', 30)
fonteMedia = pygame.font.Font('Fonts/The Wild Breath of Zelda.otf', 25)
fontePequena = pygame.font.Font('Fonts/The Wild Breath of Zelda.otf', 20)

#para por texto na tela, os dois ultimos parametros só devem ser informados caso deseje deixar o texto centralizado
def desenharTexto(texto, fonte, cor, superficie, x, y, largura=0, altura=0, larguraMaxima = 1000):
    text_obj = fonte.render(texto, True, cor)
    text_Rect = text_obj.get_rect()
    if largura > 0 and altura > 0:
        text_Rect.topleft = ((largura - text_obj.get_width()) / 2 + x, (altura - text_obj.get_height()) / 2 + y)
    else:
        text_Rect.topleft = (x, y)

    max_width = larguraMaxima
    lines = wrap_text(texto, fonte, max_width)

    # Desenha cada linha separadamente
    for i, line in enumerate(lines):
        text_obj = fonte.render(line, True, cor)
        line_rect = text_obj.get_rect()

        if largura > 0 and altura > 0:
            line_rect.topleft = ((largura - line_rect.width) / 2 + x, (altura - line_rect.height) / 2 + y + i * line_rect.height)
        else:
            line_rect.topleft = (x, y + i * line_rect.height)

        superficie.blit(text_obj, line_rect)


def wrap_text(text, font, max_width):
    words = text.split(' ')
    new_words = []
    current_line = ''

    for word in words:
        if font.size(current_line + ' ' + word)[0] <= max_width:
            current_line += ' '
            current_line += word
        else:
            new_words.append(current_line.strip())
            current_line = word

    if current_line:
        new_words.append(current_line.strip())

    return new_words


#desenha um botao, havendo a possibilidade de por uma borda arredondada, os dois ultimos parametros só devem ser informados caso o texto do botao deva ficar centralizado
def desenharBotao(retangulo, cor, texto, fonte, corTexto, superficie, borderRadius=10, larguraTexto  = 0, alturaTexto = 0):
    pygame.draw.rect(superficie, cor, retangulo, border_radius=borderRadius)
    desenharTexto(texto, fonte, corTexto, superficie, retangulo.x, retangulo.y, larguraTexto, alturaTexto)