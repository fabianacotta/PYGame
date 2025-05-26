
import pygame
import random
from time import sleep

# Pygame setup
pygame.init()
LARGURA_TELA = 900
ALTURA_TELA = 600
TELA = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption('Fuja do Python!')
relogio = pygame.time.Clock()

# --- VARIÁVEIS DO JOGO ---

jogo_rodando = True
# Controla se estamos no menu ou no jogo principal
no_menu = True
# Controla se a tela de créditos deve ser mostrada
mostrar_creditos = False

dt = 0
proximo_nivel = 1

# --- CORES ---
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
CINZA_CLARO = (200, 200, 200)
CINZA_ESCURO = (100, 100, 100)
LARANJA = (207, 132, 79)
AZUL = (130, 209, 224)
AMARELO = (240, 213, 130)
AMARELO_ALARANJADO = (219, 150, 67)
VINHO_ALARANJADO = (144, 54, 32)


# --- CARREGANDO IMAGENS E FONTE ---
inicio_img = pygame.image.load("images/inicio_2.jpg").convert()
inicio_img = pygame.transform.scale(inicio_img, (LARGURA_TELA, ALTURA_TELA))

creditos_img = pygame.image.load("images/tela_creditos.jpg").convert()
creditos_img = pygame.transform.scale(creditos_img, (LARGURA_TELA, ALTURA_TELA))

fonte = pygame.font.Font("fontes/fonte1.ttf", 36)

#Definindo som
som_pegar_moeda = pygame.mixer.Sound("sounds/som_pegar_moeda.mp3")


# --- FUNÇÕES ---

def desenhar_botao(superficie, cor_fundo, cor_texto, texto, x, y, largura, altura, acao = None):
    mouse_pos = pygame.mouse.get_pos()
    clique = pygame.mouse.get_pressed()
    botao_rect = pygame.Rect(x, y, largura, altura)

    if botao_rect.collidepoint(mouse_pos):
        pygame.draw.rect(superficie, CINZA_ESCURO, botao_rect)
        if clique[0] == 1 and acao is not None:
            pygame.time.delay(200)
            acao()
    else:
        pygame.draw.rect(superficie, cor_fundo, botao_rect)

    texto_surf = fonte.render(texto, True, cor_texto)
    texto_rect = texto_surf.get_rect(center=botao_rect.center)
    superficie.blit(texto_surf, texto_rect)

# --- FUNÇÕES DE AÇÃO DOS BOTÕES  ---

def acao_iniciar_jogo():
    global no_menu
    print("Botão 'Iniciar' clicado!")
    no_menu = False # Sinaliza para sair do loop do menu e começar o jogo

def acao_mostrar_creditos():
    global mostrar_creditos
    print("Botão 'Creditos' clicado!")
    mostrar_creditos = True # Sinaliza que a tela de créditos deve ser mostrada

def acao_voltar_menu():
    global mostrar_creditos
    print("Botão 'Voltar' clicado!")
    mostrar_creditos = False # Sinaliza para voltar à tela principal do menu

def acao_sair_jogo():
    global jogo_rodando
    print("Botão 'Sair' clicado!")
    jogo_rodando = False # Termina o loop principal da aplicação

# =================================================================
# LOOP DO MENU PRINCIPAL
# =================================================================

while no_menu and jogo_rodando:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            no_menu = False
            jogo_rodando = False

    #
    # A cada quadro, decidimos o que desenhar com base no estado de 'mostrar_creditos'
    if mostrar_creditos:
        # Desenha a tela de créditos
        TELA.blit(creditos_img, (0, 0))
        desenhar_botao(TELA, AMARELO, PRETO, "Voltar", 10, 10, 130, 50, acao_voltar_menu)
    else:
        # Desenha a tela de menu principal
        TELA.blit(inicio_img, (0, 0))
        desenhar_botao(TELA, AZUL, PRETO, "Iniciar", 350, 240, 200, 50, acao_iniciar_jogo)
        desenhar_botao(TELA, AMARELO, PRETO, "Creditos", 350, 340, 200, 50, acao_mostrar_creditos)
        desenhar_botao(TELA, LARANJA, PRETO, "Sair", 350, 440, 200, 50, acao_sair_jogo)

    # --- ATUALIZAÇÃO DA TELA ---
    pygame.display.flip()
    relogio.tick(60)

