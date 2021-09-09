#!/usr/bin/python3
import numpy as np
import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

def IsBinarySearchTree(tree):
    temp = -np.inf
    stack = []
    current = 0
    if tree:
      while True:
          if current != -1:
              if tree[current][1] != -1:
                if tree[tree[current][1]][0] >= tree[current][0]:
                  return False
              if tree[current][2] != -1:
                if tree[tree[current][2]][0] < tree[current][0]:
                  return False
              stack.append(current)
              current = tree[current][1]
              if tree[current][1] != -1:
                if tree[tree[current][1]][0] >= tree[current][0]:
                  return False
              if tree[current][2] != -1:
                if tree[tree[current][2]][0] < tree[current][0]:
                  return False
          elif stack:
              if tree[current][1] != -1:
                if tree[tree[current][1]][0] >= tree[current][0]:
                  return False
              if tree[current][2] != -1:
                if tree[tree[current][2]][0] < tree[current][0]:
                  return False
              current = stack.pop()
              if temp > tree[current][0]:
                return False
              else:
                temp = tree[current][0]
              current = tree[current][2]
              if tree[current][1] != -1:
                if tree[tree[current][1]][0] >= tree[current][0]:
                  return False
              if tree[current][2] != -1:
                if tree[tree[current][2]][0] < tree[current][0]:
                  return False
          else:
              break

    return True


def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  if IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
