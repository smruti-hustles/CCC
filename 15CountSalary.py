#calculating the salary
for _ in range(int(input())):
    x,y=map(int,input().split())
    s=input().strip()
    c=s.count('1')
    current=0
    max=0  
    for i in s:
        if i=='1':
            current+=1
            if current>max:
                max=current
        elif i=='0':
            current=0
    result=(c*x)+(max*y)
    print(result)

'''
Input Format
The first line contains an integer 
𝑇
T denoting the number of test cases. The 
𝑇
T test cases then follow.
The first line of each test case contains 
𝑋
X and 
𝑌
Y.
Second line contains a binary string (i.e it contains only ‘0’ / ‘1’), where '0' denotes that Chef was on leave and '1' denotes Chef was working on that day.
Output Format
For each testcase, output in a single line answer to the problem. i.e The salary received by Chef (including the bonus).

Input            output
3                   2
3                   2
1 2 3               3
4
2 2 3 1
4
3 1 2 4

'''   
