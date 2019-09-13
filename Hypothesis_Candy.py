'''

    Author: Rishab Lalwani
    Title: Q1 Generate a data set of length 100 and
    plot the cor- responding graphs for P(hi|d1,...,dN) and P(DN+1=lime|d1,...,dN)

'''

import random as rand
import matplotlib.pyplot as plt

def P(x):
    '''
    :param x: Hypothesis of candy bags
    :return: Graph plot of all hypothesis
    '''
    post = [0.1, 0.2, 0.4, 0.2, 0.1]
    hypothesis1 = []
    hypothesis2 = []
    hypothesis3 = []
    hypothesis4 = []
    hypothesis5 = []
    alpha = 1
    train = []
    for hype in range(10):
        new_list = []
        train.append(alpha)
        for i in range(len(x)):

            cherry = x[i].count('Lime')
            new_list.append((((alpha * cherry) / len(x[i])) * post[i]))
        alpha = 1 / sum(new_list)
        post = new_list

        hypothesis1.append(new_list[0])
        hypothesis2.append(new_list[1])
        hypothesis3.append(new_list[2])
        hypothesis4.append(new_list[3])
        hypothesis5.append(new_list[4])

    number_of_obs=list(range(1,11))

    #Plotting
    plt.plot(number_of_obs, hypothesis1)
    plt.plot(number_of_obs, hypothesis2)
    plt.plot(number_of_obs, hypothesis3)
    plt.plot(number_of_obs, hypothesis4)
    plt.plot(number_of_obs, hypothesis5)
    plt.show()
    pred(x, post)

def pred(x,post):
    '''
    :param x: Hypothesis of candy bags
    :param post: P(h/D) probabilities
    :return: predicted output along with graph plot
    '''
    pred_output= []
    post=[0.1, 0.2, 0.4, 0.2, 0.1]
    for j in range(10):
        list = []
        for i in range(len(x)):
            lime = x[i].count("Lime")
            len_lime=(lime / len(x[i]))
            formula=(len_lime) * post[i]
            list.append(formula)
        pred_output.append(1-sum(list))
        post = list
    print(pred_output)
    plt.plot([1,2,3,4,5,6,7,8,9,10], pred_output)
    plt.show()

def main():
    '''

    :return: Create hypothesis and call probability function
    '''
    h1 = ['Cherry'] * 100
    h2 = ['Cherry'] * 75 + ['Lime'] * 25
    h3 = ['Cherry'] * 50 + ['Lime'] * 50
    h4 = ['Cherry'] * 25 + ['Lime'] * 75
    h5 = ['Lime'] * 100
    rand.shuffle(h2)
    rand.shuffle(h3)
    rand.shuffle(h4)
    hypothesis = [h1,h2,h3,h4,h5]
    P(hypothesis)

if __name__ == '__main__':
    main()