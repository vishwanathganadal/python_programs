def noOfWords(str1):
    result = len(str1.split())
    return result



def start():
    str1 = input("Enter string:")
    message = noOfWords(str1)
    print(message)


start()