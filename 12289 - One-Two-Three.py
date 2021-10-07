""" Last Accepted 2021.10.07 08:56:35 by Ananda Phan"""


n = int(input())
for i in range(n):
    line = input()
    if(len(line)==5):print(3)
    else:
        if ((line[0]=="o" and line[1]=="n") or (line[0]=="o" and line[2]=="e") or (line[1]=="n" and line[2]=="e")):
            print(1)
        else:
            print(2)
