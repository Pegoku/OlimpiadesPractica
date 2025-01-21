nCycles = int(input())

for _ in range(nCycles):
    a = input()
    numsInput = input()
    nums = numsInput.split(" ")
    # print(nums)
    # print (max(nums))
    numsInt = []
    for i in nums:
        numsInt.append(int(i))
    # print(nums)

    maxNum = max(numsInt)
    maxNumCount = 0
    for i in numsInt:
        if i == maxNum:
            maxNumCount += 1
    print(f"{maxNum} {maxNumCount}")