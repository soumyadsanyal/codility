# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7
    result=0
    while A!=[]:
        result=result^(A.pop())
    return result