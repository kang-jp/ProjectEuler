from mylib.prime import primeList
pl=primeList(1000+2*10**6)
print(sum(p for p in pl if p<=2*10**6))
