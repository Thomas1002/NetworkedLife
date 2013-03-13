'''
Created on 13 Mar 2013

@author: thomas
'''

import numpy as np


if __name__ == '__main__':
    np.set_printoptions(precision=4)
    A = np.array([[1,1,1,1,1], [1,1,1,1,1], [1,1,1,0,1], [1,1,0,1,0], [1,1,1,0,1]])
    evals, evecs = np.linalg.eig(A)
    #print evecs
    
    c = np.linalg.eig(A)[1][:,0]
    print c
    '''
    B = np.array([[0,1,1,1,0,0,0,0],
                  [1,0,0,1,1,0,0,0],
                  [1,0,0,0,0,1,1,1],
                  [1,1,0,0,1,0,0,0],
                  [0,1,0,1,0,0,0,0],
                  [0,0,1,0,0,0,1,0],
                  [0,0,1,0,0,1,0,1],
                  [0,0,1,0,0,0,1,0]])
    evals, evecs = np.linalg.eig(B)
    y = power_method(evecs, 1, 10)
    print evecs'''