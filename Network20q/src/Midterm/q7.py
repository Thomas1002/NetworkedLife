'''
Created on 13 Mar 2013

@author: thomas
'''

import math as m

if __name__ == '__main__':
  p = 0.75
  n = 4
  correct = (p*(p+1))/2 * ((1-m.pow((p*(1-p)), n))) / (1-p*(1-p))
  print correct