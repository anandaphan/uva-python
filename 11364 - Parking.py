""" Last Accepted 2021.10.05 11:36:03 by Ananda Phan"""

n=int(input())
for i in range(n):
    nStore = int(input())
    num = list(map(int,input().split()))
    a=min(num)
    b=max(num)
          
    print(2*(b-a))
    
