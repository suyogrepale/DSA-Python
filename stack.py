s="{(([])[])[]}"

def isBalanced(s):
    arr=list(s)
    key={"]":"[",")":"(","}":"{"}
    temp=[]
    for i in arr:
        if ( i in key and key[i]==temp[-1]):
            temp.pop()
            continue
        temp.append(i)
    if(len(temp)):
        return "NO"
    else:
        return "YES"        


  
print(isBalanced(s))