nCycles = int(input())

for _ in range(nCycles):
    inValues = input()
    nums = inValues.split(" ")
    # numsSet = set(nums)
    # if len(numsSet) != len(nums):
    #     print("PARANORMAL") 
    #     continue
    
    numsInt = []
    for i in nums:
        numsInt.append(int(i))
    # print(numsInt)
    llista = []
    for a in numsInt:
        if a > 0:
            llista.append(a)
        elif a < 0:
            if llista and llista[-1] == abs(a):
                llista.pop()
    #     print(llista)
    # print(llista)
    if len(llista) == 0:
        print("NORMAL")
    else:
        print("PARANORMAL")

exit(0)