#!/bin/python

import sys

def magic(kx1,kv1,kx2,kv2):
    while kx1 > kx2 and kx1 != kx2:
        kx1 += kv1
        kx2 += kv2
        

    if kx1 == kx2:
        print "YES"
    else:
        print "NO"

def main():
    x1,v1,x2,v2 = raw_input().strip().split(' ')
    x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]

    if v1 == v2:
        print "NO"
    elif v1 < v2:
        magic(x1,v1,x2,v2)
    else:
        magic(x2,v2,x1,v1)

if __name__ == '__main__':
    main()

