#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(600, 400))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu.run()
            pass

            # check for all events
            #  for event in pygame.event.get():
            #  if event.type == pygame.QUIT:
            #       pygame.quit()
            #         quit()  # end pygame
