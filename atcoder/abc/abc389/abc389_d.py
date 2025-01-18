import math
r = int(input())
points = []
for x in range(-r+1,r+1):
	y_max = math.floor(0.5+(r**2-(0.5-x)**2)**(0.5))
	y_min = math.floor(0.5-(r**2-(0.5-x)**2)**(0.5))
	y_count = y_max - y_min
	points.append(y_count)

p0 = points[0]
ps = []
for i in range(1,2*r):
	p1 = points[i]
	if p0 < p1:
		p1 = p0
	ps.append(p1-1)
	p0 = points[i]

ans = sum(ps)
print(ans)
