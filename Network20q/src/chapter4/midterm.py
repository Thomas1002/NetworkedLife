'''
Created on 13 Mar 2013

@author: thomas
'''

import numpy as np
import Exercise4_1 as ex

if __name__ == '__main__':
  a = np.matrix([[1,0,0,0,0,1,0,0,0],
                 [0,0,1,0,0,1,0,0,0],
                 [0,0,0,1,0,1,0,0,0],
                 [0,0,0,0,1,1,0,0,0], #r_xA
                 [0,1,0,0,0,0,1,0,0],
                 [0,0,1,0,0,0,1,0,0],
                 [0,0,0,1,0,0,1,0,0],
                 [0,0,0,0,1,0,1,0,0], #r_xB
                 [1,0,0,0,0,0,0,1,0],
                 [0,1,0,0,0,0,0,1,0],
                 [0,0,1,0,0,0,0,1,0],
                 [0,0,0,0,1,0,0,1,0], #r_xC
                 [1,0,0,0,0,0,0,0,1],
                 [0,1,0,0,0,0,0,0,1],
                 [0,0,1,0,0,0,0,0,1],
                 [0,0,0,1,0,0,0,0,1],
                 ])
  R = np.array([[5,0,5,4],
                [0,1,1,4],
                [4,1,2,4],
                [3,4,0,3],
                [1,5,3,0]])
  r = 3.125
  c = np.array([5-r,4-r,3-r,1-r, 1-r,1-r,4-r,5-r, 5-r,1-r,2-r,3-r, 4-r,4-r,4-r,3-r])
  
  result = np.linalg.lstsq(a, c, 0.0001)[0]
  np.set_printoptions(precision=4)
  #print result
  r = ex.compute(a,c,r,R)
  print 'R ~'
  print R - r
  #result = np.linalg.lstsq(a, c) 
  #print np.linalg.pinv(a, c)
  #print "resultat"
  #print result
  #compute(a,c,r,R)#