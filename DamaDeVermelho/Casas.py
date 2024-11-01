CASA_VAZIA = 0
PECA_BRANCA = 1
PECA_PRETA = 2
PECA_BRANCA_SELECIONADA = 3
PECA_PRETA_SELECIONADA = 4
PECA_BRANCA_DAMA = 5
PECA_PRETA_DAMA = 6
PECA_BRANCA_DAMA_SELECIONADA = 7
PECA_PRETA_DAMA_SELECIONADA = 8
CASA_MOVIMENTO = 9
MOVIMENTO_NORMAL = 1
MOVIMENTO_COMER = 2


def eh_branca(peca):
    return peca == PECA_BRANCA or peca == PECA_BRANCA_SELECIONADA or peca == PECA_BRANCA_DAMA or peca == PECA_BRANCA_DAMA_SELECIONADA


def eh_preta(peca):
    return peca == PECA_PRETA or peca == PECA_PRETA_SELECIONADA or peca == PECA_PRETA_DAMA or peca == PECA_PRETA_DAMA_SELECIONADA


def color(peca):
    if eh_branca(peca):
        return PECA_BRANCA
    elif eh_preta(peca):
        return PECA_PRETA
    else:
        return CASA_VAZIA
