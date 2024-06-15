#gives the frequency of each character
from collections import Counter
l=list(eval(input()))
v=Counter(l)
print(v)
d=sorted(v)
for i,j in d.items():
    print(f"{i} : {j}")
print(sorted(v)) #gives unique and sorted ele 

'''
input
[1,2,2,4,3,2,5,5,6]
output
Counter({2: 3, 5: 2, 1: 1, 4: 1, 3: 1, 6: 1})
[1, 2, 3, 4, 5, 6]
'''