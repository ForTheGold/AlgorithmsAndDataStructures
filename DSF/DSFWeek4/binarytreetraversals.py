# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  def inOrder(self):
    result = []
    stack = []
    current = 0
    while True:
        if current != -1:
            stack.append(current)
            current = self.left[current]
        elif stack:
            current = stack.pop()
            result.append(self.key[current])
            current = self.right[current]
        else:
            break  
    return result

  def preOrder(self):
    result = []
    stack = []
    current = 0
    while True:
        if current != -1:
            stack.append(current)
            result.append(self.key[current])
            current = self.left[current]
        elif stack:
            current = stack.pop()
            current = self.right[current]
        else:
            break  
    return result
                

  def postOrder(self):
    result = []
    stack = []
    current = 0
    while True:
        if current != -1:
            stack.append(current)
            result.insert(0, self.key[current])
            current = self.right[current]
        elif stack:
            current = stack.pop()
            
            current = self.left[current]
        else:
            break  
    return result

def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
