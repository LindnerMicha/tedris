import pygame
import random
import sys


pygame.init()

screen = pygame.display.set_mode([1200, 1000])
pygame.display.set_caption("Tetrin -  Was den sonst ?")
clock = pygame.time.Clock()
fps = 60

#global ticker, ticker_sec

z_rotate = 0

option = ""

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

def spawn():
    for blocks in range(len(spielfeld)):
        if spielfeld[blocks][0] == 0:
            z_shape(z_rotate)
        elif spielfeld[blocks][0] == 1:
            pass

def button(but_txt, but_x, but_y, but_laenge, but_hoehe, but_color_0, but_color_1, but_font):
    global maus_aktiv
    global option
    global sites
    global scan_switch
    global login_but
    global login_kennung
    global runtime_login
    global runtime
    global text
    global input_box
    global dig_an
    global pw_gen

    if maus_pos[0] > but_x and maus_pos[0] < but_x + but_laenge and maus_pos[1] > but_y and maus_pos[1] < but_y+but_hoehe:
        pygame.draw.rect(screen, but_color_1, (but_x, but_y, but_laenge, but_hoehe))
        if maus_klick[0] == 1 and maus_aktiv == False:
            maus_aktiv = True
            #option = but_txt

            if but_txt == "Gen Block":
                option = "Gen Block"

        if maus_klick[0] == 0:
            maus_aktiv = False
            option = ""
    else:
        pygame.draw.rect(screen, but_color_0, (but_x, but_y, but_laenge, but_hoehe))
    textGrund, textkasten = textObjekt(but_txt, but_font)
    textkasten.center = ((but_x+(but_laenge/2)),(but_y+(but_hoehe/2)))
    screen.blit(textGrund, textkasten)
def main_menu():
    screen.fill((0, 0, 0))
def z_shape(z_rotate):
    if z_rotate == 0:
        pygame.draw.rect(screen, (100,100,100), [spielfeld[-1][1], spielfeld[-1][2], 50, 50])
        pygame.draw.rect(screen, (100,100,100), [spielfeld[-1][1]+50, spielfeld[-1][2], 50, 50])
        pygame.draw.rect(screen, (100,100,100), [spielfeld[-1][1]+50, spielfeld[-1][2]+50, 50, 50])
        pygame.draw.rect(screen, (100,100,100), [spielfeld[-1][1]+100, spielfeld[-1][2]+50, 50, 50])
    elif z_rotate == 1:
        pygame.draw.rect(screen, (100,100,100), [spielfeld[-1][1]+50, spielfeld[-1][2], 50, 50])
        pygame.draw.rect(screen, (100,100,100), [spielfeld[-1][1]+50, spielfeld[-1][2]+50, 50, 50])
        pygame.draw.rect(screen, (100,100,100), [spielfeld[-1][1], spielfeld[-1][2]+50, 50, 50])
        pygame.draw.rect(screen, (100,100,100), [spielfeld[-1][1], spielfeld[-1][2]+100, 50, 50])


menu = False
gameloop = True
runtime = False

block_preload = random.randint(0, 5)
block_draw = random.randint(0, 5)
spielfeld = []
spielfeld_x = []
spielfeld_y = []

spawn_x = 400
spawn_y = 50

#while runtime:
while menu:
    maus_pos = pygame.mouse.get_pos()
    maus_klick = pygame.mouse.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runtime = False

while gameloop:
    maus_pos = pygame.mouse.get_pos()
    maus_klick = pygame.mouse.get_pressed()
    pressed = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop = False

    screen.fill((0, 0, 0))

    button("Gen Block", 1000, 50, 150, 35, (100,100,200), (100,100,100), sys_font30)


    if timer(ticker, dificulty_sec):
        for place in range(len(spielfeld)):
            spielfeld[place] = (spielfeld[place][0], spielfeld[place][1] , spielfeld[place][2] + 50)



    if option == "Gen Block" and gen_aktiv == False:
        #spawn_x = 400
        #spawn_y = 50

        gen_aktiv = True
        #block preload ziehen
        block_draw = block_preload
        #neuen block preload setzen
        block_preload = random.randint(0, 5)
        #neuen Block Spawnen
        spielfeld_x.append(spawn_x)
        spielfeld_y.append(spawn_y)
        spielfeld.append((block_draw, spawn_x, spawn_y))


    if not option == "Gen Block":
        gen_aktiv = False


#Movement
#region
    if pressed[pygame.K_r] and rotate_aktiv == False:
        rotate_aktiv = True
        if z_rotate == 1:
            z_rotate = 0
        elif z_rotate == 0:
            z_rotate = 1
    if not pressed[pygame.K_r]:
        rotate_aktiv = False
    for move_spielfeld in range(len(spielfeld)):
        if pressed[pygame.K_d] and z_move_aktiv_pls == False:
            z_move_aktiv_pls = True
            spawn_x += 50
        if not pressed[pygame.K_d]:
            z_move_aktiv_pls = False

        if pressed[pygame.K_a] and z_move_aktiv_min == False:
            z_move_aktiv_min = True
            spawn_x -= 50
        if not pressed[pygame.K_a]:
            z_move_aktiv_min = False

        if pressed[pygame.K_s]:
            spawn_y += 5
#endregion

    if ticker >= (60 * dificulty_sec):
        ticker = 0


    print(spielfeld)
    show_fps()

    spawn()

    ticker += 1
    pygame.display.flip()
    clock.tick(fps)
