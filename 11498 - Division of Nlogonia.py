""" Last Accepted 2021.10.05 16:52:06 by Ananda Phan"""

n=int(input())
while(n!=0):
    divPoint = list(map(int,input().split()))
    for i in range(n):
        point = list(map(int,input().split()))
        if(point[0] == divPoint[0] or point[1] == divPoint[1]):
            print("divisa")
        elif(point[0] > divPoint[0] and point[1] > divPoint[1]):
            print("NE")
        elif(point[0] > divPoint[0] and point[1] < divPoint[1]):
            print("SE")
        elif(point[0] < divPoint[0] and point[1] > divPoint[1]):
            print("NO")
        elif(point[0] < divPoint[0] and point[1] < divPoint[1]):
            print("SO")
    n=int(input())
