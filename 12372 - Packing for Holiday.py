""" Last Accepted 2021.10.07 09:05:37 by Ananda Phan"""

n = int(input())
for i in range(n):
    size = list(map(int,input().split()))
    if size[0] <= 20 and size[1] <= 20 and size[2]<=20:
        ans = "good"
    else:
        ans = "bad"

    print("Case ",i+1,": ",ans,sep="")
