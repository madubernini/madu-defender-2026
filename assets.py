"""
Carregamento seguro de imagens e sons.
Se um arquivo não existir, o jogo não trava: usa um substituto
(placeholder colorido para imagem, ou "som mudo" para áudio).
"""

import os
import pygame

from settings import PASTA_IMAGENS, PASTA_SONS


def caminho_imagem(nome_arquivo):
    return os.path.join(PASTA_IMAGENS, nome_arquivo)


def caminho_som(nome_arquivo):
    return os.path.join(PASTA_SONS, nome_arquivo)


def carregar_imagem(nome_arquivo, tamanho=None, manter_proporcao_largura=None):
    """
    Carrega uma imagem com transparência (convert_alpha).
    Se não existir, devolve uma superfície magenta de aviso (fácil de notar).

    tamanho: tupla (largura, altura) para redimensionar exatamente.
    manter_proporcao_largura: se definido, redimensiona mantendo proporção
        com base na largura desejada (ignora 'tamanho' se ambos forem dados).
    """
    caminho = caminho_imagem(nome_arquivo)
    try:
        imagem = pygame.image.load(caminho).convert_alpha()
    except (pygame.error, FileNotFoundError):
        print(f"[AVISO] Imagem não encontrada: {caminho} -> usando placeholder.")
        largura = tamanho[0] if tamanho else 100
        altura = tamanho[1] if tamanho else 100
        imagem = pygame.Surface((largura, altura), pygame.SRCALPHA)
        imagem.fill((255, 0, 255, 180))
        pygame.draw.rect(imagem, (0, 0, 0), imagem.get_rect(), 3)
        return imagem

    if manter_proporcao_largura:
        razao = imagem.get_height() / imagem.get_width()
        nova_largura = manter_proporcao_largura
        nova_altura = int(nova_largura * razao)
        imagem = pygame.transform.smoothscale(imagem, (nova_largura, nova_altura))
    elif tamanho:
        imagem = pygame.transform.smoothscale(imagem, tamanho)

    return imagem


class SomMudo:
    """Substituto para quando um som não existe - tem os mesmos métodos, mas não faz nada."""
    def play(self, *args, **kwargs):
        pass

    def stop(self, *args, **kwargs):
        pass

    def set_volume(self, *args, **kwargs):
        pass


def carregar_som(nome_arquivo, volume=1.0):
    """Carrega um efeito sonoro (pygame.mixer.Sound). Se não existir, devolve SomMudo."""
    caminho = caminho_som(nome_arquivo)
    try:
        som = pygame.mixer.Sound(caminho)
        som.set_volume(volume)
        return som
    except (pygame.error, FileNotFoundError):
        print(f"[AVISO] Som não encontrado: {caminho} -> seguindo sem esse som.")
        return SomMudo()


def tocar_musica_fundo(nome_arquivo, volume=0.5, loop=True):
    """Toca uma música/ambiente em loop usando pygame.mixer.music. Não trava se faltar arquivo."""
    caminho = caminho_som(nome_arquivo)
    try:
        pygame.mixer.music.load(caminho)
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play(-1 if loop else 0)
    except (pygame.error, FileNotFoundError):
        print(f"[AVISO] Música não encontrada: {caminho} -> seguindo sem música de fundo.")