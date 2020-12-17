from vector2 import Vec2d
from entity import Entity

class PhysicsBody(Entity):
	def __init__(self, context, x, y, immovable=False, imrotatable=False):
		self.immovable = immovable
		self.imrotatable = imrotatable

		Entity.__init__(self, context, x, y)
		self.vel = Vec2d(0, 0)
		self.acc = Vec2d(0, 0)
		self.force = Vec2d(0, 0)

		self.rot = 0
		self.rot_vel = 0
		self.rot_acc = 0
		self.tourqe = 0

	def physics_update(self, dt):
		if not self.immovable:
			self.acc = self.force/self.mass
			self.vel += self.acc*dt
			self.pos += self.vel*dt
			self.force = Vec2d(0, 0)

		if not self.imrotatable:
			self.rot_acc = self.tourqe/self.moofin
			self.rot_vel += self.rot_acc*dt
			self.rot += self.rot_vel*dt
			self.tourqe = 0
