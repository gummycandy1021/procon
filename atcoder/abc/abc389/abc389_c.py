q = int(input())
acc = [0]
j = 0
minus = 0
for i in range(q):
	query = list(map(int,input().split()))
	q0 = query[0]
	if q0 == 1:
		l = query[1]
		v = acc[-1] + l
		acc.append(v)
	elif q0 == 2:
		minus = acc[j+1]
		j += 1
	else:
		k = query[1]
		print(acc[k+j-1]-minus)

