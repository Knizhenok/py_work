class Node:
    const = 0

    def __init__(self, data):
        self.data = data
        self.next = None

    def append(self, val):
        end = Node(val)
        self.const += 1
        n = self
        print(f'n = {n}')

        while n.next:
            n = n.next
            print(f'n.next {n}')
        n.next = end

        print(self.const)


if __name__ == '__main__':
    ll = Node(1)

    ll.append(2)
    ll.append(3)
