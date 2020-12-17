from vector2 import Vec2d
from draw_vector import DVec

def collides(ent1, ent2):
	if ent1.shape == "circle":
		if ent2.shape == "circle":
			print("Nice")
		elif ent2.shape == "polygon":
			# collisions = []
			for edge in ent2.edges:
				colliding, collision_point, collision_depth = circle_is_on_line(ent1.pos + ent1.r, ent1.r, *edge)
				if colliding:
					collision_vec = ent1.hitbox.mid - collision_point
					return True, collision_depth, collision_vec, collision_point

	return False, None, None, None

def circle_is_on_line(circle_mid, circle_rad, line_start, line_end):
	collision_point, length_to_line = length_from_point_to_line(circle_mid, line_start, line_end)
	if length_to_line < circle_rad:
		line_min = Vec2d(min(line_start.x, line_end.x), min(line_start.y, line_end.y))
		line_max = Vec2d(max(line_start.x, line_end.x), max(line_start.y, line_end.y))
		if line_start.x != line_end.x:
			if collision_point.x > line_min.x and collision_point.x < line_max.x:
				return True, collision_point, circle_rad-length_to_line
		else:
			if collision_point.y > line_min.y and collision_point.y < line_max.y:
				return True, collision_point, circle_rad-length_to_line
		return circle_is_on_corner(circle_mid, circle_rad, line_start, line_end)
	return False, None, None

def circle_is_on_corner(circle_mid, circle_rad, line_start, line_end):
	line_start_to_circle = (line_start - circle_mid).get_length_sqrd()
	line_end_to_circle = (line_end - circle_mid).get_length_sqrd()
	if line_start_to_circle < line_end_to_circle:
		if line_start_to_circle < circle_rad:
			return True,  line_start, circle_rad-line_start_to_circle
		else:
			return False, None, None
	else:
		if line_end_to_circle < circle_rad:
			return True,  line_end, circle_rad-line_end_to_circle
		else:
			return False, None, None

def length_from_point_to_line(point, line_start, line_end):
	line_point = line_start
	line_vector = line_end-line_start

	t = line_vector.dot(point - line_point)/line_vector.get_length_sqrd()

	collision_point = line_point + line_vector*t
	to_line = (collision_point - point).length

	return collision_point, to_line
