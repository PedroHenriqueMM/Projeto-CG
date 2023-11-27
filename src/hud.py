import pygame

class HUD:
    def __init__(self):
        self.font = pygame.font.SysFont('Arial', 24)

    def draw(self, screen, health, ammo, money):
        health_text = self.font.render(f"HP: {health}", True, (255, 0, 0))
        ammo_text = self.font.render(f"Ammo: {ammo[0]}/{ammo[1]}", True, (255, 255, 255))
        money_text = self.font.render(f"${money}", True, (0, 255, 0))

        screen.blit(health_text, (10, 10))
        screen.blit(ammo_text, (10, 40))
        screen.blit(money_text, (10, 70))