s = input()
stack = []
for i in s:
    if len(stack) == 0:
        stack.append(i)
    else:
        if stack[-1] != i:
            stack.append(i)
        else:
            stack.pop()

if stack:
    print("YES")
else:
    print("NO")