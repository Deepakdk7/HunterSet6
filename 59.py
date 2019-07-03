ax=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[]
for i in range(int(ax)):
               c.append(a[i]+b[i])
print(*c,sep=' ')
