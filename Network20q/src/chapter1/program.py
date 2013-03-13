import calc as ca
import plotter as p

class Program:
  def run(self, channelGains, power, noise, gamma):
    calc = ca.Calc(channelGains, noise, gamma)
    result = calc.result(power, 30)
    print result[0][-1]
    plotter = p.Plotter()
    #plotter.plot(result[0], 'mW', 0, 2)
    #plotter.plot(result[1], 'SIR', 0.5, 3)
