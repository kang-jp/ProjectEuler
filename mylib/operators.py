def productsum(li):
    ret=1
    for n in li:
        ret*=n
    return ret

def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)