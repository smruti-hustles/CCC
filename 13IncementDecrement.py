'''
x, y two numbers 
k another number 
we can add k to x any number of times and similarly 
can subtract k from y any number of times
while we rae doing it we need to see if at any point we are 
getting same value or not. 

Example:
x=2   y=12
k=2

2+2=4   12-2=10
4+2=6   10-2=8
6+2=6   8+2=6
 

As we can see at this point both are same so True

'''
x,y=map(int,input().split())
k=int(input())
a=(x-y)
if a%2==0:
    print("True")
else:
    print("False")    