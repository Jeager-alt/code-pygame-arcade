import pygame
from pygame.locals import *
import random

pygame.init()
pygame.font.init()

# CONFIGURACIÓN Y CONSTANTES
ANCHO, ALTO = 800, 600
FPS = 60
TITULO = 'Plantilla Base Pygame'
COLOR_FONDO = (30, 30, 30) 
COLOR_BLANCO = (255, 255, 255) 
COLOR_ROJO = (255, 50, 50)

# Fuentes para el texto
fuente_hud = pygame.font.SysFont('Arial', 25, bold=True)
fuente_gameover = pygame.font.SysFont('Arial', 50, bold=True)

# Rutas de imágenes
IMG_JUGADOR = "speedbaba.gif"  
IMG_ENEMIGO = "BALDSKI.jpg"
IMG_BALA = "bala.png"  

# Inicializar ventana
window = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption(TITULO)
reloj = pygame.time.Clock()

# CARGA Y ESCALADO DE IMÁGENES
SURFACE_JUGADOR = pygame.transform.scale(pygame.image.load(IMG_JUGADOR), (65, 65))
SURFACE_ENEMIGO = pygame.transform.scale(pygame.image.load(IMG_ENEMIGO), (60, 60))
SURFACE_BALA = pygame.transform.scale(pygame.image.load(IMG_BALA), (15, 30))

# VARIABLES DE JUEGO (Puntos y Vidas)
puntos = 0
vidas = 3

# DEFINICIÓN DE CLASES
class GameSprite(pygame.sprite.Sprite):
    def __init__(self, preloaded_image, x, y, speed):
        super().__init__()
        self.image = preloaded_image  
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def reset(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < -30:
            self.kill()

class Player(GameSprite):
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < ANCHO - self.rect.width:
            self.rect.x += self.speed
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < ALTO - self.rect.height:
            self.rect.y += self.speed

    def fire(self):
        bx = self.rect.centerx - (15 // 2)
        by = self.rect.top
        nueva_bala = Bullet(SURFACE_BALA, bx, by, 12)
        lista_balas.add(nueva_bala)

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > ALTO:
            self.respawn()

    def respawn(self):
        self.rect.y = random.randint(-150, -50)
        self.rect.x = random.randint(0, ANCHO - self.rect.width)

# INSTANCIACIÓN DE OBJETOS
lista_enemigos = pygame.sprite.Group()
lista_balas = pygame.sprite.Group()  

jugador = Player(SURFACE_JUGADOR, 360, ALTO - 120, 7)

enemigo1 = Enemy(SURFACE_ENEMIGO, 150, -100, 4)
enemigo2 = Enemy(SURFACE_ENEMIGO, 400, -250, 3)
enemigo3 = Enemy(SURFACE_ENEMIGO, 650, -50, 5)

lista_enemigos.add(enemigo1, enemigo2, enemigo3)

# GAME LOOP
run = True
finish = False 

while run:
    for e in pygame.event.get():
        if e.type == QUIT:
            run = False
        if e.type == KEYDOWN:
            if e.key == K_r:
                # REINICIAR EL JUEGO AL PRESIONAR 'R'
                finish = False
                puntos = 0
                vidas = 3
                jugador.rect.x = 360
                jugador.rect.y = ALTO - 120
                lista_balas.empty()  
                for enemy in lista_enemigos:
                    enemy.respawn()
            if e.key == K_SPACE and not finish:
                jugador.fire()

    if not finish:
        window.fill(COLOR_FONDO)

        # Actualizar lógica
        jugador.update()
        lista_enemigos.update()
        lista_balas.update()  

        # Dibujar personajes
        jugador.reset(window)
        lista_enemigos.draw(window) 
        lista_balas.draw(window)  

        # --- COLISIÓN: Bala golpea Enemigo (Suma puntos) ---
        colisiones = pygame.sprite.groupcollide(lista_balas, lista_enemigos, True, False)
        for bala, enemigos_tocados in colisiones.items():
            for enemigo in enemigos_tocados:
                puntos += 1  # Sumamos un punto por cada enemigo destruido
                enemigo.respawn()  

        # --- COLISIÓN: Enemigo golpea al Jugador (Resta vidas) ---
        enemigos_choque = pygame.sprite.spritecollide(jugador, lista_enemigos, False)
        if enemigos_choque:
            vidas -= 1  # Perder una vida
            for enemigo in enemigos_choque:
                enemigo.respawn()  # Mandamos lejos al enemigo que nos chocó para que no nos quite todas las vidas juntas
            
            if vidas <= 0:
                finish = True  # Activamos el estado de fin de juego

        # --- DIBUJAR CONTADORES (HUD) ---
        texto_puntos = fuente_hud.render(f"Puntos: {puntos}", True, COLOR_BLANCO)
        texto_vidas = fuente_hud.render(f"Vidas: {vidas}", True, COLOR_ROJO)
        window.blit(texto_puntos, (20, 20))
        window.blit(texto_vidas, (20, 55))

    else:
        # --- PANTALLA DE GAME OVER ---
        window.fill((10, 10, 10)) # Fondo oscuro para el Game Over
        
        texto_gameover = fuente_gameover.render("GAME OVER", True, COLOR_ROJO)
        texto_score_final = fuente_hud.render(f"Puntuación Final: {puntos}", True, COLOR_BLANCO)
        texto_reiniciar = fuente_hud.render("Presiona 'R' para volver a jugar", True, COLOR_BLANCO)
        
        # Centrar los textos en la pantalla
        window.blit(texto_gameover, (ANCHO // 2 - texto_gameover.get_width() // 2, ALTO // 2 - 80))
        window.blit(texto_score_final, (ANCHO // 2 - texto_score_final.get_width() // 2, ALTO // 2))
        window.blit(texto_reiniciar, (ANCHO // 2 - texto_reiniciar.get_width() // 2, ALTO // 2 + 50))

    pygame.display.update()
    reloj.tick(FPS)

pygame.quit()
