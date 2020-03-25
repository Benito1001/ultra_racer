import pygame
import numpy as np
from vector2 import Vec2d
from entity import Entity
from hitbox import Hitbox

class Block(Entity):
	def __init__(self, context, x, y, w, h):
		Entity.__init__(self, context, x, y)
		self.w = w
		self.h = h
		self.hitbox = Hitbox(context, self.pos, self.w, self.h)
		self.corners = [
			Vec2d(self.pos), Vec2d(self.pos+(self.w, 0)),
			Vec2d(self.pos+(self.w, self.h)), Vec2d(self.pos+(0, self.h))
		]
		self.shape = "square"

		self.Surface = pygame.Surface((self.px2m(self.w), self.px2m(self.h)))
		self.Surface.fill((255, 255, 255))
		pygame.draw.rect(self.Surface, (0, 0, 0), pygame.Rect(
			0, 0, self.px2m(self.w), self.px2m(self.h)
		))
		self.Surface = self.Surface.convert()

	def draw(self):
		self.context.screen.blit(self.Surface, self.px2m_tuple(self.pos.x, self.pos.y))

	def update(self, entities, dt):
		self.hitbox.update(self.pos)

	def get_corner(self, angle):
		if angle > 0:
			if angle < np.pi/2:
				return self.corners[0]
			return self.corners[1]
		if angle <= 0:
			if angle > -np.pi/2:
				return self.corners[3]
			return self.corners[2]
