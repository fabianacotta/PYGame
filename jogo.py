import pygame
import random
from time import sleep

#Pygame setup
pygame.init()
WINDOW_WIDTH = 900
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption('Insper Escape Game')
clock = pygame.time.Clock()
running = True
next_level = 1
mudar_fase = 0
dt = 0

#### Tela de Inicio do jogo ########
width, height = 900, 600
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
inicio = pygame.image.load("images/inicio.jpg")
inicio = pygame.transform.scale(inicio, (900, 600))
# Limpar a tela
screen.fill((0, 0, 0))  # Preencher com preto
# Desenhar a imagem de game over
screen.blit(inicio, (width // 2 - inicio.get_width() // 2, height // 2 - inicio.get_height() // 2))
# Atualizar a tela
pygame.display.update()
sleep(2)
#####################################


#Definindo um game class
class Game():
    def __init__(self, insper_group, food_group):
        self.insper_group = insper_group
        self.food_group = food_group
        self.score = 0
        self.lives = 5

        self.small_font = pygame.font.SysFont('impact', 24)
        self.big_font = pygame.font.SysFont('impact', 60)

        #Aqui vamos definir o logo python e a chave
        blue_food = pygame.image.load('images/food.png')
        chave = pygame.image.load('images/chave.png')

        # Food group e chave
        self.food_group.add(Food(190,200, chave, 1))
        for i in range(2): # Define quantos aumenta cada fase
            self.food_group.add(Food(i*200,200, blue_food, 0))



    def update(self):
        self.check_collision()
        self.draw()


        keys = pygame.key.get_pressed()
        if keys[pygame.K_p]:
            self.pause_game()

    def draw(self):
        global next_level
        global mudar_fase
        pygame.draw.rect(screen, "#003660", (0, 100, WINDOW_WIDTH, WINDOW_HEIGHT-200), 4)

        title_text = self.big_font.render(f"Insper Escape - Nivel: {next_level}" , True, "#003660")
        title_rect = title_text.get_rect()
        title_rect.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
        title_rect.top = 5

        #win_text = self.big_font.render(f"Level {next_level}!!!", True, "red")
        #win_rect = win_text.get_rect()
        #win_rect.centerx = WINDOW_WIDTH / 2
        #win_rect.centery = WINDOW_HEIGHT / 2

        score_text = self.small_font.render("Pontos: " + str(int(self.score)), True, "red")
        score_rect = score_text.get_rect()
        score_rect.topleft = (5,5)

        lives_text = self.small_font.render("Vidas: " + str(int(self.lives)), True, "red")
        lives_rect = lives_text.get_rect()
        lives_rect.topright = (WINDOW_WIDTH - 5, 5)

        screen.blit(title_text, title_rect)
        screen.blit(score_text, score_rect)
        screen.blit(lives_text, lives_rect)

        if self.score == 1:
            #screen.blit(win_text, win_rect)
            next_level += 1
            self.score = 0
            print(next_level)

            our_game = Game(insper, food_group) #aqui roda novamente o jogo

    def pause_game(self):
        global running

        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        is_paused = False
                if event.type == pygame.QUIT:
                    is_paused = False
                    running = False


    def check_collision(self):
        pegar_chave = pygame.sprite.spritecollideany(self.insper_group, self.food_group)
        if pegar_chave:
            if pegar_chave.type == 0:
                if self.lives == 1:
                    width, height = 900, 600
                    #screen = pygame.display.set_mode((width, height))
                    self.lives = 5
                    self.score = 0

                    game_over = pygame.image.load("images/game_over.jpg")
                    game_over = pygame.transform.scale(game_over, (900, 600))
                    # Limpar a tela
                    #screen.fill((0, 0, 0))  # Preencher com preto
                    # Desenhar a imagem de game over
                    screen.blit(game_over, (width // 2 - game_over.get_width() // 2, height // 2 - game_over.get_height() // 2))
                    # Atualizar a tela
                    pygame.display.update()
                    sleep(3)

                self.lives -= 1
                self.insper_group.reset()

            else:
                pegar_chave.remove(self.food_group)
                self.score += 1



# Definindo a class

class Insper(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        #define a imagem
        self.image = pygame.image.load('images/insper.png')
        #Define Rect
        self.rect = self.image.get_rect()
        #define posicao
        self.rect.topleft = (x, y)
        #move a imagem
        self.velocity = 10 #velocidade da raposa insper
        #acrescentando o food group
        #self.food_group = food_group
    def update(self):
        self.move()
        #self.check_collision()

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.rect.x >= 10 or keys[pygame.K_LEFT] and self.rect.x >= 10:
            self.rect.x -= self.velocity
        if keys[pygame.K_d] and self.rect.x <= WINDOW_WIDTH - 95 or keys[pygame.K_RIGHT] and self.rect.x <= WINDOW_WIDTH - 95:
            self.rect.x += self.velocity
        if keys[pygame.K_w] and self.rect.y >= 110 or keys[pygame.K_UP] and self.rect.y >= 110:
            self.rect.y -= self.velocity
        if keys[pygame.K_s] and self.rect.y <= WINDOW_HEIGHT - 95 or keys[pygame.K_DOWN] and self.rect.y <= WINDOW_HEIGHT - 95:
            self.rect.y += self.velocity

    def reset(self):
        self.rect.topleft = (100, 510)



#    def check_collision(self):
#        if pygame.sprite.spritecollide(self, self.food_group, True):
#            print(len(food_group))




class Food(pygame.sprite.Sprite):
    def __init__(self, x, y, image, food_type):
        super().__init__()
        #define a imagem
        self.image = image
        #Define Rect
        self.rect = self.image.get_rect()
        #define posicao
        self.rect.topleft = (x, y)
        #move a imagem
        self.velocity = random.randint(1, 5)

        #aqui define comida ou a chave
        self.type = food_type


        #criando random motion
        self.dx = random.choice([-1, 1])
        self.dy = random.choice([-1, 1])

    def update(self):
        #self.rect.y += self.velocity
        self.rect.x += self.dx * self.velocity
        self.rect.y += self.dy * self.velocity
        #ficar no quadrado
        if self.rect.left <= 0 or self.rect.right >= WINDOW_WIDTH:
            self.dx = -1 * self.dx
        if self.rect.top <= 100 or self.rect.bottom >= 500:
            self.dy = -1 * self.dy

food_group = pygame.sprite.Group()


#Cria o Insper group
insper_group = pygame.sprite.Group()
#posiciona o insper na tela
insper = Insper(200,510)
#adiciona o Insper no grupo
insper_group.add(insper)

#carrega a imagem
#insper = pygame.image.load("images/insper.png")

#coloca a imagem na tela
#insper_rect = insper.get_rect()

#Posiciona na tela
#insper_rect.center = (60, WINDOW_HEIGHT/2)

#######criar o class game#######
our_game = Game(insper, food_group)

while running:
    #Aqui o jogo fecha quando clicar no X
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Escolher a cor da tela

    screen.fill("black")

    #screen.blit(insper, insper_rect)
    #coloca na tela e move
    food_group.update()
    food_group.draw(screen)
    insper_group.update()
    insper_group.draw(screen)

    #atualiza o jogo
    our_game.update()

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
