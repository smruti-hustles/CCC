'''
#multiplication of 2 numbers
a=20
b=12
print(a*b)
# but it takes lots of time 
# So it's better to use Bitwise operator to reduce the time complexity
a       b
20      12 even         0
40      6  even         0+0
80      3  odd, so now  0+0+80
160     1  odd, so now again 0+0+80+160=240
 therefore, 20*12=240
'''
a=12
b=20
prod=0
while(b!=0):#when b==0 condition fails so while(b) or we can write while(b!=0)
    if(b&1==1):
        prod+=a
    a=a<<1
    b=b>>1
print(prod)  
