#left rotation
l=list(eval(input()))
k=int(input())
res1=l[k:]+l[:k]
print(res1)   
#right rotation
res2=l[:k]+l[k:]
print(res2)   