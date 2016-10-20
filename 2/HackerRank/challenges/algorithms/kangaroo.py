#!/bin/python

import sys
class  Kang(object):

  def __init__(self):
    self.slowKangLoc = int()
    self.slowKangVel = int()
    self.fastKangLoc = int()
    self.fastKangVel = int()

  def magic(self):
    if self.slowKangVel == self.fastKangVel:
      return "NO"
    while self.slowKangLoc > self.fastKangLoc and self.slowKangLoc != self.fastKangLoc:
      self.slowKangLoc += self.slowKangVel
      self.fastKangLoc += self.fastKangVel

    if self.slowKangLoc == self.fastKangLoc:
      return "YES"
    else:
      return "NO"
