'''
Created on 13 Mar 2013

@author: thomas
'''

import math as m

if __name__ == '__main__':
  p = 0.75
  n = 2
  correct = (p*(p+1))/2 * ((1-m.pow((p*(1-p)), n))) / (1-p*(1-p))
  incorrect = ((1-p) * (2-p) * (1-m.pow(p-p*p, n))) / (2*(1-p+p*p))
  print (p*(p+1)*(1-m.pow(p-p*p, n))) / (2*(1-p+p*p))
  print ((1-p) * (2-p)) / 2
  print p*(1+p)/2
  print p*(1-p)
  print m.pow(p*(1-p), n)
  print '%f, %f' % (correct, incorrect)