# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 16:42:26 2021

@author: TOSHIBA
"""

import random
maxm = 10000000
minm = 1
number = random.randint(minm, maxm)
no_of_guess = 1
direction = 0
guess = random.randint(minm, maxm)
while(True):
    if(guess == number):
        print("Right Guess ", guess)
        break
    elif(guess>number):
        print("A bit low than", guess)
        maxm = guess
        guess = random.randint(minm, maxm)
    else:
        print("A bit higher than", guess)
        minm = guess
        guess =  random.randint(minm, maxm)
    no_of_guess += 1
        
print("No of Guesses :", no_of_guess)       


#A bit low than 8836393
#A bit low than 1912762
#A bit low than 1846807
#A bit low than 1576197
#A bit low than 1274541
#A bit low than 1048948
#A bit higher than 103898
#A bit low than 618194
#A bit higher than 248142
#A bit higher than 511765
#A bit higher than 522807
#A bit low than 587180
#A bit higher than 546581
#A bit higher than 559721
#A bit higher than 571593
#A bit low than 580356
#A bit higher than 573015
#A bit higher than 573882
#A bit low than 576523
#A bit low than 574679
#A bit higher than 574190
#A bit low than 574364
#A bit low than 574314
#A bit low than 574311
#A bit low than 574244
#A bit higher than 574196
#A bit higher than 574209
#A bit low than 574222
#Right Guess  574210
#No of Guesses : 29