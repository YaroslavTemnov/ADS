class Queue:
    def __init__(self, elements):
        self.data = list(elements)
        self.head = 0

    def pop_first(self, shift):
        head = self.head
        if shift > 0:
            self.data.extend(self.data[head : head + shift])
            self.head += shift
        value = self.data[self.head]
        self.head += 1
        return value


    
    def __len__(self):
        return len(self.data) - self.head

t = int(input())
sizes = []
for i in range(t):
    sizes.append(int(input()))
for i in range(t):
    n = sizes[i]
    q = Queue(range(n))
    result = [0] * n
    for step in range(1, n+1):
        shift = step % (n - step + 1)

        pos = q.pop_first(shift)
        result[pos] = step
    print(*result)