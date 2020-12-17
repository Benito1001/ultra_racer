from vector2 import Vec2d

w = 3.2
h = 1
mass = 5

mid = Vec2d(w/2, h/2)

vertices = [
	Vec2d(0, 0),
	Vec2d(w, 0),
	Vec2d(w, h),
	Vec2d(0, h),
	Vec2d(0, 0)
]

qmoofin = mass*(w**2 + h**2)/12

print("square moof:", qmoofin)


def get_moofin(vertices, mass):
	# vertices must be a list with vertices[-1] == vertices[0]
	n = len(vertices) - 1

	moofin = 0
	total_area = 0
	for i in range(0, n):
		area = abs(vertices[i+1].cross(vertices[i]))

		mid_corector = 3*mid.dot(mid - vertices[i] - vertices[i+1])
		submoof = vertices[i].get_length_sqrd() + vertices[i].dot(vertices[i+1]) + vertices[i+1].get_length_sqrd()

		moofin += area*(mid_corector + submoof)
		total_area += area

	return mass*(moofin/total_area)/6

vmoofin = get_moofin(vertices, mass)

print(f"{'poly moof':12}", vmoofin)
