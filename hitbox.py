from vector2 import Vec2d

class Hitbox(object):

	def __init__(self, context, pos, w, h):
		self.context = context
		self.pos = pos
		self.type = type
		self.w = w
		self.h = h
		self.mid = Vec2d(self.pos.x + self.w/2, self.pos.y + self.h/2)

	def update(self, pos):
		self.pos = pos
		self.mid.x = self.pos.x + self.w/2
		self.mid.y = self.pos.y + self.h/2

	def collides(self, other):
		if (
			self.pos.x + self.w > other.pos.x and self.pos.x < other.pos.x + other.w
			and self.pos.y + self.h > other.pos.y and self.pos.y < other.pos.y + other.h
		):
			return True
		return False
