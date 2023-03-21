def search(str1,x):
    if x in str1:
        count = 0
 
        for i in range(0,len(str1)):
            if str1[i] == x:
                count = count + 1
        return count
    
    else:
        return -1


def start():
    str1 = input("Enter string:")
    x = input("Enter letter to search:")
    result = search(str1,x)
    print(result)


start()