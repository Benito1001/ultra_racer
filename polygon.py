import pygame
from vector2 import Vec2d
from physics_body import PhysicsBody
from hitbox import Hitbox

class Polygon(PhysicsBody):
	def __init__(self, context, point_list, mass, moofin, immovable=False, imrotatable=False):
		self.update_points(point_list)
		self.mass = mass
		self.moofin = moofin
		PhysicsBody.__init__(self, context, self.hitbox.pos.x, self.hitbox.pos.y, immovable, imrotatable)
		self.update_surface()
		self.shape = "polygon"

	def draw(self):
		if self.surface_dirty:
			self.update_surface()
		self.context.screen.blit(self.Surface, self.px2m_tuple(self.pos.x, self.pos.y))

	def update(self, entities, dt):
		pass

	def set_pos(self, dt):
		for point in self.points:
			point += self.vel*dt
		self.hitbox.update(self.pos)
		self.mid = self.get_mid()

	def update_points(self, point_list):
		self.points = point_list
		# close points list
		if self.points[0].x != self.points[-1].x or self.points[0].y != self.points[-1].y:
			self.points.append(Vec2d(self.points[0].x, self.points[0].y))

		self.mid = self.get_mid()
		self.edges = self.get_edges()
		self.hitbox = self.get_hitbox()
		self.pos = self.hitbox.pos
		self.surface_dirty = True

	def update_surface(self):
		self.Surface = pygame.Surface((self.px2m(self.hitbox.w), self.px2m(self.hitbox.h)))
		self.Surface.fill((255, 255, 255))
		self.Surface.set_colorkey((255, 255, 255))
		pygame.draw.polygon(self.Surface, (0, 0, 0), [self.px2m_tuple(*(point - self.pos)) for point in self.points])
		self.Surface = self.Surface.convert()
		self.surface_dirty = False

	def get_mid(self):
		return sum(self.points[:-1])/(len(self.points) - 1)

	def get_edges(self):
		edges = []
		for i in range(len(self.points) - 1):
			edges.append([self.points[i], self.points[i+1]])
		return edges

	def get_hitbox(self):
		top = self.points[0].y
		bottom = self.points[0].y
		left = self.points[0].x
		right = self.points[0].x
		for point in self.points[1:]:
			top = min(top, point.y)
			bottom = max(bottom, point.y)
			left = min(left, point.x)
			right = max(right, point.x)
		return Hitbox(Vec2d(left, top), right-left, bottom-top)
