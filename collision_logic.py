from vector2 import Vec2d

def collides(ent1, ent2):
	if ent1.shape == "circle":
		between_vec = ent2.hitbox.mid - ent1.hitbox.mid
		between_angle = between_vec.angle
		if ent2.shape == "circle":
			print("Nice")
		elif ent2.shape == "square":
			collision_vec = ent2.get_corner(between_angle) - ent1.hitbox.mid
			collision_depth = collision_vec.length - ent1.r
			if collision_depth < 0:
				print(f"\r{between_vec.length}, {collision_vec.length}", end="")
				collision_vec.length = 1
				collision_vec *= -1
				return True, abs(collision_depth), collision_vec
	return False, None, None
