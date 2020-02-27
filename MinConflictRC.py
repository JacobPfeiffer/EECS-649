import random # random() generates a uniform random number in [0.0, 1.0]
from math import ceil
import math
import numpy as np
EVALS = 0
# returns 1 if queens q1 and q2 are attacking each other, 0 o.w.

#attacking function obtained from DR. Branicky @ KU
def attacking(q1col, q1row, q2col, q2row):
  if q1col==q2col:
    return 1  # same column
  if q1row==q2row:
    return 1  # same row
  coldiff=q1col-q2col
  rowdiff=q1row-q2row
  if abs(coldiff)==abs(rowdiff):
    return 1  # same diagonal
  return 0

# evaluates the fitness of an encoding, defined as the number of
# non-attacking pairs of queens (28 - number of attacking pairs)
#
# the global variable EVALS keeps track of the number of times called
#fitness function obtained from DR. Branicky @ KU
def fitness(encoding):
  global EVALS
  EVALS += 1
  E = 28
  for i in range(1,8):
    for j in range(i+1,9):
      E -= attacking(i, encoding[i-1], j, encoding[j-1])
  return E



def findMininColumn(init, n, succ):
    min1=-1
    value=fitness(init)
    for j in range(8):

        if(j!=init[n]):
            succ[n] = j
            if fitness(succ) > value:
                min1 = j
                value=fitness(succ)

            elif fitness(succ) == value:
                if(random.random()<.5):
                    min1==j
                    value = fitness(succ)

        init[n] = min1
        succ[n] = min1



def test():
    file =open('output.txt','w')
    # test successor function
    failed=True
    min=-float('-inf')
    enc7 = [1, 2, 3, 4, 5, 6, 7, 8]
    numlist = [0,1, 2,3,4,5,6,7]
    count=0
    numbreaks=0
    numsuccess=0
    numvals=0

    for y in range(100):
        for x in range(8):
            enc7[x]=random.randrange(1,8)
        enc8 = enc7[:]
        count=0
        while failed:
            if fitness(enc7)==28:
                print("Solution was found!", " ", enc7, " Evaluations: ", count)
                failed=False
                break
            print(fitness(enc7)," ",count)
            #randomly selects a column to get
            i=random.choice(numlist)
            #finds min succesor and changes enc7 to corresponding value
            findMininColumn(enc7,i,enc8)
            count=count+1
            if count==10000:
                print("Search cutoff at 10000 iterations")
                numbreaks=numbreaks+1
                count=0
                break
            numsuccess=numsuccess+1
            numvals=numvals+count
        if y<100:
            failed=True
    print("Average # of evals: ",numvals/numsuccess)
    print("Number of failures (went through 10000 loops): ",numbreaks)





def test2():
    file =open('output.txt','w')
    # test successor function
    failed=True
    min=-float('-inf')
    enc7 = [1, 2, 3, 4, 5, 6, 7, 8]
    numlist = [0,1, 2,3,4,5,6,7]
    count=0
    numbreaks=0
    numsuccess=0
    numvals=0

    for y in range(100):
        for x in range(8):
            enc7[x]=random.randrange(1,8)
        enc8 = enc7[:]
        count=0
        i=0
        while failed:
            if fitness(enc7)==28:
                print("Solution was found!", " ", enc7, " Evaluations: ", count)
                failed=False
                break
            print(fitness(enc7)," ",count)
            #randomly selects a column to get
            #finds min succesor and changes enc7 to corresponding value
            findMininColumn(enc7,i,enc8)
            if i==7:
                i=0
            else:
                i=i+1
            count=count+1
            if count==10000:
                print("Search cutoff at 10000 iterations")
                numbreaks=numbreaks+1
                count=0
                break
            numsuccess=numsuccess+1
            numvals=numvals+count

        if y<100:
            failed=True
    print("Average # of evals: ",numvals/numsuccess)
    print("Number of failures (went through 10000 loops): ",numbreaks)

value = input("Type 1 to randomly select column to minimize or 2 to minimize columns in order")
if value=="1":
    test()
if value=="2":
    test2()

