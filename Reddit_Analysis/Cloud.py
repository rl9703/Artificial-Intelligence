'''
    Author: Rishab Lalwani
    Title: Word Clouds for titles of subreddits using matplotlib
'''

import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

#Import json files using pandas
df1 = pd.read_json('subreddit1.json', orient='split')
df2 = pd.read_json('subreddit2.json', orient='split')
df3 = pd.read_json('subreddit3.json', orient='split')


def plott(wc):
    '''
    :param wc: Word Cloud variable to be plotted
    :return: Word cloud generated
    '''
    plt.imshow(wc, interpolation = 'bilinear')
    plt.axis('off')
    plt.tight_layout(pad=0)
    plt.show()

# Plotting the clouds using matplotlib
plott(WordCloud().generate(str(df1.title.values)))
plott(WordCloud().generate(str(df2.title.values)))
plott(WordCloud().generate(str(df3.title.values)))
