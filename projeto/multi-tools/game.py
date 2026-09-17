import pygame
import random
import math


# ============================================================
# INICIALIZAÇÃO
# ============================================================

pygame.init()


# ============================================================
# CONFIGURAÇÕES
# ============================================================

LARGURA = 600
ALTURA = 800
FPS = 60

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("🚀 Space Wars")


clock = pygame.time.Clock()


# ============================================================
# CORES
# ============================================================

PRETO = (5, 5, 20)
BRANCO = (255, 255, 255)

AZUL = (0, 200, 255)
AZUL_CLARO = (100, 240, 255)

VERDE = (0, 255, 140)

VERMELHO = (255, 60, 80)
ROXO = (180, 80, 255)

AMARELO = (255, 220, 80)


# ============================================================
# FONTES
# ============================================================

fonte = pygame.font.SysFont("arial", 26, bold=True)
fonte_pequena = pygame.font.SysFont("arial", 18)
fonte_game_over = pygame.font.SysFont("arial", 55, bold=True)


# ============================================================
# ESTRELAS
# ============================================================

estrelas = []

for _ in range(100):

    estrela = {
        "x": random.randint(0, LARGURA),
        "y": random.randint(0, ALTURA),
        "velocidade": random.uniform(1, 3),
        "tamanho": random.randint(1, 3)
    }

    estrelas.append(estrela)


def desenhar_estrelas():
    """Desenha e movimenta as estrelas do espaço."""

    for estrela in estrelas:

        estrela["y"] += estrela["velocidade"]

        if estrela["y"] > ALTURA:
            estrela["y"] = 0
            estrela["x"] = random.randint(0, LARGURA)

        pygame.draw.circle(
            tela,
            BRANCO,
            (int(estrela["x"]), int(estrela["y"])),
            estrela["tamanho"]
        )


# ============================================================
# EXPLOSÕES
# ============================================================

explosoes = []


def criar_explosao(x, y):
    """Cria uma pequena explosão."""

    explosoes.append({
        "x": x,
        "y": y,
        "raio": 5,
        "tempo": 20
    })


def desenhar_explosoes():

    for explosao in explosoes[:]:

        pygame.draw.circle(
            tela,
            AMARELO,
            (
                int(explosao["x"]),
                int(explosao["y"])
            ),
            explosao["raio"],
            2
        )

        explosao["raio"] += 3
        explosao["tempo"] -= 1

        if explosao["tempo"] <= 0:
            explosoes.remove(explosao)


# ============================================================
# CLASSE DO JOGADOR
# ============================================================

