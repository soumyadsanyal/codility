# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(X, A):
    # write your code in Python 2.7
    positions={}
    index=0
    while index<len(A):
        if A[index] not in positions:
            positions[A[index]]=1
        if len(positions)==X:
            return index
        index+=1
    return -1