h,w=map(int,input().split())
s=[list(input()) for _ in range(h)]

blank = []

b_top = h
b_left = w
b_right = -1

for i in range(h):
	for j in range(w):
		sij = s[i][j]
		if sij == "#":
			if i < b_top:
				b_top = i
			if j < b_left:
				b_left = j
			b_bottom = i
			if j > b_right:
				b_right = j


ans = True

for i in range(b_top,b_bottom+1):
	for j in range(b_left,b_right+1):
		sij = s[i][j]
		if sij == ".":
			ans = False
			break
	if not ans:
		break
print('Yes' if ans else 'No')