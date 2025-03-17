#!/usr/bin/python
# -*- coding: utf-8 -*-

from Entity import Entity
from Player import Player


class Entity(Entity, Player):
    def __init__(self):
        self.name = None
        self.surf = None
        self.rect = None

    def move(self, ):
        pass
