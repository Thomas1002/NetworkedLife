
import sys
from plotter import *

class Program:
  def run(self, channelGains, power, noise, gamma):
    calc = ca.Calc(channelGains, noise, gamma)
    result = calc.result(power, 10)
    plotter = Plotter()
    plotter.plot(result[0], 'mW', 0, 2)
    plotter.plot(result[1], 'SIR', 0.5, 3)
