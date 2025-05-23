
import pygame
import random

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

    tela_de_fundo = pygame.image.load ('images/Inicio.jpg')
    tela_de_fundo = pygame.transform.scale (tela_de_fundo, (1000, 600))

    tela.fill (BRANCO)
    tela.blit (tela_de_fundo, (0,0))

    mouse_x = pygame.mouse.get_pos()
    mouse_y = pygame.mouse.get_pos()

    botao_de_start = pygame.Rect(comprimento//2 - 100, 300, 200, 50)
    botao_dos_creditos = pygame.Rect (comprimento//2 - 100, 400, 200, 50)
    botao_de_sair = pygame.Rect (comprimento//2 - 100, 500, 200, 50)
    game = True
    while game:
        print (game)
        for evento in pygame.event.get(): 
            if evento.type == pygame.QUIT: 
                pygame.quit ()
                sys.exit ()
            elif evento.type == pygame.MOUSEBUTTONDOWN: 
                status.click.play ()
                if botao_de_start.collidepoint(mouse_x, mouse_y): 
                    return 'tela_do_botao_de_start'
                if botao_dos_creditos.collidepoint (mouse_x, mouse_y): 
                    return 'tela_de_creditos'
                if botao_de_sair.collidepoint(mouse_x, mouse_y): 
                    pygame.quit ()
                    sys.exit()

        desenha_texto("Jogo do Insper", fonte_titulo, PRETO, tela, comprimento//2, altura // 4)

        # if botao_de_start.collidepoint (mouse_x, mouse_y): 
        #     botao_de_start = pygame.Rect (comprimento//2 - 105, 295, 210, 60)
        # if botao_dos_creditos.collidepoint(mouse_x, mouse_y): 
        #     botao_dos_creditos = pygame.Rect (comprimento//2 - 105, 495, 210, 60)
        # if botao_de_sair.collidepoint(mouse_x, mouse_y): 
        #     botao_de_sair = pygame.Rect (comprimento//2 - 105, 495, 210, 60)

        # raio_da_borda_dos_botoes = 5
        pygame.draw.rect (tela, AZUL, botao_de_start, raio_da_borda = 5)
        desenha_texto("Start", fonte_texto, BRANCO, tela, botao_de_start.centerx, botao_de_start.centery)
        pygame.draw.rect (tela, AMARELO, botao_dos_creditos, raio_da_borda = 5)
        desenha_texto("Créditos", fonte_texto, BRANCO, tela, botao_dos_creditos.centerx, botao_dos_creditos.centery)
        pygame.draw.rect (tela, VERMELHO, botao_de_sair, raio_da_borda = 5)
        desenha_texto("Sair", fonte_texto, BRANCO, tela, botao_de_sair.centerx, botao_de_sair.centery)

        pygame.display.flip()

    # return 'tela_inicial'

def desenha_texto (texto, fonte, cor, superficie, x, y): 
    texto_obj = fonte.render (texto, True, cor)
    texto_rect = texto_obj.get_rect ()
    texto_rect.center = (x, y)
    superficie.blit (texto_obj, texto_rect)

def tela_de_creditos (tela, status): 
    BRANCO = (255, 255, 255)
    PRETO = (0, 0, 0)

    fonte_titulo = pygame.font.Font ("fontes/fonte1.ttf", 100)
    fonte_texto = pygame.font.Font ("fontes/fonte3.ttf", 26)

    tela.fill (88, 110, 124)
    mouse_x = pygame.mouse.get_pos()
    mouse_y = pygame.mouse.get_pos()

    for evento in pygame.event.get(): 
        if evento.type == pygame.QUIT: 
            pygame.quit ()
            sys.exit()
        elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1: 
            status.click.play ()

    desenha_texto("Creditos", fonte_texto, PRETO, tela, 500, 150)
    desenha_texto("Jogo desenvolvido por:", fonte_texto, BRANCO, tela, 500, 250)
    desenha_texto("-"*80, fonte_texto, BRANCO, tela, 500, 300)
    desenha_texto("Julia Fleury", fonte_texto, BRANCO, tela, 500, 350)
    desenha_texto("Fabiana Cotta", fonte_texto, BRANCO, tela, 500, 400)
    desenha_texto("Beatriz Guida", fonte_texto, BRANCO, tela, 500, 450)
    desenha_texto("-"*80, fonte_texto, BRANCO, tela, 500, 500)
    desenha_texto("Boa sorte!!", fonte_texto, BRANCO, tela, 500, 550)

    botao_voltar = pygame.image.load ('images/botao_back.png')

    if mouse_x >= 50 and mouse_x <= 125 and mouse_y >= 50 and mouse_y <= 100: 
        botao_voltar = pygame.transform.scale (botao_voltar, (85, 60))
        tela.blit (botao_voltar, (50, 50))
    else: 
        botao_voltar = pygame.transform.scale (botao_voltar, (75, 50))
        tela.blit (botao_voltar, (50, 50))

    return "tela_de_creditos"

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
        for i in range(5):
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
        self.image = pygame.image.load('images/Insper.png').convert ()
        self.image = pygame.transform.scale(self.image, (125, 125)) 
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

