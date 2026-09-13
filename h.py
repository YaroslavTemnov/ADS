n = int(input())
queue = [int(x) for x in input().split()]
positions = [-1]
stack = [queue[0]]
for i in range (0, n+1):
    if i == n-1:
        break
    elif queue[i] < queue[i+1]:
        positions.append(queue[i])
        stack.append(queue[i+1])
    elif queue[i] == queue[i+1]:
        positions.append(positions[-1])
    elif queue[i] > queue[i+1]:
        while True:
            if len(stack) == 0:
                positions.append(-1)
                stack.append(queue[i+1])
                break
            elif queue[i+1] > stack[-1]:
                positions.append(stack[-1])
                stack.append(queue[i+1])
                break
            else:
                stack.pop()


for position in positions:
    print(position, end = " ")