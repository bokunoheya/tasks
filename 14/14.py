f=open("input.txt").read().split()
n=int(f[0])
m=int(f[1])
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
print(int(n*m/gcd(n,m)))