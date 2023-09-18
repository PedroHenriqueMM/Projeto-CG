import pygame
import time


def game_loop():
    pygame.init()

    width, height = 1280, 720
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Meu Jogo Suave')

    player_sprite = pygame.image.load('images/player_sprite.jpg')
    enemy_sprite = pygame.image.load('images/enemy_sprite.jpg')
    grass_sprite = pygame.image.load('images/grass.jpeg')
    stone_sprite = pygame.image.load('images/stone.jpeg')
    bullet_sprite = pygame.image.load('images/bullet_sprite.jpg')

    game_map = [
        [1, 1, 1, 1, 1, 2, 2, 1],
        [1, 0, 0, 2, 0, 0, 2, 1],
        [1, 0, 3, 2, 3, 0, 0, 1],
        [1, 2, 0, 0, 0, 2, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1]
    ]

    tile_size = min(width // len(game_map[0]), height // len(game_map))
    player_pos = [3 * tile_size, 3 * tile_size]
    bullets = []

    move_speed = 5

    player_sprite = pygame.transform.scale(player_sprite, (tile_size // 2, tile_size // 2))
    enemy_sprite = pygame.transform.scale(enemy_sprite, (tile_size // 2, tile_size // 2))
    bullet_sprite = pygame.transform.scale(bullet_sprite, (tile_size // 4, tile_size // 4))
    grass_sprite = pygame.transform.scale(grass_sprite, (tile_size, tile_size))
    stone_sprite = pygame.transform.scale(stone_sprite, (tile_size, tile_size))

    running = True
    while running:
        keys = pygame.key.get_pressed()
        move_x, move_y = 0, 0
        enemy_rect = pygame.Rect(0, 0, 0, 0)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullets.append({"x": player_pos[0], "y": player_pos[1],
                                    "rect": pygame.Rect(player_pos[0], player_pos[1], tile_size // 4, tile_size // 4)})

        # Note that the code below is now indented to be part of the while loop
        if keys[pygame.K_LEFT]:
            move_x = -move_speed
        if keys[pygame.K_RIGHT]:
            move_x = move_speed
        if keys[pygame.K_UP]:
            move_y = -move_speed
        if keys[pygame.K_DOWN]:
            move_y = move_speed

        new_x = player_pos[0] + move_x
        new_y = player_pos[1] + move_y
        new_rect = pygame.Rect(new_x, new_y, tile_size // 2, tile_size // 2)

        collision = False
        for i in range(len(game_map)):
            for j in range(len(game_map[i])):
                tile_type = game_map[i][j]
                tile_rect = pygame.Rect(j * tile_size, i * tile_size, tile_size, tile_size)

                if tile_type == 3:
                    enemy_rect = pygame.Rect(j * tile_size + tile_size // 4, i * tile_size + tile_size // 4,
                                             tile_size // 2, tile_size // 2)

                if tile_type == 2:
                    if new_rect.colliderect(tile_rect):
                        collision = True

                if tile_type == 3:
                    if new_rect.colliderect(enemy_rect):
                        collision = True

                for bullet in bullets:
                    bullet_rect = pygame.Rect(bullet['x'] + tile_size // 4, bullet['y'] + tile_size // 4,
                                              tile_size // 4, tile_size // 4)
                    if bullet_rect.colliderect(enemy_rect):
                        bullets.remove(bullet)
                        game_map[i][j] = 0

            if collision:
                break

        if not collision:
            player_pos[0] = new_x
            player_pos[1] = new_y

        for bullet in bullets:
            bullet['y'] -= 5
            bullet['rect'].y = bullet['y']

        for i in range(len(game_map)):
            for j in range(len(game_map[i])):
                if game_map[i][j] == 3:
                    enemy_rect = pygame.Rect(j * tile_size, i * tile_size, tile_size, tile_size)
                    for bullet in bullets:
                        if bullet['rect'].colliderect(enemy_rect):
                            game_map[i][j] = 0
                            bullets.remove(bullet)

        screen.fill((0, 0, 0))
        for i in range(len(game_map)):
            for j in range(len(game_map[i])):
                if game_map[i][j] == 1:
                    screen.blit(grass_sprite, (j * tile_size, i * tile_size))
                elif game_map[i][j] == 2:
                    screen.blit(stone_sprite, (j * tile_size, i * tile_size))
                elif game_map[i][j] == 3:
                    screen.blit(enemy_sprite, (j * tile_size, i * tile_size))

        for bullet in bullets:
            screen.blit(bullet_sprite, (bullet['x'], bullet['y']))

        screen.blit(player_sprite, (player_pos[0], player_pos[1]))

        pygame.display.flip()
        time.sleep(1 / 60.0)

# Para testar a função game_loop
if __name__ == "__main__":
    game_loop()
