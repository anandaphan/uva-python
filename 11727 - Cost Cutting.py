""" Last Accepted 2021.10.06 12:57:02 by Ananda Phan"""

n = int(input())
for i in range(n):
    num = list(map(int,input().split()))
    num.remove(max(num))
    num.remove(min(num))
    print("Case ",i+1,": ",num[0],sep="")
