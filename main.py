import pygame
import sys


pygame.init()

screen = pygame.display.set_mode([1200, 1000])
pygame.display.set_caption("Tetrin -  Was den sonst ?")
clock = pygame.time.Clock()
fps = 60

#global ticker, ticker_sec

ticker = 0
ticker_sec = 0
dificulty = 0
dificulty_sec = 1 #Wann wir es schneller

sys_font15 = pygame.font.SysFont(None, 15)
sys_font30 = pygame.font.SysFont(None, 30)

def draw_text(text, sys_font15, color, screen, x, y):
    textobj = sys_font15.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    screen.blit(textobj, textrect)
def textObjekt(text, pixel_font15):
    textFlaeche = pixel_font15.render(text, True, (0, 0, 0))
    return textFlaeche, textFlaeche.get_rect()
def show_fps():
    fps_tick = str(int(clock.get_fps()))
    draw_text(str(fps_tick), sys_font30, "Red", screen, 0, 0)
def timer(ticker, dificulty_sec):
    global dificulty
    if ticker >= (60 * dificulty_sec):
        dificulty += 1
        return True

menu = False
gameloop = True

while menu:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runtime = False

while gameloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop = False
    screen.fill((0, 0, 0))

    if timer(ticker, dificulty_sec):
        print("Test Timer")


    if ticker >= (60 * dificulty_sec):
        ticker = 0
    show_fps()
    ticker += 1
    pygame.display.flip()
    clock.tick(fps)
