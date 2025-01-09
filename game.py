from pygame import *
from random import *

init()

size = 600, 800
window = display.set_mode(size)
clock = time.Clock()
class GameSprite:
    def __init__(self,img,x,y,width,height):
        self.image = transform.scale(image.load(img), (width, height))
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.direction=None
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Platform:
    def __init__(self,x,y,width,height,color):
        self.rect=Rect(x,y,width,height)
        self.color=color
    def reset(self):
        draw.rect(window,self.color,self.rect)



player=GameSprite("character.png",200, 200, 60, 80)
lava=GameSprite("lava.png",0, 800, 600, 800)

BG = (100, 200, 200)

start_platform = [(50, 700), (400, 700), (200, 500), (50, 300), (400, 300)]
platforms = list()
for i in range(len(start_platform)):
    x=start_platform[i][0]
    y=start_platform[i][1]
    platform=Platform(x,y,120,25,(255,0,0))
    platforms.append(platform)

MAX_PLATFORMS = 5
MIN_DISTANCE = 150

def generate_platforms():
    if len(platforms) < MAX_PLATFORMS:
        x = randint(50, 450)
        y = randint(-850, size[1]//4)
        platform = Platform(x, y, 120, 25, (255, 0, 0))
        platforms.append(platform)

jump_height = 5
y_vel = 0.2
is_jump = True
game=True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            quit()
        if e.type == KEYDOWN:
            if e.key == K_r:
                finish = False
                platforms = list()
                for i in range(len(start_platform)):
                    x = start_platform[i][0]
                    y = start_platform[i][1]
                    platform = Platform(x, y, 120, 25, (255, 0, 0))
                    platforms.append(platform)
                player = GameSprite("character.png", 200, 200, 60, 80)
                lava = GameSprite("lava.png", 0, 800, 600, 800)
    window.fill(BG)

    if not finish:
        player.reset()x 
        for platform in platforms:
            draw.rect(window, (255, 0, 0), platform, border_radius=10)
            if platform.rect.y >= size[1]:
                platforms.remove(platform)
            if player.rect.colliderect(platform):
                is_jump = True
                jump_height = 10
            if player.rect.y <= 195:
                platform.rect.y += 10
                lava.rect.y += 2

    draw.rect(window, (255, 0, 0), lava)
    if lava.rect.colliderect(player.rect) or  player.rect.y>800:
        window.fill((255, 0, 0))
        finish = True

    display.update()
    clock.tick(60)

    if is_jump:
        player.rect.y -= jump_height
        jump_height -= y_vel

    keys = key.get_pressed()
    if keys[K_a]:
        player.rect.x -= 8
    if keys[K_d]:
        player.rect.x += 8
    lava.rect.y -= 1
    if player.rect.y <= 500:
        generate_platforms()

