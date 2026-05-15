ANCHO, ALTO = 640, 480
TITULO ="Intro a Pygame" 
COLOR_FONDO = (200, 128 , 230)
SQUARE_COLOR=(252, 186, 3)
WHITE = (255, 255, 255 )
BLACK = (0,0,0) 
PLAYER_IMG 
enemy_img 
# PANTALLA
screen = display.set_mode()
display.set_caption(TITULO)
FPS = 60
WALL_COLOR = (3, 227, 252)

# CLASE PADRE
class GameSprite(sprite.Sprite):
    def __init__(self, img, cor_x, cor_y, speed=0):
        super().__init__()
        self.image = transform.scale(image.load(img), (60, 60))
        self.rect = self.image.get_rect()
        self.rect.x = cor_x
        self.rect.y = cor_y
        self.speed = speed

    def reset(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))


class Player (GameSprite):

    def update (self):
        keys = key.get_pressed()
        if keys [K_d]:
            self.rect.x += self.speed
        if keys [K_a]: 
            self.rect.x -= self.speed
        if keys [K_s]:
            self.rect.y += self.speed
        if keys [K_w]:
            self.rect.y -= self.speed





class Enemy(GameSprite):
    def __init__(self, img, cor_x, cor_y, speed):
        super().__init__(img, cor_x, cor_y, speed)

        self.move_rigth = True # ESTADO INICIAL

    def update(self):
        if self.move_rigth:
            self.rect.x += self.speed
            if self.rect.x >= ANCHO - 69:
                self.move_rigth = False
        else:
            self.rect.x -= self. speed
            if self.rect.x <= 0:
                self.movwe_rigth = True 

# Clase para la paredes
class Wall (sprite.Sprite):
    def __init__(self, color, cor_x, cor_y, sprite_width, sprite_height):
        self.width = sprite_width
        self.height = sprite_height
        self.color = color
        self.image = Surface([self.width,self.height])
        self.rect = self.image.get_rect()
        self.rect.x =  cor_x
        self.rect.y =  cor_y
        
    def draw_wall(self):
        draw.rect(screen, self.color, self.rect)

def __init__(self, color, cor_x, cor_y, sprite_width, sprite_height):
        self.width = sprite_width
        self.height = sprite_height
        self.color = color
        self.image = Surface([self.width,self.height])
        self.rect = self.image.get_rect()
        self.rect.x =  cor_x
        self.rect.y =  cor_y
        
        def draw_wall(self):
            draw.rect(screen, self.color, self.rect)
wall_1 = Wall(WALL_COLOR, 220, 60, 100, 15)
wall_2 = Wall(WALL_COLOR, 220, 3, 20, 227)


if sprite.collide_rect(enemy, jugador):
    done = True
screen.fill(BLACK)

if sprite.collide_rect(goal; jugador) or sprite.collide_rect



 
player = Player(PLAYER_IMG, 30, 30, 2)
enemy = Enemy(enemy_img , 30, 30 , 2)

run = True
done = False 
clock = time.Clock()
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    if not done: 
        screen.fill(COLOR_FONDO)
        player.reset()
        player.update()
        enemy.reset()
        enemy.update()
        wall_1.draw_wall()
        wall_2.draw_wall()


    display.update()
    clock.tick(FPS)
quit()
