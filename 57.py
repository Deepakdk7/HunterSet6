ax=int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
    if i not in b:
        b.append(i)
for i in b:
    if a.count(i)==1:
        print(i)
