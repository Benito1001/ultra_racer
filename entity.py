import pygame
import pygame.math as math

class Entity(object):
	def __init__(self, context, x, y):
		self.context = context
		self.px2m = self.context.px2m_func
		self.px2m_tuple = self.context.px2m_tuple
		self.screen_w = self.context.screen_size_m.w
		self.screen_h = self.context.screen_size_m.h
		self.pos = math.Vector2(x, y)
