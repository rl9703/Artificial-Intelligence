'''
    Author: Rishab Lalwani
    Title: q3-c , slot machine
'''

import random
import sys
from pip._vendor.msgpack.fallback import xrange


def gameplay():
          '''
          :return: Number of plays
          '''
          coins = 10
          plays = 0
          while coins >= 1:
                  coins -=1
                  plays += 1
                  # Randomly arranges the 4 choices in slots
                  # Iterates through the first three
                  slots = [random.choice(
                            ["bar", "bell", "lemon", "cherry"])
                           for i in range(3)]
                  # If first two slots are same
                  if slots[0] == slots[1]:
                      #If all three slots are same
                          if slots[1] == slots[2]:
                              num_equal = 3
                          else:
                              num_equal = 2
                # No slot is same
                  else:
                    num_equal = 1

                  if slots[0] == "cherry":
                        coins = coins + num_equal
                    # If 2nd or 3rd slot contains bar or bell respectively
                  elif num_equal == 3:
                        if slots[0] == "bar":
                            coins += 20
                        elif slots[0] == "bell":
                            coins += 15
                        else:
                            coins += 5
          return plays

def test(trials):
    '''

    :param trials: Number of trials
    :return: prints the number of trials,mean and median
    '''
    scores = [gameplay() for iterate in xrange(trials)]
    mean = sum(scores) // float(trials)
    median = sorted(scores)[trials//2]
    print ("Number of trials:",trials,"\nMean:",mean,"\nMedian:", median)

if __name__ == '__main__':
    test(int(sys.argv[1]))
