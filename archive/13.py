import csv
# from pprint import pprint

inp=[]
with open('13.csv') as f:
    reader = csv.reader(f)
    for row in reader:
      inp+=row

ans=0
MOD=10**10
for s in inp:
    ans+=int(s)
ans=str(ans)
print(ans[:10])
