from code.const import ENTITY_SPEED
from code.entity import Entity


class EnemyShot(Entity):

    def __int__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self, ):
        self.rect.centerx -= ENTITY_SPEED[self.name]
