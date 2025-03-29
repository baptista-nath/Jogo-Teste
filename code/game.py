from code.const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.level import Level

from menu import Menu
import pygame


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                Level(self.window, 'Level1', menu_return)
            elif menu_return == MENU_OPTION[4]:
                pygame.quit()
                quit()
            else:
                pass
