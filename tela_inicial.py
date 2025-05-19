
import pygame 
import sys 

def desenha_texto (texto, fonte, cor, superficie, x, y): 
    texto_obj = fonte.render (texto, True, cor)
    texto_rect = texto_obj.get_rect() 
    texto_rect.center = (x, y)
    superficie.blit (texto_obj, texto_rect)

def tela_inicial (comprimento, altura, tela, status): 
    BRANCO = (255, 255, 255)
    PRETO = (0, 0, 0)
    AZUL = (4, 124, 252)
    AMARELO = (249, 194, 60)
    VERMELHO = (237, 53, 91)

    fonte_titulo = pygame.font.Font ("fontes/fonte1.ttf", 130)
    fonte_texto = pygame.font.Font ("fontes/fonte3.ttf", 26)

    tela_de_fundo = pygame.image.load ('images/Insper.png')
    tela_de_fundo = pygame.transform.scale (tela_de_fundo, (1000, 600))

    tela.fill (BRANCO)
    tela.blit (tela_de_fundo, (0,0))

    mouse_x = pygame.mouse.get_pos()
    mouse_y = pygame.mouse.get_pos()

    botao_de_start = pygame.Rect(comprimento//2 - 100, 300, 200, 50)
    botao_de_instrucoes = pygame.Rect (comprimento//2 - 100, 400, 200, 50)
    botao_de_sair = pygame.Rect (comprimento//2 - 100, 500, 200, 50)

    