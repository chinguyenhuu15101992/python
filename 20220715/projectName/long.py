class CuocGoi:    
    def __init__(self,timestamp,imsi,action_type, callinggt,laccell,action_code,mcc_mnc ):
        self.timestamp=timestamp.strip()
        self.imsi=imsi.strip()
        self.action_type=action_type.strip()
        self.callinggt=callinggt.strip()
        self.laccell=laccell.strip()
        self.action_code=action_code.strip()
        self.mcc_mnc=mcc_mnc.strip()
        callinggt = callinggt.strip()
        if callinggt.startswith('855'):
            self.country='CAM'
        elif callinggt.startswith('856'):
            self.country='LAO'
        elif callinggt.startswith('86'):
            self.country='CN'
        else:
            self.country='None'
    def print(self):
        print(self.timestamp,self.imsi,self.action_type,\
            self.callinggt,self.laccell,self.action_code,\
            self.mcc_mnc,self.country)
def getdata():

    ls =[]
    first=1
    with open('log_test.csv') as f:
        for line in f:
            #print(line)
            if first==1:
                first = 0
                print ('Skip')
                continue
            a = line.split(',')
            #print(a)
            ls.append(CuocGoi(a[0], a[1], a[2], a[3], a[4], a[5], a[6]))
    return ls


# #s ='{'
# print(ls)
# stats ={}
# for l in ls:
#     key = str((l.country, l.action_code))
#     #print(key)
#     if stats.get(key)==None:
#         stats[key] = 1
#     else:
#         stats[key] += 1
# stats = sorted(stats.items())
# for st in stats:
#     print(st)
# #count = sum((p.country == "CAM" and p.action_code.find("RJ_01")!=-1) for p in ls)
# #print(count)