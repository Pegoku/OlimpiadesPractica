nCycles = int(input())

def sumPastisos(llista):
    pes = 0
    for i in llista:
        pes = pes + i
    return pes

def reverse(llista):
    llista.reverse()
    return llista
for _ in range(nCycles):
    nPastisos = int(input())
    pastissos = input().split(" ")
    pastissos = list(map(int, pastissos))
    pesPastisos = 0
    pastisosL = []
    pastisosR = []
    pesPastisosL = 0
    pesPastisosR = 0
    mid2partsLast = 0
    
    for i in pastissos:
        i = int(i)
        pesPastisos = pesPastisos + i
    
    midPastisosPes = pesPastisos / 2
    print (f"midPastisosPes {midPastisosPes}")
    pastissos
    print(pastissos)
    print(reverse(pastissos))
    for l in pastissos:
        pastisosR = []
        l = int(l)
        pastisosL.append(l)
        pesPastisosL = sumPastisos(pastisosL)
        print(f"L {pastisosL} {pesPastisosL}")
        for r in reverse(pastissos):
            r = int(r)
            pastisosR.append(r)
            
            pesPastisosR = sumPastisos(pastisosR)
            print(f"R {pastisosR} {pesPastisosR} {r}")
            if pesPastisosL == pesPastisosR and pesPastisosL <= midPastisosPes and pesPastisosR > 1:
                # print(f"iguals {pastisosL} {pastisosR}")
                break
            elif pesPastisosR > pesPastisosL or pesPastisosL > midPastisosPes:
                # print(f"mes grans {pastisosL} {pastisosR}")
                break
            # else:
                # print(f"mes petits {pastisosL} {pastisosR}")

        print(f"R {pastisosR} {pesPastisosR} {midPastisosPes}")
        print(f"L {pastisosL} {pesPastisosL} {midPastisosPes}")
        if pesPastisosL == midPastisosPes:
            # print(f"iguals {pastisosL} pesPastisosL {pesPastisosL}")
            print(pesPastisosL)
            mid2partsLast = pesPastisosL
            break       
            
    print(mid2partsLast)
            
        
        # if sumPastisos(pastisosL) == midPastisosPes:
        #     print(pastisosL)
        #     break
            
    
    # print(pastissos)

