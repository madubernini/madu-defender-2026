"""
Madu Defender 2026 - Defenda o Gol
Jogo top-down simples feito com Pygame: controle a goleira e defenda
as bolas que caem do topo da tela antes que entrem no gol.

Como jogar:
- Setas (ou A/D) para mover a goleira para os lados.
- ENTER para começar / jogar de novo.
- ESC ou fechar a janela para sair.
"""

import sys
import random
import pygame

from settings import (
    LARGURA,
    ALTURA,
    FPS,
    TITULO,
    VIDAS_INICIAIS,
    DEFESAS_PARA_VENCER,
    BOLA_VELOCIDADE_INICIAL,
    BOLA_VELOCIDADE_MAX,
    BOLA_INCREMENTO_VELOCIDADE,
    SPAWN_INTERVALO_INICIAL,
    SPAWN_INTERVALO_MIN,
    SPAWN_DECREMENTO,
    ESTADO_MENU,
    ESTADO_JOGANDO,
    ESTADO_GAMEOVER,
    ESTADO_VITORIA,
)
from assets import carregar_som, tocar_musica_fundo
from cenario import Cenario
from gk import GK
from bola import Bola
from ui import UI


class Jogo:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        self.tela = pygame.display.set_mode((LARGURA, ALTURA))
        pygame.display.set_caption(TITULO)
        self.relogio = pygame.time.Clock()

        self.cenario = Cenario()
        self.ui = UI()

        # Sons
        self.som_apito_inicio_fim = carregar_som("apito_inicio_fim.mp3", volume=0.1)
        self.som_apito_jogada = carregar_som("apito.mp3", volume=0.5)
        self.som_defesa = carregar_som("gk_defende_ball.mp3", volume=1)
        self.som_gol = carregar_som("sound_goal.mp3", volume=1)
        self.nome_musica_torcida = "crowd_stadium.mp3"

        self.estado = ESTADO_MENU
        self._musica_tocando = False

        self.reiniciar_jogo()

    def reiniciar_jogo(self):
        self.gk = GK()
        self.bolas = pygame.sprite.Group()

        self.pontos = 0
        self.vidas = VIDAS_INICIAIS

        self.velocidade_bola_atual = BOLA_VELOCIDADE_INICIAL
        self.spawn_intervalo_atual = SPAWN_INTERVALO_INICIAL

        # Temporizador de criação de bolas (pygame custom event)
        self.EVENTO_SPAWN_BOLA = pygame.USEREVENT + 1
        pygame.time.set_timer(self.EVENTO_SPAWN_BOLA, self.spawn_intervalo_atual)

    def iniciar_partida(self):
        self.reiniciar_jogo()
        self.estado = ESTADO_JOGANDO
        self.som_apito_inicio_fim.play()
        tocar_musica_fundo(self.nome_musica_torcida, volume=0.35, loop=True)

    def finalizar_partida(self):
        self.estado = ESTADO_GAMEOVER
        pygame.mixer.music.stop()
        self.som_apito_inicio_fim.play()
        # Para de gerar bolas novas
        pygame.time.set_timer(self.EVENTO_SPAWN_BOLA, 0)

    def finalizar_vitoria(self):
        self.estado = ESTADO_VITORIA
        pygame.mixer.music.stop()
        self.som_apito_inicio_fim.play()
        # Para de gerar bolas novas
        pygame.time.set_timer(self.EVENTO_SPAWN_BOLA, 0)

    def criar_nova_bola(self):
        nova = Bola(self.velocidade_bola_atual)
        self.bolas.add(nova)

    def aumentar_dificuldade(self):
        """Chamado a cada defesa: deixa o jogo um pouco mais difícil."""
        self.velocidade_bola_atual = min(
            BOLA_VELOCIDADE_MAX,
            self.velocidade_bola_atual + BOLA_INCREMENTO_VELOCIDADE,
        )
        self.spawn_intervalo_atual = max(
            SPAWN_INTERVALO_MIN,
            self.spawn_intervalo_atual - SPAWN_DECREMENTO,
        )
        pygame.time.set_timer(self.EVENTO_SPAWN_BOLA, self.spawn_intervalo_atual)

    def processar_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.sair()

            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    self.sair()

                if evento.key == pygame.K_RETURN:
                    if self.estado == ESTADO_MENU:
                        self.iniciar_partida()
                    elif self.estado in (ESTADO_GAMEOVER, ESTADO_VITORIA):
                        self.estado = ESTADO_MENU

            elif evento.type == self.EVENTO_SPAWN_BOLA:
                if self.estado == ESTADO_JOGANDO:
                    self.criar_nova_bola()

    def atualizar(self):
        if self.estado != ESTADO_JOGANDO:
            return

        teclas = pygame.key.get_pressed()
        self.gk.atualizar(teclas)

        for bola in list(self.bolas):
            bola.atualizar()

            if not bola.defendida:
                # Verifica colisão com a goleira (usa hitbox mais justa)
                if self.gk.hitbox.colliderect(bola.rect):
                    bola.marcar_como_defendida()
                    self.pontos += 1
                    self.som_defesa.play()
                    if self.pontos >= DEFESAS_PARA_VENCER:
                        self.finalizar_vitoria()
                    else:
                        self.aumentar_dificuldade()

                # Bola passou da goleira e saiu por baixo da tela = gol sofrido
                elif bola.saiu_da_tela_por_baixo():
                    self.bolas.remove(bola)
                    self.vidas -= 1
                    self.som_gol.play()
                    if self.vidas <= 0:
                        self.finalizar_partida()
            else:
                # Bola já defendida, saiu por cima = remove da lista
                if bola.saiu_da_tela_por_cima():
                    self.bolas.remove(bola)

    def desenhar(self):
        self.cenario.desenhar(self.tela)

        if self.estado in (ESTADO_JOGANDO, ESTADO_GAMEOVER, ESTADO_VITORIA):
            self.gk.desenhar(self.tela)
            for bola in self.bolas:
                bola.desenhar(self.tela)
            self.ui.desenhar_hud(self.tela, self.pontos, self.vidas)

        if self.estado == ESTADO_MENU:
            self.ui.desenhar_menu(self.tela)

        if self.estado == ESTADO_GAMEOVER:
            self.ui.desenhar_game_over(self.tela, self.pontos)

        if self.estado == ESTADO_VITORIA:
            self.ui.desenhar_vitoria(self.tela, self.pontos)

        pygame.display.flip()

    def sair(self):
        pygame.quit()
        sys.exit()

    def executar(self):
        while True:
            self.processar_eventos()
            self.atualizar()
            self.desenhar()
            self.relogio.tick(FPS)


if __name__ == "__main__":
    jogo = Jogo()
    jogo.executar()
