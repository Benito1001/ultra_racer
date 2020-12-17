from vector2 import Vec2d

class Polygon:
	def __init__(self, vertices):
		self.vertices = vertices
		if self.vertices[0].x != self.vertices[-1].x or self.vertices[0].y != self.vertices[-1].y:
			self.vertices.append(Vec2d(self.vertices[0].x, self.vertices[0].y))

		self.mid = self.get_mid()
		self.vertices = [vertex - self.mid for vertex in self.vertices]
		self.edges = self.get_edges()
		self.normals = self.get_normals()

	def get_mid(self):
		return sum(self.vertices[:-1])/(len(self.vertices) - 1)

	def get_edges(self):
		edges = []
		for i in range(len(self.vertices) - 1):
			edges.append([self.vertices[i], self.vertices[i+1]])
		return edges

	def get_normals(self):
		normals = []
		for edge in self.edges:
			edge_vector = edge[1] - edge[0]
			new_normal = Vec2d(-edge_vector.y, edge_vector.x)/edge_vector.length
			for normal in normals:
				if abs(new_normal.dot(normal)) == 1:
					break
			else:
				normals.append(new_normal)
		return normals

class Square(Polygon):
	def __init__(self, x, y, w, h):
		self.w = w
		self.h = h
		self.pos = Vec2d(x, y)
		Polygon.__init__(self, self.get_vertices())

	def get_vertices(self):
		vertices = [
			Vec2d(self.pos.x, self.pos.y),
			Vec2d(self.pos.x + self.w, self.pos.y),
			Vec2d(self.pos.x + self.w, self.pos.y + self.h),
			Vec2d(self.pos.x, self.pos.y + self.h)
		]
		return vertices


def get_collion_depth(poly1, poly2, n):
	between_vec = poly1.mid - poly2.mid
	between = between_vec.dot(n)
	if between_vec.dot(n) < 0:
		between *= -1
		left_poly = poly2
		right_poly = poly1
	else:
		left_poly = poly1
		right_poly = poly2

	max_l2n = max([vertex.dot(n) for vertex in left_poly.vertices[:-1]])
	min_l2n = min([vertex.dot(n) for vertex in right_poly.vertices[:-1]])

	return (between - max_l2n + min_l2n)*-1

def is_colliding(poly1, poly2):
	# get list og uniqe normals
	normals = poly1.normals + poly2.normals
	for n1 in poly1.normals:
		for n2 in poly1.normals:
			if abs(n1.dot(n2)) == 1:
				normals.remove(n1)

	collision_depths = []
	for n in normals:
		collision_depth = get_collion_depth(poly1, poly2, n)
		if collision_depth < 0:
			return False
		else:
			collision_depths.append(collision_depth)
	return collision_depths

sq1 = Square(0, 3.2, 1, 1)
sq2 = Square(0.12, 4, 1, 1)

print(is_colliding(sq1, sq2))

# Hvordan håndtere dumme programerere?
