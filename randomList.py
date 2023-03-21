import random

def randomList(x,y):
    randomlist = []
    for i in range(0,10):
        n = random.randint(x,y)
        randomlist.append(n)

    return randomlist

def start():
    message = randomList(10,20)
    print(message)


start()




