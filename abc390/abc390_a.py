a=list(map(int,input().split()))

flag = False
for i in range(4):
	if not flag and a[i] == a[i+1]+1:
		flag = True
	elif flag and a[i] > a[i+1]:
		flag = False
		break
	
print('Yes' if flag else 'No')
