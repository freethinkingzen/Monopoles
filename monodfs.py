#!/usr/bin/python3

import sys


class Sorter:

  def __init__(self, m, n):
    self.m = m                # Number of monopoles
    self.n = n                # Number of rooms to sort into

    self.rooms = [] #[list() for x in range(n)]
      

  def tripleCheck(self, intSet, integer):
    if integer in intSet:
      return 0
    for i in range(len(intSet)):
      for j in range(i, len(intSet)):
        if i != j:
          if (intSet[i] + intSet[j]) == integer:
            return 0
    return 1


  def recursive(self, sets, integer):
    if(integer > self.m):
      return
    for i in sets:
      if self.tripleCheck(i, integer):
        i.append(integer)
        self.recursive(sets, integer+1)
        if(integer <= self.m):
          i.remove(integer)
        if(integer == self.m):
          self.rooms = [row[:] for row in sets]


    

def main():

  #Return  -1 if too few args
  if len(sys.argv) < 3:
    print("Error: Incorrect Number of Arguments\n")
    return -1

  m = int(sys.argv[1])   # Upper limit of {1 ... m} monopoles
  n = int(sys.argv[2])   # Number of rooms to sort into

  # Screen input for invalid arguments
  if m < 1 or n < 1:
    print("Error: Monopoles and rooms must be greater than zero\n")
    return -1
  if m < n:
    print("Error: Number of monopoles must be greater than or equal to number of rooms to sort into\n")
    return -1
  if m == n:
    print("Trivial Solution: One monopole in each room\n")
    return 0
  
  sorter = Sorter(m,n)
  temp = [list() for x in range(n)]
  temp[0].append(1)
  sorter.recursive(temp,2)
  if not sorter.rooms:
    print("Unsat")
  else:
    for i in range(len(sorter.rooms)):
      print("Room", i,":", sorter.rooms[i])

if __name__ == "__main__":
  main()
