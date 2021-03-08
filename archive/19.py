import datetime
end=datetime.date(2000,12,31)+datetime.timedelta(1)
tmp=datetime.date(1901,1,1)
ans=0
while end!=tmp:
    if tmp.weekday()==6 and tmp.day==1:
        ans+=1
    tmp+=datetime.timedelta(1)
print(ans)
