import pygame
import sys
from Game import game_loop  # Certifique-se de que Game.py está na mesma pasta e contém a função game_loop

def main_menu():
    pygame.init()
    width, height = 1280, 720
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Menu do Meu Jogo Suave')

    menu = True
    running = False  # Variável para verificar se o jogo está em execução

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()  # Encerra o programa completamente

        screen.fill((0, 0, 0))

        font = pygame.font.SysFont(None, 50)
        text = font.render('Meu Jogo Suave', True, (255, 255, 255))
        screen.blit(text, [width // 4, height // 4])

        text = font.render('Pressione [Enter] para começar ou [Q] para sair', True, (255, 255, 255))
        screen.blit(text, [width // 4, height // 2])

        pygame.display.update()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_RETURN]:
            if not running:
                print("Iniciando o jogo...")
                pygame.time.delay(200)  # Adiciona um pequeno atraso
                running = True
                game_loop()  # Inicie o jogo
                running = False  # Reinicialize a variável running

        if keys[pygame.K_q]:
            pygame.quit()
            sys.exit()  # Encerra o programa completamente

if __name__ == "__main__":
    main_menu()
