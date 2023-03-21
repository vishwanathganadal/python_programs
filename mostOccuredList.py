def mostOccured(x):
    counter = 0
    result = x[0]
     
    for i in x:
        curr_frequency = x.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            result = i
 
    return result

def start():
    list1 = [1,2,2,3,3,3,4]
    message = mostOccured(list1)
    print(message)


start()