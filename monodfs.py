#!/usr/bin/python3

import sys

def main():

  #Return  -1 if too few args
  if(len(sys.argv) < 3):
    print("Incorrect Number of Arguments\n")
    return  -1;

  m = int(sys.argv[1])   # Upper limit of {1 ... m} monopoles
  n = int(sys.argv[2])   # Number of rooms to sort into

  rooms = []             # List of monopole sets for each room
  monopoles = set((range(1, m+1)))    # Set of all monopoles

  print (monopoles)



if __name__ == "__main__":
  main()
