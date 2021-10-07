""" Last Accepted 2021.10.07 08:36:29 by Ananda Phan"""


n = int(input())
i = 0
while n!=0:
    treat = list(map(int,input().split()))
    balance = len(treat)-2*treat.count(0)   
    print("Case ",i+1,": ",balance,sep="")
    i+=1
    n=int(input())
    
