#!/usr/bin/python3

import sys


class Sorter:

  def __init__(self, m, n):
    self.m = m                # Number of monopoles
    self.n = n                # Number of rooms to sort into
    self.rooms = []           # Captures the result as a lazy escape from recursion
      

  # Takes an array of integers and a new integer to add
  # Checks if adding the new integer violates X+Y=Z constraint
  # returns 0 if it should not be added
  # returns 1 if it can be added
  def tripleCheck(self, intSet, integer):
    if integer in intSet:
      return 0
    for i in range(len(intSet)):
      for j in range(i, len(intSet)):
        if i != j:
          if (intSet[i] + intSet[j]) == integer:
            return 0
    return 1

  # Recursively tries to add allowed integers 1-m
  # to 1-m rooms. If a dead end it hit and m ints
  # don't fit into n rooms, the recursion returns
  # and removes the last integer added and attempts
  # to add to the next room.
  def recursive(self, sets, integer):
    if(integer > self.m):
      return
    for i in sets:
      # Check if for X,Y,Z, X+Y=Z. Enter on return 1
      if self.tripleCheck(i, integer):
        i.append(integer) #add new integer
        self.recursive(sets, integer+1) #add to room
        if(integer == self.m):  #capture solution
          self.rooms = [row[:] for row in sets]
        if(integer <= self.m):  #remove if dead end was hit
          i.remove(integer)


    

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
    # Check that all numbers are represened in solution
    test_case = []
    for i in sorter.rooms:
      test_case += i
    test_case.sort()
    if(test_case == [item for item in range(1,m+1)]):
      print("SUCCESS!")
    else:
      print("Invalid Solution Found: Not all monopoles are present")
     
    # Print solution with "Room x: []" format
    for i in range(len(sorter.rooms)):
      print("Room", i,":", sorter.rooms[i])

if __name__ == "__main__":
  main()
