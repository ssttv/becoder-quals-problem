m=[]
s=[]
for i in range(int(input())):
    l=input().split()
    k=len(l)
    s.append(l[0])
    for i in range(2,k):
        m.append(l[i])
m=set(m)
p=len(s)
for j in range(p):
    if s[j] in m:
        m.pop()
print(len(m))