import pygame
import pytmx


class GameMap:
    def __init__(self, path, screen_dimensions):
        self.path = path
        self.map_tmx = pytmx.load_pygame(path)
        self.width, self.height = screen_dimensions
        self.hitbox = (self.width + 20, self.height, 28, 60)

    def draw(self, screen):
        for layer in self.map_tmx.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid in layer:
                    tile = self.map_tmx.get_tile_image_by_gid(gid)
                    if tile:
                        screen.blit(tile, (x * self.map_tmx.tilewidth, y * self.map_tmx.tileheight))

    def get_all_layers(self):
        all_layers = self.map_tmx.visible_layers
        return all_layers
