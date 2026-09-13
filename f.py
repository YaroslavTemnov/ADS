a = input()
b = input()
i = 0
aa = []
bb = []
if a.count("#") != b.count("#") and len(a) == len(b):
    print("No")
else:
    for j in a:
        if j == "#":
            del aa[i-1:i+1]
            i -= 1
        else:
            i += 1 
            aa.append(j)
    i = 0

    for j in b:
        if j == "#":
            del bb[i-1:i+1]
            i -= 1
        else:
            bb.append(j)
            i += 1    

    if aa == bb:
        print("Yes")
    else:
        print("No")
