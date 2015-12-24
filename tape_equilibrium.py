# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7
    if len(A)<2:
        return -1
    c=[]
    d=[]
    index=0
    counter=0
    while index<len(A):
        c.append(counter)
        counter+=A[index]
        index+=1
    index=len(A)-1
    counter=0
    while index>=0:
        counter+=A[index]
        d.append(counter)
        index-=1
    temp=[]
    while d!=[]:
        temp.append(d.pop())
    d=temp
    delta=[]
    index=1
    while index<len(c):
        delta.append(abs(c[index]-d[index]))
        index+=1
    #print(c,d,delta)
    return min(delta)