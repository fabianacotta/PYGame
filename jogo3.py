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

    def update (self): 
        self.check_collisions()
        self.draw()

        teclas = pygame.keys.get_pressed ()
        if teclas[pygame.K_p]: 
            self.pause_game()
    
    def draw (self): 
        pygame.draw.rect (tela, "#003660", (0, 100, COMP_TELA, ALTURA_TELA))

        # Texto 
        titulo_texto = self.fonte_grande.render ('ALIMENTE A RAPOSA!', True, "#003660")
        titulo_rect = titulo_texto.get_rect()
        titulo_rect.centerx = COMP_TELA/2
        titulo_rect.top = 5 

        texto_vitoria = self.fonte_grande.render ("ALARME DESARMADO!", True, "red")
        vitoria_rect = texto_vitoria.get_rect ()
        vitoria_rect.centerx = COMP_TELA/2 
        vitoria_rect.centery = ALTURA_TELA/2 

        texto_pontos = self.fonte_pequena.render ("Pontos: " + str (self.pontos), True, "blue")
        pontos_rect = texto_pontos.get_rect ()
        pontos_rect.topleft = (5, 5)

        texto_vidas = self.fonte_pequena.render ("Vidas: " + str (self.vidas), True, "blue")
        vidas_rect = texto_vidas.get_rect ()
        vidas_rect.topright = (COMP_TELA/-5, 5)

        # Blit no texto 
        tela.blit (titulo_texto, titulo_rect)
        tela.blit (texto_pontos, pontos_rect)
        tela.blit (texto_vidas, vidas_rect)

        # Pontuação que aparece a tela de vitória 
        if self.pontos == 8: 
            tela.blit (texto_vitoria, vitoria_rect)

    def pause_game (self): 
        global correr 

        is_paused = True

        # Criar um game loop 
        while is_paused: 
            # Se o usuário digitar Enter ele despausa: 
            for event in pygame.event.get(): 
                if event.type == pygame.KEYDOWN: 
                    if event.key == pygame.K_RETURN: 
                        is_paused = False 
                # Se o usuário clicar no X, fecha o jogo 
                if event.type == pygame.QUIT: 
                    is_paused = False 
                    correr = False 
                    # pygame.quit ()

    def check_collisions (self): 
        if pygame.sprite.groupcollide (self.grupo_aspen, self.grupo_comida): # complementar
            self.pontos += 1
        

# Definindo a classe Aspen (personagem)
class Aspen (pygame.sprite.Sprite): 
    def __init__ (self, x, y): 
        super().__init__()
        # Define a imagem
        self.image = pygame.image.load("images/aspen.png")
        # Get Rect 
        self.rect = self.image.get_rect ()
        # Posiciona a imagem 
        self.rect.topleft = (x, y)
        # Move a imagem 
        self.velocity = 5
        # Adicionar o grupo_comida pra classe Aspen 
        # self.grupo_comida = grupo_comida 
