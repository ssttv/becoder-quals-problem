f=[]
s=[]
for i in range(int(input())):
    l=input().split()
    k=len(l)
    s.append(l[0])
    for i in range(2,k):
        f.append(l[i])
f=set(f)
p=len(s)
for j in range(p):
    if s[j] in f:
        f.pop()
print(len(f))
