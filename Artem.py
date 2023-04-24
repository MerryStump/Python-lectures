a=[1,2,2]
l=len(a)
print(l)
for i in range(l):
    del a[l]
    break
print(a)