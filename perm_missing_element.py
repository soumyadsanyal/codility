# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7
    thesum=sum(A)
    n=len(A)
    themax=(n+1)*(n+2)/2
    return themax-thesum