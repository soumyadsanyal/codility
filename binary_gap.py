# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def test(N):
    index=0
    while 2**index<=N:
        index+=1
    return index-1

def solution(N):
    # write your code in Python 2.7
    result=[]
    index=test(N)
    best=0
    while index>=0:
        #result.append(index)
        N-=2**index
        newindex=test(N)
        if newindex<0:
            break
        gap=index-newindex-1
        if gap>best:
            best=gap
        index=newindex
    return best
    #if len(result)<=1:
    #    return 0
    #else:
    #    index=0
    #    m=[]
    #    while index<len(result)-1:
    #        m.append(result[index]-result[index+1]-1)
    #        index+=1
    #    return max(m)
        