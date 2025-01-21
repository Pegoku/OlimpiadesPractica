nCycles = int(input())


def sqrt(a):
    return a**0.5

for i in range(nCycles):

    nums = []
    inwords = (input())
    
    words = inwords.split(" ")
    for i in words:
        nums.append(int(i))
        
    print(int(sqrt((nums[0]**2) + (nums[1]**2))))


