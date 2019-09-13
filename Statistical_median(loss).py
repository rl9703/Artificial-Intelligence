'''
    Author:Rishab Lalwani
    Title: Q2 -(18.15) 7-nearest-neighbors regression
'''

import math
import sys

import numpy as np


def loss(neighbours):
    '''
    :param neighbours: Input list of neighbours
    :return: statistical median of the neighbour list along with the loss
    '''

    N=np.array(neighbours)
    Y=np.median(N)
    sum=0
    for each in neighbours:
        sum+=abs(each-Y)
    return Y,sum

def loss2(neighbours):
    '''
    :param neighbours: Input list of neighbours
    :return: Statistical mean of the neighbour list along with the loss
    '''

    M = np.array(neighbours)
    y = np.mean(M)
    total=0
    for each in M:
        total+= math.pow((each - y), 2)
    return y,total


def main():

    neighbours=[]
    i=1
    if len(sys.argv)<2:
        neighbours=[7,6,8,4,7,11,100]
    else:
        while i<len(sys.argv):
            neighbours.append(int(sys.argv[i]))
            i+=1
    y1,t1=loss(neighbours)
    print('The minimized value for L1 is',t1,'with y1 as the median of the neighbours of value',y1 )
    y2, t2 = loss2(neighbours)
    print('The minimized value for L2 is',t2,'with y2 as the mean of the neighbours of value',y2 )

if __name__ == '__main__':
    main()