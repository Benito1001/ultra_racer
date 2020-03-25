import pygame
from vector2 import Vec2d
import numpy as np
from circle import Circle
from collision_logic import collides

class Player(Circle):
	def __init__(self, context, x, y, r):
		Circle.__init__(self, context, x, y, r)

		self.mass = 1
		self.force = Vec2d(0, 0)
		self.acc = Vec2d(0, 0)
		self.vel = Vec2d(0, 0)
		self.power = 12
		self.keys = {}

	def update(self, entities, dt):
		self.update_pos(dt)
		for entity in entities:
			if entity != self and self.hitbox.collides(entity.hitbox):
				colliding, collision_depth, collision_vec = collides(self, entity)
				if colliding:
					self.force += collision_vec*2000*collision_depth**(3/2)

	def update_pos(self, dt):
		if self.keys.get("w"):
			self.force.y -= self.power
		if self.keys.get("s"):
			self.force.y += self.power
		if self.keys.get("a"):
			self.force.x -= self.power
		if self.keys.get("d"):
			self.force.x += self.power
		self.restrain()
		self.friction()

		self.acc = self.force/self.mass
		self.vel += self.acc*dt
		self.pos += self.vel*dt
		self.hitbox.update(self.pos)
		self.force.x, self.force.y = 0, 0

	def draw(self):
		self.color = (0, 100, 200)
		pygame.draw.circle(self.Surface, (self.color), self.px2m_tuple(self.r, self.r), self.px2m(self.r))
		self.Surface.convert()
		self.context.screen.blit(self.Surface, self.px2m_tuple(self.pos.x, self.pos.y))

	def get_friction(self, D):
		return -D*self.vel

	def friction(self):
		D = 1
		self.force += self.get_friction(D)

	def restrain(self):
		k = 2000
		d = 5
		spring_force = lambda sign, r, ax: sign*k*abs(r)**(3/2) + self.get_friction(d)[ax]
		# Contain using a spring force
		if self.pos.x < 0:
			self.force.x += spring_force(1, self.pos.x, 0)
		if self.pos.y < 0:
			self.force.y += spring_force(1, self.pos.y, 1)

		if self.pos.x + 2*self.r > self.screen_w:
			self.force.x += spring_force(-1, self.pos.x + 2*self.r - self.screen_w, 0)
		if self.pos.y + 2*self.r > self.screen_h:
			self.force.y += spring_force(-1, self.pos.y + 2*self.r - self.screen_h, 1)
