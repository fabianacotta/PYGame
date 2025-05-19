# import pygame 
# import sys
# from tela_inicial import tela_inicial
# from tela_creditos import tela_de_creditos

import pygame
import sys
from tela_inicial import tela_inicial
from tela_creditos import tela_de_creditos
import jogo4  # importa para usar os recursos mas o loop principal está aqui

pygame.init()
comprimento = 1000
altura = 600
tela = pygame.display.set_mode((comprimento, altura))
pygame.display.set_caption("Jogo do Insper")

# Carregar sons ou status, se necessário
class Status:
    def __init__(self):
        self.click = pygame.mixer.Sound("sons/click.ogg")

status = Status()

# Variável de controle de estado
estado = 'tela_inicial'

# Variáveis do jogo
food_group = pygame.sprite.Group()
aspen_group = pygame.sprite.Group()
aspen = jogo4.Aspen(200, 510)
aspen_group.add(aspen)
jogo = jogo4.Game(aspen_group, food_group)

clock = pygame.time.Clock()
rodando = True

while rodando:
    if estado == 'tela_inicial':
        estado = tela_inicial(comprimento, altura, tela, status)

    elif estado == 'tela_de_creditos':
        estado = tela_de_creditos(tela, status)

    elif estado == 'tela_do_botao_de_start':
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

        tela.fill("black")
        food_group.update()
        food_group.draw(tela)
        aspen_group.update()
        aspen_group.draw(tela)
        jogo.update()
        if jogo.score >= 1 or jogo.lives <= 0:
            estado = 'game_over'

    elif estado == 'game_over':
        tela.fill((0, 0, 0))
        fonte = pygame.font.SysFont('impact', 60)
        texto = fonte.render("GAME OVER", True, (255, 0, 0))
        texto_rect = texto.get_rect(center=(comprimento // 2, altura // 2))
        tela.blit(texto, texto_rect)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_RETURN:
                estado = 'tela_inicial'
                food_group.empty()
                aspen_group.empty()
                aspen = jogo4.Aspen(200, 510)
                aspen_group.add(aspen)
                jogo = jogo4.Game(aspen_group, food_group)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
