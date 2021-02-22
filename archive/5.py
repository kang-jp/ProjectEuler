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

def f(n,d):
    ret=0
    while n%d==0:
        ret+=1
        n=n//d
        if n==0: break
    return ret

cnt=dict(zip(primeList(20),[0 for _ in range(20)]))
primes=cnt.keys()
for k in range(2,20):
    for p in primes:
        cnt[p]=max(f(k,p),cnt[p])

ans=1
for p in primes:
    ans*=p**cnt[p]
print(ans)
