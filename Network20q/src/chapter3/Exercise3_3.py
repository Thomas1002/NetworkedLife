'''
Created on 15 Feb 2013

@author: thomas
'''

import numpy as np

def g(h, theta):
  l = len(h)
  g = theta * h + (1 - theta) * 1.0 / len(h) * np.resize(1, (l,l))
  return g

def iterativ(g, pi):  
  return np.array(pi * np.mat(g))[0]

def compute(matrix, pi, theta):
  G = g(matrix, theta)
  np.set_printoptions(precision=4) 
  
  c = 0
  index = 1
  while c == 0:
    '''print 'Index %d' % (index)'''
    index = index + 1
    local = iterativ(G, pi)
    if compare(local, pi) == 1:
      c = 1
    else:
      pi = local
    '''print local'''
  print pi

def main():
  thd = float(1.0/3.0)
  m = np.array([[0.0, 1.0, 0.0, 0.0, 0.0],
                [1.0, 0.0, 0.0, 0.0, 0.0],
                [thd, 0.0, thd, 0.0, thd],
                [0.0, 0.0, 0.5, 0.0, 0.5],
                [0.0, 0.0, 0.0, 0.0, 0.0]])
  w = np.matrix([[0,0,0,0,1]])
  o = np.matrix([[1,1,1,1,1]])
  hat = 1.0 / len(m) * np.multiply(w.T, o)
  h = m + hat
  print h
  pi = [0.2, 0.2, 0.2, 0.2, 0.2]
  theta = [0.1, 0.3, 0.5, 0.85]
  for i in theta:
    print 'Result for theta = %f' % (i)
    compute(h, pi, i)
  print 'We can see that as theta grows node 1 & 2 becomes the nodes with the largest in degree'
  print 'The ranked order: 1,2,3,5,4'
def main2():
  thd = float(1.0/3.0)
  m = np.array([[0.0, 0.5, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0], 
                [0.5, 0.0, 0.0, 0.0, 0.5, 0.0, 0.0, 0.0],
                [0.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5],
                [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                [0.0, 0.0, 0.0, 0.5, 0.0, 0.0, 0.0, 0.5],
                [0.0, 0.0, 0.0, 0.5, 0.5, 0.0, 0.0, 0.0],
                [0.0, 0.0, 0.0, 0.5, 0.0, 0.5, 0.0, 0.0],
                [thd, 0.0, 0.0, thd, 0.0, 0.0, thd, 0.0]]) 
  '''G = g(m, 0.85)
  np.set_printoptions(precision=4)''' 
  
  s = float(1.0/8.0)
  st = [s, s, s, s, s, s, s, s]
  
  compute(m, st, 0.85)
  
'''  c = 0
  index = 1
  while c == 0:
    print 'Index %d' % (index)
    index = index + 1
    local = iterativ(G, st)
    if compare(local, st) == 1:
      c = 1
    else:
      st = local
    print local
'''  
def compare(a,b):
  for index in range(0, len(b)):
    if round(a[index], 4) != round(b[index], 4):
      return 0
  return 1
  
if __name__ == '__main__':
    main()