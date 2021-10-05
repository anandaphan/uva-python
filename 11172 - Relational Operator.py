""" Last Accepted 2021.10.05 10:27:00 by Ananda Phan"""

n=int(input())
for i in range(n):
    num = list(map(int,input().split()))

    if(num[0]>num[1]): print(">")
    elif(num[0]<num[1]): print("<")
    else:
        print("=")
