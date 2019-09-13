import argparse
import sys
#import pdb
import gym
import time
import random
from gym import wrappers, logger

class Agent(object):
 
    """The world's simplest agent!"""
    def __init__(self, action_space):
        self.action_space = action_space

    # You should modify this function
    def act(self, observation, reward, done):
        mycoordinates=[]
        wallcoordinates=[]
        enemycoordinates=[]
        collide=[]
        items=[]
        flag=False
        c=0
        d=0
        j=0
        for i in observation:
            c+=1
            d=0
            for z in i:
                d+=1
                if 0 not in z:
                        if 240 in z:
                            mycoordinates.append([c,d])
                        elif 84 in z:
                            wallcoordinates.append([c,d])    
                        elif c<160:
                            enemycoordinates.append([c,d])
                            
                            
        if len(mycoordinates)>1 and len(enemycoordinates)>1:
            mn = len(mycoordinates)-1
            c=0
            diagonal=0.0
            for i in observation:
                c+=1
                d=0
                for z in i:
                    d+=1
                    if [c,d] in enemycoordinates:
                        up=(c-(mycoordinates[0][0]+2))
                        down=(d-(mycoordinates[0][1]+6))
                        if up!=0 and down!=0:
                            diagonal=abs(up/down)
                        if abs(diagonal)==1.0:
                        
                            if diagonal>0:
                                 if random.sample([0,1],1)[0]==0:
                                    if c>mycoordinates[0][0]:
                                        j=16
                                    else:
                                        j=14
                            else:
                                if random.sample([0,1],1)[0]==0:
                                    if c>mycoordinates[0][0]:
                                        j=17
                                    else:
                                        j=15
                        if c>mycoordinates[0][0]+4 and c< (mycoordinates[0][0] + 9):
                            flag=True                                        
                            if d>mycoordinates[0][1]+5:
                                for i in range(mycoordinates[0][1]+5,d):
                                    if [c,i] in wallcoordinates:
                                        flag=False
                                if flag:        
                                    j=11
                            else:
                                for i in range(d,mycoordinates[0][1]-3):
                                    if [c,i] in wallcoordinates:
                                        flag=False
                                if flag: 
                                    j=12
                        elif d>mycoordinates[0][1] and d<mycoordinates[-1][1]+5:
                            flag=True
                            if c>mycoordinates[-1][0]:
                                for i in range(mycoordinates[0][0]+20,c):
                                    if [i,d] in wallcoordinates:
                                        flag=False
                                if flag: 
                                    j=13
                            elif c<mycoordinates[0][0]:
                                for i in range(c,mycoordinates[0][0]):
                                    if [i,d] in wallcoordinates:
                                        flag=False
                                if flag: 
                                    j=10
                             
                                    
        if len(enemycoordinates) < random.sample([5,80],1)[0]:
                if len(mycoordinates)>1:
                    collide.append([mycoordinates[0][0]-5,mycoordinates[0][1]+2])
                    collide.append([mycoordinates[0][0],mycoordinates[0][1]+5])
                    collide.append([mycoordinates[0][0]-5,mycoordinates[0][1]-2])
                    collide.append([mycoordinates[-1][0]+5,mycoordinates[-1][1]])
                    
                    if collide[0] and collide[2] in wallcoordinates:
                        j=3
                        if collide[1] in wallcoordinates:
                            j=9
                    else:
                        if collide[1] in wallcoordinates:
                            j=5
                        elif collide[0] in wallcoordinates:
                            j=3
                        else:
                            j=2
  
        
        return j

## YOU MAY NOT MODIFY ANYTHING BELOW THIS LINE OR USE
## ANOTHER MAIN PROGRAM
if __name__ == '__main__':
    for i in range(100):
        parser = argparse.ArgumentParser(description=None)
        parser.add_argument('--env_id', nargs='?', default='Berzerk-v0', help='Select the environment to run')
        args = parser.parse_args()

        # You can set the level to logger.DEBUG or logger.WARN if you
        # want to change the amount of output.
        logger.set_level(logger.INFO)

        env = gym.make(args.env_id)

        # You provide the directory to write to (can be an existing
        # directory, including one with existing data -- all monitor files
        # will be namespaced). You can also dump to a tempdir if you'd
        # like: tempfile.mkdtemp().
        outdir = 'random-agent-results'
     


        env.seed(0)
        agent = Agent(env.action_space)

        episode_count = 100
        reward = 0
        done = False
        score = 0
        special_data = {}
        special_data['ale.lives'] = 3
        ob = env.reset()
        while not done:
            action = agent.act(ob, reward, done)
            #time.sleep(0.3)
            ob, reward, done, x = env.step(action)
            score += reward
            env.render()
         
        # Close the env and write monitor result info to disk
        print ("Your score: %d" % score)
        env.close()
        with open('/Users/rishab/Desktop/gym-master/data1.txt','a') as out:
            out.write("\nYour score: %d" % score)
        out.close()

