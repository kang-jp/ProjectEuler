ans=-1
for i in range(1000):
    for j in range(1000):
        n=i*j
        if str(n)==str(n)[::-1]:
            ans=max(n,ans)
print(ans)