import pygame
import numpy as np
from vector2 import Vec2d
from entity import Entity

class DVec(Entity):
	def __init__(self, context, x, y, vx, vy):
		Entity.__init__(self, context, x, y)
		self.vec = Vec2d(vx, vy)

		self.Surface = pygame.Surface(self.px2m_tuple(*abs(self.vec)))
		self.Surface.fill((255, 255, 255))
		self.Surface.set_colorkey((255, 255, 255))
		pygame.draw.lines(self.Surface, (0, 0, 255), False, [(0, 0), self.px2m_tuple(*self.vec)], 1)
		self.Surface = self.Surface.convert()

	def draw(self):
		pygame.draw.lines(self.Surface, (0, 0, 255), False, [(0, 0), self.px2m_tuple(*self.vec)], 1)

	def update(self, entities, dt):
		pass
