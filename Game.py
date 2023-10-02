import pygame
import math
import time
from map import GameMap

class Player:
    def __init__(self, pos):
        self.original_image = pygame.image.load('images/player_sprite.png')
        self.original_image = pygame.transform.scale(self.original_image, (129, 110))
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect(center=pos)
        self.pos = pygame.math.Vector2(pos)
        self.speed = 5

    def update(self):
        self.rotate()
        self.move()

    def rotate(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        angle = math.atan2(mouse_y - self.pos.y, mouse_x - self.pos.x)
        angle = math.degrees(angle)
        self.image = pygame.transform.rotate(self.original_image, -angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def move(self):
        keys = pygame.key.get_pressed()
        dx, dy = 0, 0
        if keys[pygame.K_a]:
            dx = -self.speed
        if keys[pygame.K_d]:
            dx = self.speed
        if keys[pygame.K_w]:
            dy = -self.speed
        if keys[pygame.K_s]:
            dy = self.speed
        self.pos.x += dx
        self.pos.y += dy
        self.rect.center = self.pos

class Bullet:
    def __init__(self, pos, angle):
        self.image = pygame.image.load('images/bullet_sprite.png')
        self.rect = self.image.get_rect(center=pos)
        self.pos = pygame.math.Vector2(pos)
        self.speed = 15
        self.angle = angle
        self.dx = self.speed * math.cos(math.radians(angle))
        self.dy = self.speed * math.sin(math.radians(angle))

    def update(self):
        self.pos.x += self.dx
        self.pos.y += self.dy
        self.rect.center = self.pos


def game_loop():
    pygame.init()

    width, height = 1600, 900
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('CS2D')

    player = Player((width // 2, height // 2))
    bullets = []

    game_map = GameMap('images/mapa.png', (width, height))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    angle = math.degrees(
                        math.atan2(pygame.mouse.get_pos()[1] - player.pos.y, pygame.mouse.get_pos()[0] - player.pos.x))
                    bullet = Bullet(player.pos, angle)
                    bullets.append(bullet)

        player.update()
        screen.fill((0, 0, 0))

        # Desenha o mapa
        game_map.draw(screen)

        for bullet in bullets:
            bullet.update()
            screen.blit(bullet.image, bullet.rect.topleft)

        screen.blit(player.image, player.rect.topleft)

        pygame.display.flip()
        time.sleep(1 / 60.0)


if __name__ == "__main__":
    game_loop()
