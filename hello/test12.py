#for testing
import random 


def runArray(): 
    testArray=[]
    for j in range(10):
        testArray.append(random.randint(1,20))
    print('Randomised list is: ',testArray)