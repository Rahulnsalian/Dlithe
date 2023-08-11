l=[2,4,5,6,7,8,9,1,3]
sum=6
for i in l:
    key=sum-i
    if key in l:
        print(key,i)
        l.remove(key)
        l.remove(i)