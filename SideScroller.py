import pygame
import sys
pygame.init()

boy_size_x = int(100)
boy_size_y = int(100)
x = int(0)
y = int()
speed =  int(5)
boy_x = int(100)
boy_y =  int(125)
cacti = pygame.image.load('cactus1.png')
cacti = pygame.transform.scale(cacti, (int(cacti.get_width()/16), int(cacti.get_height()/16)))
obs_x = 700
obs_y = 200
ii = int(1)
state = str("R")
obs = [cacti, obs_x, obs_y]
obs_list = [obs]
background = pygame.image.load('images/PurpledParralax.jpg')
background2 = pygame.image.load('images/PurpledParralax.jpg')
screen = pygame.display.set_mode((400, background.get_height()))
screen.blit(background, (x, 0))
x2 = x+background.get_width()
run_frames = 8
dead_frames = 10
jump_frames = 10
boy_run = run_frames * [0]
boy_dead = dead_frames * [0]
boy_jump = jump_frames * [0]
for i in range(run_frames):
    boy_run[i] = pygame.image.load('pumkin_boy/Run ('+str(i+1)+').png')
    boy_run[i] = pygame.transform.scale(boy_run[i], (int(boy_run[i].get_width()/7), int(boy_run[i].get_height()/7)))
for i in range(dead_frames):
    boy_dead[i] = pygame.image.load('pumkin_boy/Dead ('+str(i+1)+').png')
    boy_dead[i] = pygame.transform.scale(boy_dead[i], (int(boy_dead[i].get_width()/7), int(boy_dead[i].get_height()/7)))
for i in range(jump_frames):
    boy_jump[i] = pygame.image.load('pumkin_boy/Jump ('+str(i+1)+').png')
    boy_jump[i] = pygame.transform.scale(boy_jump[i], (int(boy_jump[i].get_width()/7), int(boy_jump[i].get_height()/7)))

jump_height = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]

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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_j:
                state = "J"
                ii = 1
                for z in range(49):
                    speed = 1
                    x -= speed
                    x2 -= speed
                    if x < -background.get_width():
                        x = background.get_width()
                    if x2 < -background.get_width():
                        x2 = background.get_width()
                    screen.blit(background, (x, 0))
                    screen.blit(background2, (x2, 0))
                    screen.blit(cacti, (obs_x, obs_y))
                    screen.blit(boy_run[int(i/4)%run_frames], (boy_x, boy_y))
                    boy_y -= jump_height[ii] * 2
                    ii += 1
                    pygame.display.update()
                    i += 1
                state = "R"
#            sys.exit
    x -= speed
    x2 -= speed
    if x < -background.get_width():
        x = background.get_width()
    if x2 < -background.get_width():
        x2 = background.get_width()
    screen.blit(background, (x, 0))
    screen.blit(background2, (x2, 0))
    for obsi in obs_list:
        obsi[1] -= speed
        screen.blit(obsi[0], (obsi[1], obsi[2]))
        if collide_rect(obsi[1], obsi[2], cacti.get_width(), cacti.get_height(), boy_x, boy_y, boy_size_x, boy_size_y):
            speed = 0
            boy_x -= 50
            state = "D"
            i = 0
    if state == "R":
        screen.blit(boy_run[int(i/4)%run_frames], (boy_x, boy_y))
        i += 1
    if state == "D":
        screen.blit(boy_dead[i], (boy_x, boy_y))
        if i < dead_frames-1:
            i += 1
        else:
            Running = False
    pygame.display.update()
    pygame.time.Clock().tick(30)