class Jogador(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()

        self.image = pygame.Surface(
            (50, 40),
            pygame.SRCALPHA
        )

        # Corpo da nave
        pygame.draw.polygon(
            self.image,
            AZUL,
            [
                (25, 0),
                (5, 35),
                (25, 28),
                (45, 35)
            ]
        )

        # Cockpit
        pygame.draw.circle(
            self.image,
            AZUL_CLARO,
            (25, 15),
            7
        )

        # Asas
        pygame.draw.line(
            self.image,
            BRANCO,
            (8, 30),
            (42, 30),
            2
        )

        self.rect = self.image.get_rect()

        self.rect.centerx = LARGURA // 2
        self.rect.bottom = ALTURA - 30

        self.velocidade = 7

        self.vidas = 3

    def update(self):

        teclas = pygame.key.get_pressed()

        if teclas[pygame.K_LEFT]:
            self.rect.x -= self.velocidade

        if teclas[pygame.K_RIGHT]:
            self.rect.x += self.velocidade

        # Impede a nave de sair da tela

        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.right > LARGURA:
            self.rect.right = LARGURA

    def atirar(self):

        laser = Laser(
            self.rect.centerx,
            self.rect.top
        )

        todos_sprites.add(laser)
        lasers.add(laser)


# ============================================================
# CLASSE DO INIMIGO
# ============================================================

class Inimigo(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()

        self.image = pygame.Surface(
            (40, 35),
            pygame.SRCALPHA
        )

        # Corpo do inimigo

        pygame.draw.polygon(
            self.image,
            VERMELHO,
            [
                (20, 0),
                (40, 20),
                (30, 32),
                (10, 32),
                (0, 20)
            ]
        )

        # Olhos

        pygame.draw.circle(
            self.image,
            BRANCO,
            (13, 18),
            4
        )

        pygame.draw.circle(
            self.image,
            BRANCO,
            (27, 18),
            4
        )

        pygame.draw.circle(
            self.image,
            PRETO,
            (13, 18),
            2
        )

        pygame.draw.circle(
            self.image,
            PRETO,
            (27, 18),
            2
        )

        self.rect = self.image.get_rect()

        self.rect.x = random.randint(
            0,
            LARGURA - self.rect.width
        )

        self.rect.y = random.randint(
            -150,
            -40
        )

        self.velocidade_y = random.randint(2, 5)

    def update(self):

        self.rect.y += self.velocidade_y

        # Se sair da tela, volta para cima

        if self.rect.top > ALTURA:

            self.rect.x = random.randint(
                0,
                LARGURA - self.rect.width
            )

            self.rect.y = random.randint(
                -150,
                -40
            )

            self.velocidade_y = random.randint(2, 5)


# ============================================================
# CLASSE DO LASER
# ============================================================

class Laser(pygame.sprite.Sprite):

    def __init__(self, x, y):

        super().__init__()

        self.image = pygame.Surface(
            (6, 20),
            pygame.SRCALPHA
        )

        # Laser principal

        pygame.draw.rect(
            self.image,
            VERDE,
            (1, 0, 4, 20)
        )

        # Brilho

        pygame.draw.rect(
            self.image,
            BRANCO,
            (2, 0, 2, 20)
        )

        self.rect = self.image.get_rect()

        self.rect.centerx = x
        self.rect.bottom = y

        self.velocidade = -12

    def update(self):

        self.rect.y += self.velocidade

        if self.rect.bottom < 0:
            self.kill()


# ============================================================
# GRUPOS DE SPRITES
# ============================================================

todos_sprites = pygame.sprite.Group()
inimigos = pygame.sprite.Group()
lasers = pygame.sprite.Group()


# ============================================================
# JOGADOR
# ============================================================

jogador = Jogador()

todos_sprites.add(jogador)


# ============================================================
# CRIAÇÃO DOS INIMIGOS
# ============================================================

for _ in range(8):

    inimigo = Inimigo()

    todos_sprites.add(inimigo)
    inimigos.add(inimigo)


# ============================================================
# VARIÁVEIS DO JOGO
# ============================================================

pontuacao = 0

rodando = True
game_over = False


# ============================================================
# LOOP PRINCIPAL
# ============================================================

while rodando:

    clock.tick(FPS)


    # ========================================================
    # EVENTOS
    # ========================================================

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            rodando = False

        if evento.type == pygame.KEYDOWN:

            if evento.key == pygame.K_SPACE and not game_over:

                jogador.atirar()

            if evento.key == pygame.K_r and game_over:

                # Reinicia o jogo

                pontuacao = 0

                jogador.vidas = 3

                jogador.rect.centerx = LARGURA // 2

                jogador.rect.bottom = ALTURA - 30

                inimigos.empty()
                lasers.empty()

                for _ in range(8):

                    inimigo = Inimigo()

                    todos_sprites.add(inimigo)
                    inimigos.add(inimigo)

                game_over = False


    # ========================================================
    # ATUALIZAÇÃO
    # ========================================================

    if not game_over:

        todos_sprites.update()


        # ====================================================
        # COLISÃO LASER x INIMIGO
        # ====================================================

        colisoes = pygame.sprite.groupcollide(
            inimigos,
            lasers,
            True,
            True
        )


        for inimigo in colisoes:

            pontuacao += 100

            criar_explosao(
                inimigo.rect.centerx,
                inimigo.rect.centery
            )

            # Cria outro inimigo

            novo_inimigo = Inimigo()

            todos_sprites.add(novo_inimigo)
            inimigos.add(novo_inimigo)


        # ====================================================
        # COLISÃO INIMIGO x JOGADOR
        # ====================================================

        hit = pygame.sprite.spritecollide(
            jogador,
            inimigos,
            True
        )


        if hit:

            jogador.vidas -= 1

            if jogador.vidas <= 0:

                game_over = True


    # ========================================================
    # DESENHO
    # ========================================================

    tela.fill(PRETO)

    # Fundo estrelado

    desenhar_estrelas()

    # Sprites

    todos_sprites.draw(tela)

    # Explosões

    desenhar_explosoes()


    # ========================================================
    # PLACAR
    # ========================================================

    texto_pontos = fonte.render(
        f"PONTOS: {pontuacao}",
        True,
        BRANCO
    )

    tela.blit(
        texto_pontos,
        (20, 20)
    )


    # ========================================================
    # VIDAS
    # ========================================================

    texto_vidas = fonte.render(
        f"VIDAS: {jogador.vidas}",
        True,
        VERMELHO
    )

    tela.blit(
        texto_vidas,
        (430, 20)
    )


    # ========================================================
    # INSTRUÇÕES
    # ========================================================

    if not game_over:

        instrucoes = fonte_pequena.render(
            "← → Mover     ESPAÇO Atirar",
            True,
            AZUL_CLARO
        )

        tela.blit(
            instrucoes,
            (LARGURA // 2 - instrucoes.get_width() // 2, ALTURA - 25)
        )


    # ========================================================
    # GAME OVER
    # ========================================================

    if game_over:

        # Fundo escuro transparente

        overlay = pygame.Surface(
            (LARGURA, ALTURA),
            pygame.SRCALPHA
        )

        overlay.fill((0, 0, 0, 180))

        tela.blit(overlay, (0, 0))


        texto_game_over = fonte_game_over.render(
            "GAME OVER",
            True,
            VERMELHO
        )

        tela.blit(
            texto_game_over,
            (
                LARGURA // 2 - texto_game_over.get_width() // 2,
                280
            )
        )


        texto_final = fonte.render(
            f"Pontuação: {pontuacao}",
            True,
            BRANCO
        )

        tela.blit(
            texto_final,
            (
                LARGURA // 2 - texto_final.get_width() // 2,
                370
            )
        )


        texto_restart = fonte_pequena.render(
            "Pressione R para jogar novamente",
            True,
            AZUL_CLARO
        )

        tela.blit(
            texto_restart,
            (
                LARGURA // 2 - texto_restart.get_width() // 2,
                430
            )
        )


    # ========================================================
    # ATUALIZA A TELA
    # ========================================================

    pygame.display.flip()


# ============================================================
# FINALIZAÇÃO
# ============================================================

pygame.quit()
