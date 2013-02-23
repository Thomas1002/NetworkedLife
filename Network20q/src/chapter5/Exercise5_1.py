'''
Created on 22 Feb 2013

@author: thomas
'''


def main():
  NR = 3 * 5 + 10 * 4.35
  N = 13
  r1 = (NR+3*5) / (N + 3)
  r2 = (NR+10*4.35) / (N+10)
  print 'Bayesian ranking.'
  print 'Canon %d %.2f %.2f' % (3, 5, r1)
  print 'HP    %d %.2f %.2f' % (10, 4.35, r2)

if __name__ == '__main__':
    main()