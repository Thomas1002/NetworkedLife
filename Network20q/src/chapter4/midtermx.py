'''
Created on 13 Mar 2013

@author: thomas
'''

import numpy as np
import Exercise4_1 as ex

if __name__ == '__main__':
  a = np.matrix([[1,0,0,0,1,0,0,0,0,0],
                 [0,1,0,0,1,0,0,0,0,0],
                 [0,0,0,1,1,0,0,0,0,0],
                 
                 [1,0,0,0,0,1,0,0,0,0],
                 [0,0,1,0,0,1,0,0,0,0],
                 [0,0,0,1,0,1,0,0,0,0],
                 
                 [1,0,0,0,0,0,1,0,0,0],
                 [0,0,1,0,0,0,1,0,0,0],
                 [0,0,0,1,0,0,1,0,0,0],
                 
                 [1,0,0,0,0,0,0,1,0,0],
                 [0,0,1,0,0,0,0,1,0,0],
                 [0,0,0,1,0,0,0,1,0,0],
                 
                 [1,0,0,0,0,0,0,0,1,0],
                 [0,1,0,0,0,0,0,0,1,0],
                 [0,0,1,0,0,0,0,0,1,0],
                 
                 [0,1,0,0,0,0,0,0,0,1],
                 [0,0,1,0,0,0,0,0,0,1],
                 ])
  R = np.array([[1,9,9,8,3,0],
                [2,0,0,0,4,6],
                [0,2,3,6,3,6],
                [5,6,5,1,0,0]])
  r = 73.0 / 18.0
  print 'r = %f' % (r)
  c = np.array([1-r,2-r,5-r, 9-r,2-r,6-r, 9-r,3-r,5-r, 8-r,6-r,1-r, 3-r,4-r,3-r, 6-r,6-r])
  r = ex.compute(a,c,r,R)
  #result = np.linalg.lstsq(a, c) 
  #print np.linalg.pinv(a, c)
  print "resultat"
  print R - r
  #compute(a,c,r,R)#