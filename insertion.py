a=[1,8,4,6,2]
for i in range(0,4):
    min=a[i]
    pos=i
    for j in range(i+1,5):
        if(min<a[j]):
            min=a[j]
            pos=j
    if pos!=i:
        temp=a[pos]
        a[pos]=a[i]
        a[i]=temp
print(a)