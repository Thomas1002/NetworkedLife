'''
Created on 13 Mar 2013

@author: thomas
'''
import numpy as np

if __name__ == '__main__':
  a = np.matrix([[1,0,0,0,0,1,0,0,0],
                 [0,0,1,0,0,1,0,0,0],
                 [0,0,0,1,0,1,0,0,0],
                 [0,0,0,0,1,1,0,0,0],
                 [0,1,0,0,0,0,1,0,0],
                 [0,0,1,0,0,0,1,0,0],
                 [0,0,0,1,0,0,1,0,0],
                 [0,0,0,0,1,0,1,0,0],
                 [1,0,0,0,0,0,0,1,0],
                 [0,1,0,0,0,0,0,1,0],
                 [0,0,1,0,0,0,0,1,0],
                 [0,0,0,0,1,0,0,1,0],
                 [1,0,0,0,0,0,0,0,1],
                 [0,1,0,0,0,0,0,0,1],
                 [0,0,1,0,0,0,0,0,1],
                 [0,0,0,1,0,0,0,0,1],
                 ])
  r = 3.125
  c = np.array([5-r,4-r,3-r,1-r, 
                1-r,1-r,4-r,5-r,
                5-r,1-r,2-r,3-r,
                4-r,4-r,4-r,3-r ])
  R = np.array([[5,-1,5,4],
                 [-1,1,1,4],
                 [4,1,2,4],
                 [3,4,-1,3],
                 [1,5,3,-1]])
  compute(a,c,r,R)
  