from math import pi
import pygame
from physics_body import PhysicsBody
from hitbox import Hitbox

class Circle(PhysicsBody):
	def __init__(self, context, x, y, r, density, color):
		self.mass = density*pi*r**2
		PhysicsBody.__init__(self, context, x, y, imrotatable=True)
		self.r = r
		self.color = color
		self.hitbox = Hitbox(self.pos-(self.r, self.r), self.r*2, self.r*2)
		self.shape = "circle"

		self.Surface = pygame.Surface((self.px2m(self.r*2), self.px2m(self.r*2)))
		self.Surface.fill((255, 255, 255))
		pygame.draw.circle(self.Surface, (0, 0, 0), self.px2m_tuple(self.r, self.r), self.px2m(self.r))
		self.Surface = self.Surface.convert()

	def draw(self):
		pygame.draw.circle(self.Surface, (self.color), self.px2m_tuple(self.r, self.r), self.px2m(self.r))
		self.Surface.convert()
		self.context.screen.blit(self.Surface, self.px2m_tuple(self.pos.x, self.pos.y))
