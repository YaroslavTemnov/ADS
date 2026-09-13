def Boris_win():
    b.append(n.pop(0))
    b.append(b.pop(0))

def Nursik_win():
    n.append(b.pop(0))    
    n.append(n.pop(0))


b = [int(x) for x in input().split()]
n = [int(x) for x in input().split()]
c = 0
while len(b) > 0 and len(b) < 10:
    if b[0] == 0 and n[0] == 9:
        Boris_win()
    elif b[0] == 9 and n[0] == 0:
        Nursik_win()          
    elif b[0] > n[0]:
        Boris_win()
    else:
        Nursik_win()
    c += 1

if b:
    print("Boris", c)
else:
    print("Nursik", c)