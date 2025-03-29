#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.background import Background


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str):  # Corridor o argumento
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(7):
                    list_bg.append(Background(f'Level1Bg{i}', (0, 0)))  # Corridor a chimaera
                return list_bg  # Agora o return est fora do loop
