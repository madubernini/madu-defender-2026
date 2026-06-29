"""
Cenário - desenha o fundo (campo de grama) e o gol na parte inferior da tela.
"""

import pygame

from settings import LARGURA, ALTURA, GOAL_ALTURA, GOAL_Y
from assets import carregar_imagem


class Cenario:
    def __init__(self):
        # Background: textura de grama, esticada suavemente para cobrir a tela toda
        # (evita linhas de corte visíveis que apareceriam ao repetir/tile a imagem)
        bg_original = carregar_imagem("background.png")
        self.fundo = pygame.transform.smoothscale(bg_original, (LARGURA, ALTURA))

        # Gol: desenhado na parte de baixo da tela, ocupando a largura da tela.
        self.goal = carregar_imagem("goal.png", tamanho=(LARGURA, GOAL_ALTURA))

    def desenhar(self, tela):
        tela.blit(self.fundo, (0, 0))
        tela.blit(self.goal, (0, GOAL_Y))