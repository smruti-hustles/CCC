'''
A number is said to be a narcissistic number, 
if the addition value of each digit raised to 
the power of numbers of digits available in the original number is equal to the original number.

Instance-1

Input number is 153.

Let’s check it by using the logic of Narcissistic number.

Number of digits available in 153 is 3.

Calculate the power values and add those = (1^3) + (5^3) + (3^3) = 1 + 125 + 27 = 153

As we notice here both the calculated number and original number are same.

Hence, 153 is a narcissistic number.
'''

n=int(input())
t=n
l=len(str(n))
sum=0
while(n!=0):
    r=n%10
    sum+=pow(r,l)
    n=n//10
if t==sum:
    print("Narcissistic Number ")    
else:
    print("Not")    