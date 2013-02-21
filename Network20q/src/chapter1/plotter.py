'''
Created on 9 Feb 2013

@author: thomas
'''
from numpy import *
from numpy.linalg import *
import matplotlib.pyplot as plt


class Plotter:

  def plot(self, data, ylabel, ymin, ymax):
    d = array(data).transpose()
    x = range(0, len(d[0]))
    for p in d:
      plt.plot(x, p, lw=p[1])
    plt.ylabel(ylabel)
    plt.xlabel('Iteration')
    plt.axis([0,len(d[0])-0.8,ymin, ymax])
    plt.show()
    
            