f=open("input.txt").read()
c=0
for i in f[1:]:
    if i=="1":
        c+=1
print(int(c/2))
