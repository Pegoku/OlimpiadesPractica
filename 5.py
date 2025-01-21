nCycles = int(input())

dimensionsInput = input()

dimensions = dimensionsInput.split(" ")

h = int(dimensions[0])
v = int(dimensions[1])

map = []
for _ in range(h):
    a = input()
    if len(a) != v:
        print("Llargaria no correcte")
    llistah = []
    for i in a:
        llistah.append(i)
    map.append(llistah)

if h == 1:
    l = ""
    for i in range(v):
        l += "."
    print(l)
    
# print(map)
# for a in map:
#     x = []
#     for b in a:
#         x.append(b)
#     print(x)