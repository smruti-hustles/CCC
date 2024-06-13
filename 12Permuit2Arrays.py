def isPossible(a, b, n, k):
    # Your code goes here
        a.sort(reverse=True)
        b.sort()
        f=1
        for i in range(n):
            if a[i]+b[i]<k:
                f=0
                break
        if f==1:
            return True
        else:
            return False
n=int(input())  #length of lists/arrays       
a=list(eval(input()))   
b=list(eval(input()))   
k=int(input())  #k value  
print(isPossible(a,b,n,k)) 