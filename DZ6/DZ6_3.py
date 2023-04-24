from random import randint
s=[randint(10, 50) for i in range(30)]
s.sort()
n=0
l=29
a=[]
print(s)
while True:
    if s[l]!=s[l-1]:
        a.append(s[l])
        n+=1
        l-=1
        if n==3:
            break
    else:
        l-=1
print(a)