isDone = False
while True:
    try:
        line=input()
    except EOFError:
        break
    
    txt=""
    for c in line:
        if(c == "\""):
            if (isDone == False):
                txt+="``"
            else:
                txt+="''"
            isDone= not isDone
        else:
            txt+=c
    print(txt)
