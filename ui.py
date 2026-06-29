"""
Interface do usuário: HUD (placar/vidas), tela de menu inicial e tela de game over.
"""

import pygame

from settings import (
    LARGURA,
    ALTURA,
    BRANCO,
    PRETO,
    AMARELO,
    VERMELHO,
    VERDE_NEON,
    DEFESAS_PARA_VENCER,
    TAMANHO_FONTE_GRANDE,
    TAMANHO_FONTE_MEDIA,
    TAMANHO_FONTE_PEQUENA,
)
from assets import carregar_imagem


class UI:
    def __init__(self):
        pygame.font.init()
        self.fonte_grande = pygame.font.SysFont("arial", TAMANHO_FONTE_GRANDE, bold=True)
        self.fonte_media = pygame.font.SysFont("arial", TAMANHO_FONTE_MEDIA, bold=True)
        self.fonte_pequena = pygame.font.SysFont("arial", TAMANHO_FONTE_PEQUENA)

        # Imagem de menu (instruções), centralizada e um pouco transparente
        self.menu_bg = carregar_imagem("menu_background.png", manter_proporcao_largura=560)
        self.menu_bg.set_alpha(235)
        self.menu_rect = self.menu_bg.get_rect(center=(LARGURA // 2, ALTURA // 2))

    # ---------- HUD durante o jogo ----------
    def desenhar_hud(self, tela, pontos, vidas):
        # Placar (canto superior esquerdo) - mostra progresso até a meta de vitória
        texto = f"Defesas: {pontos}/{DEFESAS_PARA_VENCER}"
        texto_pontos = self.fonte_media.render(texto, True, BRANCO)
        sombra_pontos = self.fonte_media.render(texto, True, PRETO)
        tela.blit(sombra_pontos, (22, 22))
        tela.blit(texto_pontos, (20, 20))

        # Vidas (canto superior direito, desenhadas como bolinhas/corações simples)
        raio = 14
        espaco = 36
        x_inicial = LARGURA - 20 - (raio * 2)
        for i in range(vidas):
            cx = x_inicial - i * espaco
            cy = 35
            pygame.draw.circle(tela, VERMELHO, (cx, cy), raio)
            pygame.draw.circle(tela, PRETO, (cx, cy), raio, 2)

    # ---------- Tela de Menu ----------
    def desenhar_menu(self, tela):
        # Overlay leve escurecendo o jogo atrás, para destacar o menu
        overlay = pygame.Surface((LARGURA, ALTURA), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 90))
        tela.blit(overlay, (0, 0))

        tela.blit(self.menu_bg, self.menu_rect)

    # ---------- Tela de Game Over ----------
    def desenhar_game_over(self, tela, pontos):
        overlay = pygame.Surface((LARGURA, ALTURA), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))
        tela.blit(overlay, (0, 0))

        titulo = self.fonte_grande.render("VOCÊ PERDEU!", True, VERMELHO)
        tela.blit(titulo, titulo.get_rect(center=(LARGURA // 2, ALTURA // 2 - 120)))

        placar = self.fonte_media.render(f"Defesas: {pontos}", True, AMARELO)
        tela.blit(placar, placar.get_rect(center=(LARGURA // 2, ALTURA // 2 - 30)))

        instrucao = self.fonte_media.render("Pressione ENTER", True, VERDE_NEON)
        tela.blit(instrucao, instrucao.get_rect(center=(LARGURA // 2, ALTURA // 2 + 60)))

        instrucao2 = self.fonte_pequena.render("para jogar novamente", True, BRANCO)
        tela.blit(instrucao2, instrucao2.get_rect(center=(LARGURA // 2, ALTURA // 2 + 100)))

    # ---------- Tela de Vitória ----------
    def desenhar_vitoria(self, tela, pontos):
        overlay = pygame.Surface((LARGURA, ALTURA), pygame.SRCALPHA)
        overlay.fill((0, 40, 0, 170))
        tela.blit(overlay, (0, 0))

        titulo = self.fonte_grande.render("VOCÊ VENCEU!", True, AMARELO)
        tela.blit(titulo, titulo.get_rect(center=(LARGURA // 2, ALTURA // 2 - 120)))

        placar = self.fonte_media.render(f"Defesas: {pontos}", True, VERDE_NEON)
        tela.blit(placar, placar.get_rect(center=(LARGURA // 2, ALTURA // 2 - 30)))

        instrucao = self.fonte_media.render("Pressione ENTER", True, VERDE_NEON)
        tela.blit(instrucao, instrucao.get_rect(center=(LARGURA // 2, ALTURA // 2 + 60)))

        instrucao2 = self.fonte_pequena.render("para jogar novamente", True, BRANCO)
        tela.blit(instrucao2, instrucao2.get_rect(center=(LARGURA // 2, ALTURA // 2 + 100)))
