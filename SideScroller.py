import pygame
import time
import sys
pygame.init()

boy_size_x = int(100)
boy_size_y = int(100)
x = int(0)
y = int()
speed =  int(1)
boy_x = int()
boy_y =  int(100)
cacti = pygame.image.load('cactus1.png')
cacti = pygame.transform.scale(cacti, (int(cacti.get_width()/8), int(cacti.get_height()/8)))
obs_x = 200
obs_y = 100
obs = [cacti, obs_x, obs_y]
obs_list = [obs]
background = pygame.image.load('images/PurpledParralax.jpg')
screen = pygame.display.set_mode((800, background.get_height()))
screen.blit(background, (0, 0))
x2 = x+background.get_width()
run_frames = 8
boy_run = run_frames * [0]
for i in range(run_frames):
    boy_run[i] = pygame.image.load('pumkin_boy/Run ('+str(i+1)+').png')
    boy_run[i] = pygame.transform.scale(boy_run[i], (boy_size_x, boy_size_y))

def collide_rect(x1, y1, w1, h1, x2, y2, w2, h2):
#    if ((x2 > x1 and x2 - x1 < w1) or (x1 > x2 and x1 - x2 < w2)) and ((y2 > y1 and y2 - y1 < h1) or (y1 > y2 and y1 - y2 < h2)):
    if ((x2 >= x1 and x2 - x1 <= (w1+w2)/2) or (x1 > x2 and x1 - x2 < (w2+w1)/2)) and ((y2 >= y1 and y2 - y1 <= (h1+h2)/2) or (y1 > y2 and y1 - y2 < (h1+h2)/2)):
        return True
    else:
        return False

Running = True
while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
#            sys.exit
    x -= speed
    x2 -= speed
    if x < background.get_width():
        x = background.get_width()
    if x2 < background.get_width():
        x2 = background.get_width()
    screen.blit(background, (0, 0))
    screen.blit(background, (x2, 0))
    for obsi in obs_list:
        obsi[1] -= speed
        screen.blit(obsi[0], (obsi[1], obsi[2]))
        if collide_rect(obsi[1], obsi[2], obsi[0].get_width(), obsi[0].get_height(), boy_x, boy_y, boy_size_x, boy_size_y):
            speed = 0
    screen.blit(boy_run[int(i/4)%run_frames], (boy_x, boy_y))
    i += 1
    boy_x += 0
    pygame.display.update()
    time.sleep(0)
