def lcd(a, b):
    if b == 0:
        return a
    else:
        return(lcd(b, a%b))

a, b = list(map(int, input().split()))
print(lcd(a, b))