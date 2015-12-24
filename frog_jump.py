# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(X, Y, D):
    # write your code in Python 2.7
    if Y<X:
        return 0
    difference=Y-X
    extra=1-int(difference%D==0)
    hops=difference//D
    return hops+extra