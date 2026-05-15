# 1. INICIALIZACIÓN
import pygame
from pygame.locals import *  # Importa constantes como QUIT, KEYDOWN, K_a, etc.

pygame.init()
pygame.font.init()


# 2. CONFIGURACIÓN Y CONSTANTES
ANCHO, ALTO = 800, 600
FPS = 60
TITULO = 'Plantilla Base Pygame'
COLOR_FONDO = (30, 30, 30) # Gris oscuro
COLOR_BLANCO = (255, 255, 255) # Blanco

# Rutas de imágenes (ajusta los nombres a tus archivos reales)
IMG_JUGADOR = "speedbaba.gif"  # O "hero.png"
IMG_ENEMIGO = "BALDSKI.jpg"


# 3. DEFINICIÓN DE CLASES
class GameSprite(pygame.sprite.Sprite):
    """Clase base correcta que hereda de los Sprites de Pygame."""
    def __init__(self, sprite_img, x, y, w, h, speed):
        super().__init__()
        # Carga y escala la imagen
        self.image = pygame.transform.scale(pygame.image.load(sprite_img), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def reset(self, surface):
        """Dibuja el sprite individualmente (útil para el jugador)."""
        surface.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    """Clase para el personaje controlado por el usuario."""
    def update(self):
        keys = pygame.key.get_pressed()
        
        # Movimiento Horizontal
        if keys[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < ANCHO - self.rect.width:
            self.rect.x += self.speed
        
        # Movimiento Vertical
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < ALTO - self.rect.height:
            self.rect.y += self.speed


class Enemy(GameSprite):
    """Clase para enemigos que caen desde arriba."""
    def update(self):
        self.rect.y += self.speed
        # Si sale de la pantalla, reaparece arriba en una posición aleatoria
        if self.rect.y > ALTO:
            self.rect.y = -50
            # Importamos random aquí mismo para evitar desorden arriba
            import random
            self.rect.x = random.randint(0, ANCHO - self.rect.width)


# 4. INSTANCIACIÓN DE OBJETOS
window = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption(TITULO)
reloj = pygame.time.Clock()

# Creación de personajes
jugador = Player(IMG_JUGADOR, 360, ALTO - 120, 80, 100, 6)
lista_enemigos = pygame.sprite.Group()

# Creamos 3 enemigos de prueba en distintas posiciones X
enemigo1 = Enemy(IMG_ENEMIGO, 150, -100, 60, 60, 4)
enemigo2 = Enemy(IMG_ENEMIGO, 400, -250, 60, 60, 3)
enemigo3 = Enemy(IMG_ENEMIGO, 650, -50, 60, 60, 5)

# Los añadimos al grupo
lista_enemigos.add(enemigo1, enemigo2, enemigo3)


# 5. CICLO PRINCIPAL (GAME LOOP)
run = True
finish = False 

while run:
    # --- A. Gestión de Eventos ---
    for e in pygame.event.get():
        if e.type == QUIT:
            run = False
        
        if e.type == KEYDOWN:
            if e.key == K_r:
                # Reinicio básico
                finish = False
                jugador.rect.x = 360
                jugador.rect.y = ALTO - 120
                for enemy in lista_enemigos:
                    enemy.rect.y = -100

    # --- B. Lógica del Juego ---
    if not finish:
        window.fill(COLOR_FONDO)

        # Actualizar posiciones
        jugador.update()
        lista_enemigos.update()

        # Dibujar elementos
        jugador.reset(window)
        lista_enemigos.draw(window)  # Dibuja TODO el grupo a la vez

        # Colisiones (Activa esto si quieres que el juego se detenga al chocar)
        if pygame.sprite.spritecollide(jugador, lista_enemigos, False):
            window.fill(COLOR_BLANCO)
            # finish = True 

    # --- C. Actualización de Pantalla ---
    pygame.display.update()
    reloj.tick(FPS)

pygame.quit()
