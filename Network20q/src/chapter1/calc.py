'''
Created on 9 Feb 2013

@author: thomas
'''

class Calc:
  def __init__(self, channelGains, noise, gamma):
    self.channelGains = channelGains
    self.gamma = gamma
    self.noise = noise
  
  def calculateSIR(self, i, power):
    d = 0
    channelGain = self.channelGains[i]
    for index in range(0, len(channelGain)):
      if (index != i):
        result =  channelGain[index] * power[index]
        d = d + result
    value = power[i] / (d + self.noise[i])
    #print '%f %f' % (i, self.noise[i])
    return value
  
  def calculatePowerLevel(self, power):
    result = [[], []]
    for i in range(0, len(self.channelGains)):
      sir = self.calculateSIR(i, power)
      p = self.gamma[i] / sir * power[i]
      
      result[0].append(sir)
      result[1].append(p)
    return result
  
  def result(self, power, iterations):
    sir = []
    p = [power]
    for i in range(0, iterations):
      result = self.calculatePowerLevel(power)
      power = result[1]
      sir.append(result[0])
      p.append(result[1])
    '''print 'sir %s' % (sir)'
    'print 'p %s' % (p)'''
    return [p,sir]