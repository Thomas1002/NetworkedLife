'''
Created on 9 Feb 2013

@author: thomas
'''
import program as pr
import numpy as np
def test():
  channelGains = [[1, 0.1, 0.2, 0.3], 
                  [0.2, 1, 0.1, 0.1], 
                  [0.2, 0.1, 1, 0.1], 
                  [0.1, 0.1, 0.1,1]]
  power = [1.0, 1.0, 1.0, 1.0]
  noise = [0.1, 0.1, 0.1, 0.1]
  gamma = [2.0, 2.5, 1.5, 2.0]
  pr.Program().run(channelGains, power, noise, gamma)

if __name__ == '__main__':
  np.set_printoptions(precision=2)
  test()
  
  
  channelGains = [[1.0, 0.2, 0.1], 
                  [0.2, 1.0, 0.2], 
                  [0.2, 0.3, 1.0]]
  power = [1.0, 1.0, 1.0]
  noise = [0.1, 0.2, 0.1]
  gamma = [2.0, 2.0, 2.5]
  pr.Program().run(channelGains, power, noise, gamma)