'''
In this program we are going to check whether toys are in pair or not 
i.e., we are checking that whether the numbers are in even count or not, 
the numbers which are not in even count, we are just outputting them 
'''
l=list(map(int,input().split()))
ans=[]
for i in l:
    if l.count(i)%2!=0:
        ans.append(i)
print(ans)    
'''
input
1 2 3 1 2 4
output
[3, 4]
'''    
