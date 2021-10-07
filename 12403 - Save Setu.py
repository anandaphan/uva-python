""" Last Accepted 2021.10.07 09:16:37 by Ananda Phan"""
	
n = int(input())
balance = 0
for i in range(n):
    operation = input().split()
    if(len(operation)==1): print(balance)
    else:        
        balance += int(operation[1])
    
