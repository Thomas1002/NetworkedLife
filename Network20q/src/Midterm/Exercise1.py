'''
Created on 9 Feb 2013

@author: thomas
'''
import program as pr

if __name__ == '__main__':
  channelGains = [[1, 0.2, 0.1], [0.2, 1, 0.2], [0.2, 0.3, 1]]
  power = [1.0, 1.0, 1.0]
  noise = [0.1, 0.2, 0.1]
  gamma = [2.0, 2.0, 2.5]
  pr.Program().run(channelGains, power, noise, gamma)