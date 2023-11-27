import pygame
import time
import math
from src.player import Player
from src.bullet import Bullet
from src.hud import HUD
from game_map import GameMap
import pytmx

def check_collision(player_rect, tiles):
    for tile in tiles:
        print(player_rect.colliderect(tile))
        if player_rect.colliderect(tile):
            return True
    return False
def game_loop():
    clock = pygame.time.Clock()
    pygame.init()

    width, height = 1600, 900
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('CS2D')

    player = Player((width // 2, height // 2))
    bullets = []

<<<<<<< HEAD
    game_map = GameMap('../map/game_map.tmx', (width, height))
=======
    game_map = GameMap('assets/images/mapa.png', (width, height))

>>>>>>> parent of 2b873b6 (hud melhorado)
    hud = HUD()

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

        # Atualiza o jogador
        player.update()
        screen.fill((0, 0, 0))

        all_layers = game_map.get_all_layers()

        for layer in all_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                tiles = [
                    pygame.Rect(x * game_map.map_tmx.tilewidth, y * game_map.map_tmx.tileheight, game_map.map_tmx.tilewidth, game_map.map_tmx.tileheight)
                    for x, y, _ in layer.iter_data()]
                if check_collision(player.hitbox, tiles):
                    print("Colisão com o mapa!")
                else:
                    print("Não está colidindo!")

                for tile in tiles:
                    pygame.draw.rect(screen, (255, 0, 0), tile,
                                     2)  # Desenha um retângulo vermelho ao redor do hitbox do mapa

        # Desenha o mapa
        game_map.draw(screen)

        # Atualiza e desenha as balas
        for bullet in bullets[:]:
            if bullet.update(width, height):
                bullets.remove(bullet)
            else:
                screen.blit(bullet.image, bullet.rect.topleft)

        # Desenha o jogador
        screen.blit(player.image, player.rect.topleft)
        pygame.draw.rect(screen, (255, 0, 0), player.hitbox, 2)

        # Desenha o HUD
        hud.draw(screen, player.health, player.ammo, player.money)

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    game_loop()
