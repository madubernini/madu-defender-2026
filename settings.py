"""
Configurações e constantes do jogo - Defenda o Gol Copa 2026
"""

# ---------- Janela ----------
LARGURA = 768
ALTURA = 1024
FPS = 60
TITULO = "Madu Defender 2026 - Defenda o Gol"

# ---------- Cores ----------
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERDE_GRAMA = (34, 90, 40)
AMARELO = (255, 223, 0)
VERMELHO = (220, 40, 40)
VERDE_NEON = (0, 255, 100)
CINZA_CLARO = (220, 220, 220)
PRETO_TRANSP = (0, 0, 0, 160)

# ---------- Caminhos ----------
PASTA_IMAGENS = "images"
PASTA_SONS = "sounds"

# ---------- Gol (parte de baixo da tela) ----------
GOAL_ALTURA = 220  # altura da faixa do gol desenhado na parte inferior
GOAL_LARGURA = LARGURA
GOAL_Y = ALTURA - GOAL_ALTURA  # posição Y onde o gol começa (topo da faixa do gol)

# Faixa onde o GK se move (logo acima do gol, entre as bolas e o gol)
GK_LINHA_Y = GOAL_Y - 90  # posição vertical (centro) do goleiro
GK_LARGURA = 120
GK_ALTURA = 160
GK_VELOCIDADE = 9  # pixels por frame

# Limites de movimento do GK (margem das bordas)
GK_MARGEM = 20

# ---------- Bola ----------
BOLA_TAMANHO = 42  # bola desenhada como BOLA_TAMANHO x BOLA_TAMANHO
BOLA_VELOCIDADE_INICIAL = 12
BOLA_VELOCIDADE_MAX = 14.0
BOLA_INCREMENTO_VELOCIDADE = 0.05  # aumenta a cada bola defendida
BOLA_DESVIO_MAX = 6.2  # variação horizontal máxima por frame (curva/ângulo)
BOLA_SPAWN_Y = 40  # posição Y onde a bola nasce, no topo da tela

# Intervalo entre bolas (em ms) - vai diminuindo com o tempo/pontuação
SPAWN_INTERVALO_INICIAL = 1100
SPAWN_INTERVALO_MIN = 550
SPAWN_DECREMENTO = 25  # reduz o intervalo a cada bola defendida

# ---------- Vidas / Pontuação ----------
VIDAS_INICIAIS = 3
DEFESAS_PARA_VENCER = 15  # defenda essa quantidade de bolas, sem zerar as vidas, para vencer

# ---------- Fontes ----------
FONTE_NOME = None  # usa fonte padrão do pygame se None
TAMANHO_FONTE_GRANDE = 64
TAMANHO_FONTE_MEDIA = 36
TAMANHO_FONTE_PEQUENA = 24

# ---------- Estados do jogo ----------
ESTADO_MENU = "menu"
ESTADO_JOGANDO = "jogando"
ESTADO_GAMEOVER = "gameover"
ESTADO_VITORIA = "vitoria"
