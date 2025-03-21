import pygame

from code.const import WIN_WIDTH, WIN_HEIGHT
from menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        menu = Menu(self.window)

        while True:
            menu = Menu(self.window)
            menu.run()
            pass


if __name__ == "__main__":
    game = Game()
    game.run()
