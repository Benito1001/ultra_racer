import pygame
from entity import Entity
from hitbox import Hitbox

class Circle(Entity):
	def __init__(self, context, x, y, r):
		Entity.__init__(self, context, x, y)
		self.r = r
		self.hitbox = Hitbox(context, self.pos-(r, r), self.r*2, self.r*2)
		self.shape = "circle"

		self.Surface = pygame.Surface((self.px2m(self.r*2), self.px2m(self.r*2)))
		self.Surface.fill((255, 255, 255))
		pygame.draw.circle(self.Surface, (0, 0, 0), self.px2m_tuple(self.r, self.r), self.px2m(self.r))
		self.Surface = self.Surface.convert()
