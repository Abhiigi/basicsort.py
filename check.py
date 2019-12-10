def short(ids):                                 #sorting
    for i in range(len(ids)):
        for j in range(i+1,len(ids)):
            if ids[i]>ids[j]:
                temp=ids[i]
                ids[i]=ids[j]
                ids[j]=temp
            else:
                pass
    return ids        

def delete(ids,m):                                  
    ids=short(ids)
    print(ids)
    flag=[]
    f=0
    s=0
    j=0
    x=0
    z=0
    n=ids[0]
    
    for i in range(len(ids)):                           #finding the occurance of same elements 
        s=s+1

        if n==ids[i]:
            f=f+1
        else:
            n=ids[i]
            flag.append(f)
            f=1
   

    for i in flag:                                    #adjistment for last  element to append in list
        x=x+i 
    flag.append(s-x)
    

    print('bef short',flag)                           #sorthig
    flag=short(flag)
    print('aft short',flag)
 

    for i in range(len(flag)):                         #checking 2 one"s and 2 in list
        if flag[i]==2:
            p=len(flag)-1
            return p
        elif flag[i]==1:
            if flag[i]==flag[i+1]:
                p=len(flag)-2
                break
            else:
                p=len(flag)
 
    return p


ids=[1,2,1,2,1,2,3,3,3,4,3,2,1,3,0]                     # user input
p=delete(ids,2)
print('different objects are:')
print(p)
