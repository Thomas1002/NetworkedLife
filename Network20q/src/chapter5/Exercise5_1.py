'''
Created on 22 Feb 2013

@author: thomas
'''
import numpy as np

def midterm():
  n = np.array([5, 15, 15, 10, 5])
  r = np.array([4.8, 4.5, 4.3, 3.6, 3.5])
  nr = n * r
  NR = nr.sum()
  N = n.sum()
  
  r1 = (NR + nr[0]) / (N + n[0])
  r2 = (NR + nr[1]) / (N + n[1])
  r3 = (NR + nr[2]) / (N + n[2])
  r4 = (NR + nr[3]) / (N + n[3])
  r5 = (NR + nr[4]) / (N + n[4])
  
  print "%f, %f, %f, %f, %f" % (r1, r2, r3, r4, r5)
  #r1 = (NR+3*5) / (N + 3)
  #r2 = (NR+10*4.35) / (N+10)
  print 'Bayesian ranking.'
  print 'Canon %d %.2f %.2f' % (3, 5, r1)

def main():
  NR = 3 * 5 + 10 * 4.35
  N = 13
  r1 = (NR+3*5) / (N + 3)
  r2 = (NR+10*4.35) / (N+10)
  print 'Bayesian ranking.'
  print 'Canon %d %.2f %.2f' % (3, 5, r1)
  print 'HP    %d %.2f %.2f' % (10, 4.35, r2)

if __name__ == '__main__':
  midterm()
  print 'main'
  main()