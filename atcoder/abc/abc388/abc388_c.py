import bisect

n=int(input())
a=list(map(int,input().split()))

dp = [0]*(n)

for i in range(n-1):
	a1 = a[i+1]
	half = a1 // 2
	half_i = bisect.bisect_right(a,half)
	dp1 = dp[i] + half_i
	dp[i+1] = dp1

ans = dp[-1]
print(ans)