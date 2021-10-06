""" Last Accepted 2021.10.06 08:59:44 by Ananda Phan"""

t=int(input())
for i in range(t):
    n = int(input())
    result = str(int(((n*567/9 + 7492)*235/47)-498))
    
    print(int(result[-2]))
