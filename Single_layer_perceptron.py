'''
    Author:Rishab Lalwani
    Title:Q5 Single layer perceptron that can detect the origin of alligator,
    given the weight and length using backpropogation.
'''

import numpy as np
import sys

def training(input,output):
    '''

    :param input: Array of input weight and lengths as training data
    :param output: list of output cities of training data
    :return: list of Synaptic weights for test data

    '''

    s=np.random.random((2,1))

    x=np.array(input,dtype=np.float64)

    Output = []

    for i in range(len(output)):

        if output[i] == 'T':
            Output.append(1)

        elif output[i] == 'F':
            Output.append(0)

    y=np.array(Output,dtype=np.float64).T
    '''
        Feed forward network using single layer perceptron
    '''
    for i in range(1000):

        z=np.dot(x,s)

        sigmoid = 1/(1+np.exp(-z))

        error = (y-sigmoid)

        sigmoidDerivative = sigmoid * (1-sigmoid)

        s = s + np.dot(x.T, error*sigmoidDerivative)


    return s.T[0]


def activationOutput(testdata,synaptic_weights):

    activation = np.dot(np.array(testdata,dtype=np.float64), synaptic_weights)

    result = 1 / (1 + np.exp(activation))

    return 'T' if result<0.5 else 'F'

def main():

    input = [[11,70],[35,11],[21,45],[60,80],[37,32],[26,64],[44,30],[12,60]]

    output = ['T','F','T','F','F','T','F','T']

    if len(sys.argv)>2:
        testdata = [int(sys.argv[1]),int(sys.argv[2])]

    else:
        # Default Weight and length of alligator
        testdata=[12,70]

    synaptic_weights = training(input,output)

    print('An aligator with weight',testdata[0],'and length',testdata[1],'lives in',end=' ')

    print(activationOutput(testdata,synaptic_weights))

if __name__ == '__main__':
    main()