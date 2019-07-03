ax=input().split()
a=ax[0]
b=[]
d=[]
k=int(ax[1])
if k==1:
    print(*a,sep=' ')
else:
    for i in range((len(ax[0])-k)+1):
        c=i
        b=[]
        for j in range(k):
            b.append(a[c])
            c=c+1
        d.append(b)
    for i in d:
        print(*i,sep='',end=' ')
