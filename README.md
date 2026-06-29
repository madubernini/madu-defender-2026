# ⚽ Madu Defender 2026

Jogo 2D de arcade feito em **Python + Pygame**, inspirado na Copa do Mundo de 2026.

Você controla a goleira **Madu** e precisa defender o gol contra uma sequência de bolas que caem do topo da tela. Defenda **15 bolas** para vencer — mas cuidado, você só tem **3 vidas**!

![Tela de menu](https://github.com/madubernini/madu-defender-2026/blob/main/scheenshots/menu.png)
![Jogo em andamento](screenshots/gameplay.png)
![Tela de vitória](screenshots/vitoria.png)

---

## 🎮 Sobre o jogo

| | |
|---|---|
| **Gênero** | Arcade / Defesa (top-down) |
| **Objetivo** | Defender 15 bolas sem perder todas as vidas |
| **Vidas** | 3 — cada bola que entra no gol custa 1 vida |
| **Dificuldade** | Progressiva — a cada defesa, as bolas ficam mais rápidas e frequentes |

A goleira fica numa faixa fixa, logo acima do gol, e se move apenas para os lados. As bolas nascem no topo da tela e caem em direção ao gol com uma leve curva, exigindo reflexo para se posicionar a tempo.

---

## 🕹️ Controles

| Tecla | Ação |
|---|---|
| `←` / `A` | Mover a goleira para a esquerda |
| `→` / `D` | Mover a goleira para a direita |
| `Enter` | Iniciar partida / Jogar novamente |
| `Esc` | Sair do jogo |

---

## 🖥️ Como jogar (Windows — executável)

1. Baixe o arquivo `.zip` da [última release](../../releases).
2. Extraia o conteúdo em qualquer pasta.
3. Garanta que o `.exe` está na mesma pasta que as subpastas `images/` e `sounds/`.
4. Dê duplo clique em `MaduDefender2026.exe`.

> O jogo não precisa de instalação nem de Python instalado para rodar nessa forma.

---

## 🐍 Como rodar via código-fonte (Python)

Pré-requisito: [Python 3.10+](https://www.python.org/downloads/) instalado.

```bash
# 1. Clone o repositório
git clone https://github.com/madubernini/madu-defender-2026.git
cd madu-defender-2026

# 2. Instale as dependências
pip install pygame

# 3. Rode o jogo
python main.py
```

---

## 📁 Estrutura do projeto

```
madu-defender-2026/
├── main.py              # Loop principal e lógica geral do jogo
├── settings.py          # Constantes (tamanhos, velocidades, cores, regras)
├── assets.py            # Carregamento seguro de imagens e sons
├── cenario.py           # Desenha o campo de fundo e o gol
├── gk.py                # Classe da goleira controlável
├── bola.py              # Classe da bola que cai
├── ui.py                # HUD, tela de menu, vitória e game over
├── images/
│   ├── background.png
│   ├── ball.png
│   ├── gk.png
│   ├── goal.png
│   └── menu_background.png
└── sounds/
    ├── apito_inicio_fim.mp3
    ├── apito.mp3
    ├── crowd_stadium.mp3
    ├── gk_defende_ball.mp3
    └── sound_goal.mp3
```

---

## ⚙️ Ajustando o jogo

A maior parte do balanceamento está centralizada em `settings.py`:

| Constante | O que controla |
|---|---|
| `VIDAS_INICIAIS` | Quantidade de vidas no começo |
| `DEFESAS_PARA_VENCER` | Quantas defesas são necessárias para vencer |
| `BOLA_VELOCIDADE_INICIAL` / `BOLA_VELOCIDADE_MAX` | Velocidade de queda das bolas |
| `BOLA_DESVIO_MAX` | Intensidade da curva/ângulo da bola |
| `SPAWN_INTERVALO_INICIAL` / `SPAWN_INTERVALO_MIN` | Frequência com que as bolas aparecem |
| `GK_VELOCIDADE` | Velocidade de movimento da goleira |

---

## 🛠️ Tecnologias

- [Python](https://www.python.org/)
- [Pygame](https://www.pygame.org/)

---

## 📄 Licença

Projeto acadêmico, desenvolvido como atividade prática da disciplina de Linguagem de Programação Aplicada.
