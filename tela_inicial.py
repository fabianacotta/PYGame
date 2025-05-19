
import pygame 
import sys 

def desenha_texto (texto, fonte, cor, superficie, x, y): 
    texto_obj = fonte.render (texto, True, cor)
    texto_rect = texto_obj.get_rect() 
    texto_rect.center = (x, y)
    superficie.blit (texto_obj, texto_rect)

    