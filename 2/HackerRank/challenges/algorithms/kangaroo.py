#!/bin/python

import sys
class  Kang(object):
  def magic(kx1,kv1,kx2,kv2):
    if kv1 == kv2:
      return "NO"
    while kx1 > kx2 and kx1 != kx2:
      kx1 += kv1
      kx2 += kv2

    if kx1 == kx2:
      return "YES"
    else:
      return "NO"

  def main():
    x1,v1,x2,v2 = raw_input().strip().split(' ')
    x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]

    if v1 < v2:
      answer = magic(x1,v1,x2,v2)
    else:
      answer = magic(x2,v2,x1,v1)
    print answer
