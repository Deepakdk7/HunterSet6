ax=input().split()
k=int(ax[1])
n=int(ax[0])
a=list(map(int,input().split()))
c=0
for i in range(n-1):
    for j in range(i,n):
        if abs(a[i]-a[j])==k:
            c=c+1
print(c)
