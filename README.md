# Dama de Vermelho

Dama de vermelho é um jogo de damas feito em python com diversos bots pré treinados usando Q Learning.


# regras
* o jogo consiste em um tabureiro 8x8 com peças brancas e pretas, o objetivo é capturar todas as peças do adversário.
* as peças brancas começam o jogo, e as peças pretas sempre jogam depois.
* as peças podem se mover na diagonal, e capturar peças adversárias pulando sobre elas.
* apenas uma peça pode ser capturada por jogada.
* se uma peça chegar ao final do tabuleiro, ela se torna uma dama, e pode se mover na diagonal em qualquer direção.
* se uma peça puder capturar outra peça, ela é obrigada a fazê-lo.
* o jogo termina quando um dos jogadores não tem mais peças, ou não pode mais se mover.

# bots
* os bots são treinados usando Q Learning, e são capazes de jogar o jogo de forma eficiente.
* os bots são recompensados de forma diferente para fornecer diversos estilos de jogo
* os pesos são armezanados em arquivos de forma com que o bot melhore cada vez e ja comece treinado.
