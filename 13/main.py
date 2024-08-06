f=open("input.txt").read().split()
n=f[0]
m=f[1]
cow=0
bull=0
for i in range(4):
    if n[i]==m[i]:
        cow+=1
    for j in range(4):
        if n[i]==m[j] and i!=j:
            bull+=1
print(cow, bull)
