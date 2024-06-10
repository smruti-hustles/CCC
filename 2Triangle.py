'''
an iscosceles right angled triangle with base 'b' is given.
we need to find out total how many squares can fit in this triangle(side of square is k)

eg..
triangle base=6
square side=2
no. of triangles==>3
'''
base=int(input())
side=int(input())
a=base/side
b=a-1
answer=b*(b+1)/2
print(answer)