def removeConsecutiveCharacter(S):
        # code here
        res=S[0]
        for i in range(1,len(S)):
            if S[i]!=S[i-1]:
                res+=(S[i])
        return res 
S=input()
print(removeConsecutiveCharacter(S)) 
  