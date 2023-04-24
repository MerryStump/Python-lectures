s = [i for i in range(1, 11)]
for i in range(10):
    a=(i+1)%2
    if a==0:
        s[i]='$'
print(s)