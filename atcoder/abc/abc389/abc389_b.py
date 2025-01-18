x=int(input())
ans=0
p = 1
while p != x:
	ans += 1
	p *= ans
print(ans)
