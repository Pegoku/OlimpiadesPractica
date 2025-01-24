nCycles = int(input())
for _ in range(nCycles):
    inValues = input()
    nums = inValues.split(" ")
    if nums == ['0']:
        print("NORMAL")
        continue
    numsInt = [int(a) for a in nums if a!='0']
    llista = []
    for a in numsInt:
        if a > 0:
            llista.append(a)
        else:
            if len(llista) > 0 and llista[-1] == abs(a):
                llista.pop()
            else:
                llista = [1]
                break
    if len(llista) == 0:
        print("NORMAL")
    else:
        print("PARANORMAL")
