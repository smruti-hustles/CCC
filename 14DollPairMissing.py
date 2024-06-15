t=int(input())
for i in range(t):
    n=int(input())
    l=[]
    for t in range(n):
        m=int(input())
        l.append(m)
    for i in l:
        if l.count(i)%2==1:
            print(i)
            break

'''
input   output
1   #no of test case
3   #no of numbers
1   1,1 pair are there but 2 is only one it's pair is missing
2
1

'''        
