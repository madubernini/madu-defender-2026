"""
Bola - nasce no topo da tela (abaixo do gol) e cai com leve curva/ângulo.
"""

import random
import pygame

from settings import (
    LARGURA,
    ALTURA,
    BOLA_SPAWN_Y,
    BOLA_TAMANHO,
    BOLA_DESVIO_MAX,
)
from assets import carregar_imagem


class Bola(pygame.sprite.Sprite):
    def __init__(self, velocidade_queda):
        super().__init__()
        self.image_original = carregar_imagem(
            "ball.png", tamanho=(BOLA_TAMANHO, BOLA_TAMANHO)
        )
        self.image = self.image_original
        self.rect = self.image.get_rect()

        # Nasce em uma posição X aleatória, perto do topo da tela
        margem_x = BOLA_TAMANHO
        self.rect.centerx = random.randint(margem_x, LARGURA - margem_x)
        self.rect.centery = BOLA_SPAWN_Y

        # Velocidade vertical (constante por bola, definida pela dificuldade atual)
        self.vel_y = velocidade_queda

        # Velocidade horizontal: começa com um pequeno valor aleatório,
        # simulando o "ângulo" do chute. Pode ser positivo ou negativo.
        self.vel_x = random.uniform(-BOLA_DESVIO_MAX, BOLA_DESVIO_MAX)

        # Posição em float para movimento mais suave (rect só aceita int)
        self.pos_x = float(self.rect.centerx)
        self.pos_y = float(self.rect.centery)

        # Ângulo de rotação visual (efeito de bola girando)
        self.angulo = 0
        self.vel_rotacao = self.vel_x * 12  # gira mais rápido quanto mais "de canto" for

        # Estado: usado para tratar a animação de "defendida" (quica e sai)
        self.defendida = False

    def atualizar(self):
        if not self.defendida:
            self.pos_y += self.vel_y
            self.pos_x += self.vel_x

            # Rebate nas bordas laterais da tela (efeito de curva sem sair pela lateral)
            if self.pos_x <= BOLA_TAMANHO / 2:
                self.pos_x = BOLA_TAMANHO / 2
                self.vel_x *= -1
            elif self.pos_x >= LARGURA - BOLA_TAMANHO / 2:
                self.pos_x = LARGURA - BOLA_TAMANHO / 2
                self.vel_x *= -1
        else:
            # Após ser defendida: sobe rápido e sai da tela por cima
            self.pos_y -= 18
            self.pos_x += self.vel_x * 0.5

        self.rect.centerx = int(self.pos_x)
        self.rect.centery = int(self.pos_y)

        # Rotação visual simples
        self.angulo = (self.angulo + self.vel_rotacao) % 360
        self.image = pygame.transform.rotate(self.image_original, self.angulo)
        # Recentraliza o rect depois de rotacionar (rotate muda o tamanho da superfície)
        centro_atual = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = centro_atual

    def marcar_como_defendida(self):
        self.defendida = True

    def saiu_da_tela_por_cima(self):
        return self.rect.bottom < 0

    def saiu_da_tela_por_baixo(self):
        return self.rect.top > ALTURA

    def desenhar(self, tela):
        tela.blit(self.image, self.rect)