def fibonacciList(f,s,L):
    """
    O(L)
    """
    ret=[f,s]
    for _ in range(L-2):
        ret.append(ret[-1]+ret[-2])
    return ret

def omit(func,li):
    ret=[]
    for ele in li:
        if not func(ele):
            ret.append(ele)
    return ret

def ju(n):
    return not(n%2==0 and n<=4000000)

print(sum(omit(ju,fibonacciList(1,2,100))))
