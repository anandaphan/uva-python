""" Last Accepted 2021.10.07 09:24:11 by Ananda Phan"""
	
line = input()
i=0
while line != "*":
    if line == "Hajj": ans = "Hajj-e-Akbar"
    else :
        ans = "Hajj-e-Asghar"
    print("Case ",i+1,": ",ans,sep="")
    i+=1
    line = input()
