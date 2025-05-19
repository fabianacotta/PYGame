import pygame
import random

# Definir algumas coisas do PyGame
pygame.init ()
COMP_TELA = 900
ALTURA_TELA = 600
tela = pygame.display.set_mode (COMP_TELA, ALTURA_TELA)
pygame.display.set_caption('Jogo de DesSoft')
relogio = pygame.time.Clock()
correr = True

dt = 0 
pos_jogador = pygame.Vector2(tela.get_width()/2, tela.get_height())

# Definindo uma classe do game
class Game(): 
    def __init__(self, grupo_aspen, grupo_comida): 
        self.grupo_aspen = grupo_aspen
        self.grupo_comida = grupo_comida
        self.pontos = 0
        self.vidas = 3

        # Definir a fonte
        self.fonte_pequena = pygame.font.Sysfont ("imapct", 24)
        self.fonte_grande = pygame.font.Sysfont ("imapct", 60)

        # Definir as imagens das "comidas"
        python_azul = pygame.image.load ("images/food.png")
        python_vermelho = pygame.image.load ("images/chave.png")

        # Adicionar as "comidas" pro grupo de comidas
        # Sendo o python_azul = 0 e o python_vermelho = 1
        self.grupo_comida.add (Food(190, 200, python_vermelho, 1))
        for i in range (7): 
            self.food_group.add (Food(200, 200, python_azul, 0))
            
