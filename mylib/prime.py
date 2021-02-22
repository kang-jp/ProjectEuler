def primeList(su):
    """N=su, O(NlogN)"""

    ret=[True for _ in range(su+1)]
    ret[0]=ret[1]=False
    k=2
    while k<=su:
        if ret[k]:
            for i in range(k*2,su+1,k):
                ret[i]=False
        k+=1
    return [i for i,b in enumerate(ret) if b]