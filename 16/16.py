import itertools
f=open("input.txt").read().split()
n=int(f[0])
list=[]
c=0
for j in range(1,n+1):
    list.append(j)
for k in range(2,12):
    for i in itertools.combinations(list,k):
        if sum(i)==n:
            c+=1
print(c+1)
