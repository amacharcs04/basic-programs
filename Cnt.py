a=[1,[1,2],[1,2]]

#print a 

def getLstCnt(lst):
    cnt=0
    for e in lst:
        if type(e) == list:
            cnt+=getLstCnt(e)
        else:
            cnt+=1
    return cnt

cnt=getLstCnt(a)
print ("cnt is :",cnt)
