n=int(input())
a=list(map(int,input().split()))

a0 = a[0]
a1 = a[1]
r = a1 / a0

ans = True
for i in range(n-1):
	if r*a[i] != a[i+1]:
		ans = False
		break

print('Yes' if ans else 'No')