# =================================================================
# Inicio do jogo
# =================================================================

#Definindo um game class
class Game():
    # ... (o resto da sua classe Game continua aqui, sem alterações)
    def __init__(self, insper_raposa, python_comidas):
        self.insper_raposa = insper_raposa
        self.python_comidas = python_comidas
        self.pontuacao = 0
        self.vidas = 5

        self.fonte_pequena = pygame.font.SysFont('impact', 30)
        self.fonte_media = pygame.font.SysFont('impact', 40)
        self.fonte_grande = pygame.font.SysFont('impact', 60)

        #Aqui vamos definir o logo python e a chave
        pythons = pygame.image.load('images/food.png')
        chave = pygame.image.load('images/chave.png')

        # Food group e chave
        self.python_comidas.add(Food(190,200, chave, 1))
        for i in range(2): # Define quantos aumenta cada fase
            self.python_comidas.add(Food(i*200,200, pythons, 0))


    def update(self):
        self.check_collision()
        self.draw()


        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_p]:
            self.pausar_jogo()

    def draw(self):
        global proximo_nivel

        pygame.draw.rect(TELA, "#003660", (0, 100, LARGURA_TELA, ALTURA_TELA-200), 4)

        titulo = self.fonte_grande.render(f"Insper Escape - Nivel: {proximo_nivel}" , True, "#003660")
        titulo_rect = titulo.get_rect()
        titulo_rect.center = (LARGURA_TELA / 2, ALTURA_TELA / 2)
        titulo_rect.top = 5


        #win_text = self.fonte_grande.render(f"Level {proximo_nivel}!!!", True, "red")
        #win_rect = win_text.get_rect()
        #win_rect.centerx = LARGURA_TELA / 2
        #win_rect.centery = ALTURA_TELA / 2

        #pontuacao = self.fonte_pequena.render("Pontos: " + str(int(self.pontuacao)), True, "red")
        #pontuacao = pontuacao.get_rect()
        #pontuacao.topleft = (5,5)

        vidas_text = self.fonte_pequena.render("Vidas: " + str(int(self.vidas)), True, "red")
        vidas_rect = vidas_text.get_rect()
        vidas_rect.topright = (LARGURA_TELA - 5, 5)

        TELA.blit(titulo, titulo_rect)
        #TELA.blit(pontuacao_text, pontuacao)  #desabilitei o pontuacao
        TELA.blit(vidas_text, vidas_rect)

        if self.pontuacao == 1:
            #TELA.blit(win_text, win_rect)
            proximo_nivel += 1
            self.pontuacao = 0
            som_pegar_moeda.play()
            nosso_jogo = Game(insper, python_comidas) #aqui roda novamente o jogo


    def pausar_jogo (self):
        global jogo_rodando

        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        is_paused = False
                if event.type == pygame.QUIT:
                    is_paused = False
                    jogo_rodando = False


    def check_collision(self):
        global proximo_nivel

        restart_game_text = self.fonte_pequena.render('Pressione "ENTER" para reiniciar', True, VINHO_ALARANJADO, AMARELO_ALARANJADO)
        restart_game_text_rect = restart_game_text.get_rect()
        restart_game_text_rect.center = (LARGURA_TELA / 2, ALTURA_TELA / 2 + 140)

        restart_pontuacao_text = self.fonte_media.render(f"Você fez {proximo_nivel-1} pontos!", True, AMARELO_ALARANJADO, VINHO_ALARANJADO)
        restart_pontuacao_text_rect = restart_pontuacao_text.get_rect()
        restart_pontuacao_text_rect.center = (LARGURA_TELA / 2, ALTURA_TELA / 2 + 10)





        pegar_chave = pygame.sprite.spritecollideany(self.insper_raposa, self.python_comidas)
        if pegar_chave:
            if pegar_chave.type == 0:
                if self.vidas == 1:
                    ########### Aqui mostra a tela de Game Over e reinicia o joga apos apertar "Enter" #####
                    width, height = 900, 600
                    #TELA = pygame.display.set_mode((width, height))
                    self.vidas = 5
                    self.pontuacao = 0
                    proximo_nivel = 1
                    game_over = pygame.image.load("images/game_over.jpg")
                    game_over = pygame.transform.scale(game_over, (1100, 600))
                    # Desenhar a imagem de game over
                    TELA.blit(game_over, (width // 2 - game_over.get_width() // 2, height // 2 - game_over.get_height() // 2))
                    # Atualizar a tela
                    pygame.display.update()

                    ##### Aqui coloco a mensagem de Enter para reiniciar #######
                    TELA.blit(restart_game_text, restart_game_text_rect)
                    pygame.display.update()

                    ##### Aqui coloco a mensagem de pontuacao #######
                    TELA.blit(restart_pontuacao_text, restart_pontuacao_text_rect)
                    pygame.display.update()

                    teclas = pygame.key.get_pressed()
                    self.pausar_jogo()       #Aqui para o jogo e espera o Enter para reiniciar
                    python_comidas.remove(python_comidas) # Aqui apaga os sprites para reiniciar o jogo
                    #print(python_comidas)
                    nosso_jogo = Game(insper, python_comidas)
                else:
                    self.vidas -= 1
                self.insper_raposa.reset()

            else:
                pegar_chave.remove(self.python_comidas)
                self.pontuacao += 1

# Definindo a class
class Insper(pygame.sprite.Sprite):
    # ... (o resto da sua classe Insper continua aqui, sem alterações)
    def __init__(self, x, y):
        super().__init__()
        #define a imagem
        self.image = pygame.image.load('images/insper.png')
        #Define Rect
        self.rect = self.image.get_rect()
        #define posicao
        self.rect.topleft = (x, y)
        #move a imagem
        self.velocity = 10 # velocidade da raposa insper
        #acrescentando o python_comidas
        #self.python_comidas = python_comidas
    def update(self):
        self.move()
        #self.check_collision()

    def move(self):
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_a] and self.rect.x >= 10 or teclas[pygame.K_LEFT] and self.rect.x >= 10:
            self.rect.x -= self.velocity
        if teclas[pygame.K_d] and self.rect.x <= LARGURA_TELA - 95 or teclas[pygame.K_RIGHT] and self.rect.x <= LARGURA_TELA - 95:
            self.rect.x += self.velocity
        if teclas[pygame.K_w] and self.rect.y >= 110 or teclas[pygame.K_UP] and self.rect.y >= 110:
            self.rect.y -= self.velocity
        if teclas[pygame.K_s] and self.rect.y <= ALTURA_TELA - 95 or teclas[pygame.K_DOWN] and self.rect.y <= ALTURA_TELA - 95:
            self.rect.y += self.velocity

    def reset(self):
        self.rect.topleft = (100, 510)

class Food(pygame.sprite.Sprite):
    # ... (o resto da sua classe Food continua aqui, sem alterações)
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
        if self.rect.left <= 0 or self.rect.right >= LARGURA_TELA:
            self.dx = -1 * self.dx
        if self.rect.top <= 100 or self.rect.bottom >= 500:
            self.dy = -1 * self.dy


python_comidas = pygame.sprite.Group()
insper_raposa = pygame.sprite.Group()
insper = Insper(200, 510)
insper_raposa.add(insper)

nosso_jogo = Game(insper, python_comidas)

# =================================================================
# LOOP DO JOGO PRINCIPAL
# =================================================================

while jogo_rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogo_rodando = False

    TELA.fill("black")

    python_comidas.update()
    python_comidas.draw(TELA)
    insper_raposa.update()
    insper_raposa.draw(TELA)
    nosso_jogo.update()

    pygame.display.flip()
    dt = relogio.tick(60) / 1000

# --- FIM DO JOGO ---
pygame.quit()
