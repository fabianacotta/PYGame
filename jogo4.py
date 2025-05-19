
import pygame
import random

#Pygame setup
pygame.init()
WINDOW_WIDTH = 900
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption('Teste3')
clock = pygame.time.Clock()
running = True

dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

#Definindo um game class
class Game():
    def __init__(self, aspen_group, food_group):
        self.aspen_group = aspen_group
        self.food_group = food_group
        self.score = 0
        self.lives = 3

        self.small_font = pygame.font.SysFont('impact', 24)
        self.big_font = pygame.font.SysFont('impact', 60)

        #Aqui vamos definir o logo python e a chave
        blue_food = pygame.image.load('images/food.png').convert()
        blue_food = pygame.transform.scale(blue_food, (100, 120)) 
        chave = pygame.image.load('images/chave.png').convert()
        chave = pygame.transform.scale(chave, (50, 50)) 


        # Food group e chave
        self.food_group.add(Food(190,200, chave, 1))
        for i in range(7):
            self.food_group.add(Food(i*200,200, blue_food, 0))


    def update(self):
        self.check_collision()
        self.draw()


        keys = pygame.key.get_pressed()
        if keys[pygame.K_p]:
            self.pause_game()

    def draw(self):
        pygame.draw.rect(screen, "#003660", (0, 100, WINDOW_WIDTH, WINDOW_HEIGHT-200), 4)

        title_text = self.big_font.render("Insper Escape" , True, "#003660")
        title_rect = title_text.get_rect()
        title_rect.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
        title_rect.top = 5

        win_text = self.big_font.render("Voce venceu!!!", True, "red")
        win_rect = win_text.get_rect()
        win_rect.centerx = WINDOW_WIDTH / 2
        win_rect.centery = WINDOW_HEIGHT / 2

        score_text = self.small_font.render("Score: " + str(int(self.score)), True, "blue")
        score_rect = score_text.get_rect()
        score_rect.topleft = (5,5)

        lives_text = self.small_font.render("Lives: " + str(int(self.lives)), True, "blue")
        lives_rect = lives_text.get_rect()
        lives_rect.topright = (WINDOW_WIDTH - 5, 5)

        screen.blit(title_text, title_rect)
        screen.blit(score_text, score_rect)
        screen.blit(lives_text, lives_rect)

        if self.score == 1:
            screen.blit(win_text, win_rect)

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
        pegar_chave = pygame.sprite.spritecollideany(self.aspen_group, self.food_group)
        if pegar_chave:
            if pegar_chave.type == 0:
                self.lives -= 1
                self.aspen_group.reset()

            else:
                pegar_chave.remove(self.food_group)
                self.score += 1

# Definindo a class

class Aspen(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        #define a imagem
        self.image = pygame.image.load('images/aspen.png')
        #Define Rect
        self.rect = self.image.get_rect()
        #define posicao
        self.rect.topleft = (x, y)
        #move a imagem
        self.velocity = 5
        #acrescentando o food group
        #self.food_group = food_group
    def update(self):
        self.move()
        #self.check_collision()

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.rect.x >= 10:
            self.rect.x -= self.velocity
        if keys[pygame.K_d] and self.rect.x <= WINDOW_WIDTH - 95:
            self.rect.x += self.velocity
        if keys[pygame.K_w] and self.rect.y >= 110:
            self.rect.y -= self.velocity
        if keys[pygame.K_s] and self.rect.y <= WINDOW_HEIGHT - 95:
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

#Cria 8 foods
#for i in range(8):
#    food = Food(i*100, 200)
#    food_group.add(food)

#Cria o Aspen group
aspen_group = pygame.sprite.Group()
#posiciona o aspen na tela
aspen = Aspen(200,510)
#adiciona o Aspen no grupo
aspen_group.add(aspen)

#carrega a imagem
#aspen = pygame.image.load("images/aspen.png")

#coloca a imagem na tela
#aspen_rect = aspen.get_rect()

#Posiciona na tela
#aspen_rect.center = (60, WINDOW_HEIGHT/2)

#######criar o class game#######
our_game = Game(aspen, food_group)

while running:
    #Aqui o jogo fecha quando clicar no X
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Escolher a cor da tela

    screen.fill("black")

    #screen.blit(aspen, aspen_rect)
    #coloca na tela e move
    food_group.update()
    food_group.draw(screen)
    aspen_group.update()
    aspen_group.draw(screen)

    #atualiza o jogo
    our_game.update()

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()

