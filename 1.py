nCycles = int(input())



outWord = []




for i in range(nCycles):
    inwords = (input())

    outword = []
    
    words = inwords.split(" ")
    capitalizedWords = [word.capitalize() for word in words]
    outWord.append(" ".join(capitalizedWords))
    print(" ".join(outWord))
    capitalizedWords = []
    outWord = []


