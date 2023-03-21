def search(str1,x):
    if x in str1:
        count = 0
        for i in range(0,len(str1)):
            if str1[i] == x:
                count = count + 1
        return count
    else:
        return -1

def start1():
    str1 = input("Enter string:")
    x = input("Enter letter to search:")
    result = search(str1,x)
    print(result)


#######################################


def noOfWords(str1):
    result = len(str1.split())
    return result

def start():
    str1 = input("Enter string:")
    message = noOfWords(str1)
    print(message)


while True:
    print("1.Count the no of words")
    print("2.Count the no of specific letter u want to find ")
    print("0.End")
    ch = int(input("Enter choice:"))
    if ch == 1:
        start()
    elif ch == 2:
        start1()
    elif ch == 0:
        break
    else:
        print("no such option")