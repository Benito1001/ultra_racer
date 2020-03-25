import pygame
from player import Player
from block import Block
pygame.init()

clock = pygame.time.Clock()
mainloop = True
fps = 60
playtime = 0.0

px2m = 50


class Size(object):
	def __init__(self, w, h):
		self.w = w
		self.h = h
screen_size = Size(720, 480)
screen = pygame.display.set_mode((screen_size.w, screen_size.h))

background = pygame.Surface(screen.get_size())
background.fill((255, 255, 255))
background = background.convert()
screen.blit(background, (0, 0))

class Context():
	px2m = px2m
	px2m_func = lambda self, n: n*px2m
	px2m_tuple = lambda self, x, y: (x*px2m, y*px2m)
	screen_size_px = screen_size
	screen_size_m = Size(screen_size_px.w/px2m, screen_size_px.h/px2m)
	screen = screen
	background = background
context = Context()


player = Player(context, 0.5, 0.5, 1)

entities = [
	player,
	Block(context, 5, 5, 1, 1)
]


while mainloop:
	# Print framerate and playtime in titlebar
	milliseconds = clock.tick(fps)
	true_fps = clock.get_fps()
	playtime += milliseconds/1000
	text = f"fps: {true_fps:.2f}   Speed: {player.vel.length:.2f}"
	pygame.display.set_caption(text)
	if true_fps != 0:
		dt = 1/true_fps
	else:
		dt = 1/fps

	# Update and Draw
	for entity in entities:
		for i in range(10):
			entity.update(entities, dt/10)

	screen.blit(background, (0, 0))
	for entity in entities:
		entity.draw()

	# Event handeler
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			mainloop = False
		elif event.type == pygame.KEYDOWN:
			key_name = pygame.key.name(event.key)
			player.keys[key_name] = True
			if event.key == pygame.K_ESCAPE:
				mainloop = False
		elif event.type == pygame.KEYUP:
			key_name = pygame.key.name(event.key)
			player.keys[key_name] = False

	# Update Pygame display.
	pygame.display.flip()

# Finish Pygame.
pygame.quit()

# At the very last:
print(f"This game was played for {playtime:.2f} seconds")
