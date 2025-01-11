from sortedcontainers import SortedSet, SortedList, SortedDict

n=int(input())
a=list(map(int,input().split()))

S = SortedList([])

for i in range(n):
	v2 = i
	ind = S.bisect_left(i)
	v4 = len(S) - ind
	v3 = min(v2,v4)
	a[i] += v3

	v0 = n - i - 1
	v1 = min(a[i],v0)
	a[i] -= v1
	S.add(i+v1)

print(*a)
