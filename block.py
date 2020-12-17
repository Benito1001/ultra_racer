from numpy import pi
from vector2 import Vec2d
from polygon import Polygon

class Block(Polygon):
	def __init__(self, context, x, y, w, h, density, rot=0):
		self.w = w
		self.h = h
		self.mid = Vec2d(x + self.w/2, y + self.h/2)

		mass = density*w*h
		moofin = (w**2 + h**2)/12 * mass
		Polygon.__init__(self, context, self.get_vertices(rot), mass, moofin, immovable=True)
		self.rot = rot

	def update(self, entities, dt):
		self.physics_update(dt)
		self.set_pos(dt)
		self.update_points(self.get_vertices(self.rot))

	def get_vertices(self, rot):
		vertices = [
			Vec2d(self.mid.x - self.w/2, self.mid.y - self.h/2),
			Vec2d(self.mid.x + self.w/2, self.mid.y - self.h/2),
			Vec2d(self.mid.x + self.w/2, self.mid.y + self.h/2),
			Vec2d(self.mid.x - self.w/2, self.mid.y + self.h/2),
			Vec2d(self.mid.x - self.w/2, self.mid.y - self.h/2)
		]
		return [self.mid + (vertex - self.mid).rotate(rot) for vertex in vertices]
