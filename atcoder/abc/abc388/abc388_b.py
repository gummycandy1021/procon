n,d=map(int,input().split())
ans = [[] for _ in range(d+1)]
for i in range(n):
	t,l=map(int,input().split())
	for k in range(1,d+1):
		ans[k].append(t*(l+k))

for k in range(1,d+1):
	m = max(ans[k])
	print(m)
