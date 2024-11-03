import json
import random

from Movimento import Movimento


class Aprendizado:
    def __init__(self, alpha=0.1, gamma=0.9, epsilon=0.2, nome='Bot', estilo=None):
        self.tabela_q = dict()
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.nome = nome
        self.estilo = estilo

    def set_nome(self, nome):
        self.nome = nome

    def set_estilo(self, estilo):
        self.estilo = estilo

    def get_valor_q(self, estado, acao):
        return self.tabela_q.get((estado, acao), 0.0)

    def acao(self, estado, acoes):
        if len(acoes) == 0:
            return None
        if random.uniform(0, 1) < self.epsilon:
            return random.choice(acoes)
        else:
            melhores_acoes = self.melhores_jogadas(acoes, estado)
            return random.choice(melhores_acoes)

    def melhores_jogadas(self, acoes, estado):
        valores_q = []
        for acao in acoes:
            valores_q.append(self.get_valor_q(estado, acao.to_string()))
        maior_q = max(valores_q)
        melhores_acoes = []
        for i in range(len(acoes)):
            if valores_q[i] == maior_q:
                melhores_acoes.append(acoes[i])
        return melhores_acoes

    def atualizar_valor_q(self, estado, acao, recompensa, proximo_estado, proximas_acoes):
        valor_antigo = self.get_valor_q(estado, acao.to_string())
        recompensas_futuras = []
        if len(proximas_acoes) == 0:
            return
        if proximas_acoes:
            for a in proximas_acoes:
                recompensas_futuras.append(self.get_valor_q(proximo_estado, a.to_string()))
        melhor_futuro = max(recompensas_futuras)
        novo_valor = (1 - self.alpha) * valor_antigo + self.alpha * (recompensa + self.gamma * melhor_futuro)
        self.tabela_q[(estado, acao.to_string())] = novo_valor
        self.salvar_aprendizado(self.nome + '_data.txt')

    def salvar_aprendizado(self, arq='qlearning_data.txt'):
        with open(arq, 'w') as f:
            for key, value in self.tabela_q.items():
                estado, acao = key
                f.write(f'{estado}|{acao}|{value}\n')

    def carregar_aprendizado(self, arq='qlearning_data.txt'):
        try:
            with open(arq, 'r') as f:
                for line in f:
                    estado, acao, valor = line.split('|')
                    self.tabela_q[(estado, acao)] = float(valor)
        except FileNotFoundError:
            pass


