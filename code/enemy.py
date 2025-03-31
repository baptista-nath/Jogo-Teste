import random
from code.const import ENTITY_SPEED, WIN_WIDTH, ENTITY_SHOT_DELAY
from code.entity import Entity
from code.enemyShot import EnemyShot  # Importa a classe do tiro inimigo


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]  # Define o tempo entre os tiros

    def move(self):
        """Movimento do inimigo para a esquerda"""
        self.rect.centerx -= ENTITY_SPEED[self.name]
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH

    def shoot(self):
        """O inimigo atira automaticamente em intervalos"""
        self.shot_delay -= 1
        if self.shot_delay <= 0:  # Quando o tempo chega a zero, atira
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]  # Reseta o tempo para o próximo tiro
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))

        return None  # Retorna None se ainda não for o momento do tiro
