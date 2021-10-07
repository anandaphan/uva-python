""" Last Accepted 2021.10.07 09:24:11 by Ananda Phan"""

n = int(input())
for i in range(n):
    line= input()
    if (line =="1" or line == "4" or line == "78"):
        print("+")
    elif(line[-2]=="3" and line[-1]=="5"):
        print("-")
    elif(line[0]=="9" and line[-1]=="4"):
        print("*")
    else:
        print("?")
    
