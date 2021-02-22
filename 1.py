def multiples(numlist,base):
    """
    N = len(numlist)
    K = len(base)
    O(NK)
    """
    ret=[]
    for num in numlist:
        flag=False
        for b in base:
            if num%b==0:
                flag=True
        if flag:
            ret.append(num)
    return ret

print(sum(multiples(range(1,1000),[3,5])))
            
    
