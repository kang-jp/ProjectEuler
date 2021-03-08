N=10**6
INF=float('inf')
cnt=[INF for _ in range(N+1)]
cnt[0]=0
cnt[1]=1

def collatz(num,chain=1):
    if num==1:
        return chain
    else:
        if num%2==0:
            return collatz(num//2,chain=chain+1)
        else:
            return collatz(3*num+1,chain=chain+1)

for i in range(1,N+1):
    if cnt[i]!=INF:
        cnt[2*i]=cnt[i]+1
        continue
    cnt[i]=collatz(i)

