
import pygame
import random

#setup do Pygame 
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
        self.small_font = pygame.font.SysFont('impact', 24)
        self.big_font = pygame.font.SysFont('impact', 60)

        #Aqui vamos definir o logo python e a chave
        blue_food = pygame.image.load('images/food.png')
        chave = pygame.image.load('images/chave.png')

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

        win_text = self.big_font.render("Alarme desarmado", True, "red")
        win_rect = win_text.get_rect()
        win_rect.centerx = WINDOW_WIDTH / 2
        win_rect.centery = WINDOW_HEIGHT / 2

        score_text = self.small_font.render("Score: " + str(int(self.score)), True, "blue")
        score_rect = score_text.get_rect()
        score_rect.topleft = (5,5)

        lives_text = self.small_font.render("Lives: " + str(int(self.score)), True, "blue")
        lives_rect = lives_text.get_rect()
        lives_rect.topright = (WINDOW_WIDTH - 5, 5)

        screen.blit(title_text, title_rect)
        screen.blit(score_text, score_rect)
        screen.blit(lives_text, lives_rect)

        if self.score == 8:
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
        print(pegar_chave)
        