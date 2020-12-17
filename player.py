import pygame
from vector2 import Vec2d
import numpy as np
from circle import Circle
from collision_logic import collides

class Player(Circle):
	def __init__(self, context, x, y, r):
		Circle.__init__(self, context, x, y, r, 1, (100, 200, 0))

		self.mass = 1
		self.force = Vec2d(0, 0)
		self.acc = Vec2d(0, 0)
		self.vel = Vec2d(0, 0)
		self.power = 12
		self.keys = {}

	def update(self, entities, dt):
		self.force_update(dt)
		self.collision_update(entities)
		self.physics_update(dt)
		self.hitbox.update(self.pos)

	def collision_update(self, entities):
		for entity in entities:
			if entity != self and hasattr(entity, "hitbox") and self.hitbox.collides(entity.hitbox):
				colliding, collision_depth, collision_vec, collision_point = collides(self, entity)
				if colliding:
					spring_force = collision_vec*2000*collision_depth**(3/2)
					self.force += spring_force
					entity.force -= spring_force

					self.tourqe += spring_force.cross(collision_point - self.pos)
					entity.tourqe += spring_force.cross(collision_point - entity.mid)

	def force_update(self, dt):
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
