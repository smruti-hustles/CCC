n=input()
d={}
for i in range(len(n)):
    if n[i] in d:
        d[n[i]]+=1
    else:
        d[n[i]]=1
for key,value in d.items():
    print(f"{key},count{value}")            