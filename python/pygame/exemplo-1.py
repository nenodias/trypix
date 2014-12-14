import sys, pygame
from pygame.locals import *

# Constantes da Janela
RAIO_CIRCULO = 20
INCREMENTO = 5
BAIXO = 'baixo'
CIMA = 'cima'
ESQUERDA = 'esquerda'
DIREITA = 'direita'
LARGURA = 800
ALTURA = 600
TITULO = "Teste Círculo"

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)

# Taxa de atualização da tela
FPS = 15

pygame.init()

TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption(TITULO)

fpsClock = pygame.time.Clock()
pygame.key.set_repeat(1, 1)

global x, y, teclaPressionada
teclaPressionada = None
# Colocando as coordenadas iniciais no centro
x, y = int(LARGURA/2), int(ALTURA/2)

# Método onde os eventos são capturados
def eventos():
    global teclaPressionada
    for event in pygame.event.get():
        # Testando se o evento para sair foi chamado ou evento é de uma tecla pressionada e essa tecla é o ESC
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
        # Testando se uma tecla foi pressionada
        elif event.type == KEYDOWN:
            tecla = pygame.key.get_pressed()
            if tecla[K_RIGHT]:
                teclaPressionada = DIREITA
            if tecla[K_LEFT]:
                teclaPressionada = ESQUERDA
            if tecla[K_UP]:
                teclaPressionada = CIMA
            if tecla[K_DOWN]:
                teclaPressionada = BAIXO

def logica():
    global x,y
    if teclaPressionada == DIREITA:
        x += INCREMENTO
    if teclaPressionada == ESQUERDA:
        x -= INCREMENTO
    if teclaPressionada == CIMA:
        y -= INCREMENTO
    if teclaPressionada == BAIXO:
        y += INCREMENTO

    if x >= LARGURA + RAIO_CIRCULO:
        x = 0
    elif x <= 0 - RAIO_CIRCULO:
        x = LARGURA
    if y >= ALTURA + RAIO_CIRCULO:
        y = 0
    elif y <= 0 - RAIO_CIRCULO:
        y = ALTURA

def desenha():
    pygame.draw.circle(TELA, PRETO, (x, y), RAIO_CIRCULO)

while True:
    TELA.fill(BRANCO)
    eventos()
    logica()
    desenha()

    pygame.display.update()
    fpsClock.tick(FPS)