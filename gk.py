"""
Goleira (GK) - controlada pelo jogador, move-se só no eixo X.
"""

import pygame

from settings import (
    LARGURA,
    GK_LINHA_Y,
    GK_LARGURA,
    GK_ALTURA,
    GK_VELOCIDADE,
    GK_MARGEM,
)
from assets import carregar_imagem


class GK(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = carregar_imagem("gk.png", tamanho=(GK_LARGURA, GK_ALTURA))
        self.rect = self.image.get_rect()
        self.rect.centerx = LARGURA // 2
        self.rect.centery = GK_LINHA_Y

        # Área de colisão um pouco menor que o sprite (fica mais justo/justo com a bola)
        self.hitbox = self.rect.inflate(-30, -50)

    def atualizar(self, teclas):
        dx = 0
        if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
            dx -= GK_VELOCIDADE
        if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
            dx += GK_VELOCIDADE

        self.rect.x += dx

        # Limita o GK dentro da tela (com margem)
        if self.rect.left < GK_MARGEM:
            self.rect.left = GK_MARGEM
        if self.rect.right > LARGURA - GK_MARGEM:
            self.rect.right = LARGURA - GK_MARGEM

        # Atualiza hitbox junto com o rect
        self.hitbox.center = self.rect.center

    def desenhar(self, tela):
        tela.blit(self.image, self.rect)