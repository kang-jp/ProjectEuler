import csv

inp=[]
with open('18.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        tmp=row[0].split()
        tmp=list(int(x) for x in tmp)
        inp.append(tmp)

from pprint import pprint
pprint(inp)

def f(h,w,value=0):
    if h==len(inp):
        return value
    else:
        value+=inp[h][w]
        return max(f(h+1,w,value=value),f(h+1,w+1,value=value))
        
print(f(0,0))