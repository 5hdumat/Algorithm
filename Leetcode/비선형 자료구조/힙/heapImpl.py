import sys


class BinaryHeap(object):
    def __init__(self):
        self.items = [None, 1, 2, 3, 4, 5, 6]

    def __len__(self):
        return len(self.items) - 1

    def _percolate_up(self):
        i = len(self)
        parent = i // 2
        while parent > 0:
            if self.items[parent] > self.items[i]:
                self.items[parent], self.items[i] = self.items[i], self.items[parent]

            i = parent
            parent = i // 2

    def insert(self, k):
        self.items.append(k)
        self._percolate_up()

    def _percolate_down(self, idx):
        left = idx * 2
        right = idx * 2 + 1
        smallest = idx

        if left <= len(self) and self.items[left] < self.items[smallest]:
            smallest = left

        if right <= len(self) and self.items[right] < self.items[smallest]:
            smallest = right

        if smallest != idx:
            self.items[idx], self.items[smallest] = self.items[smallest], self.items[idx]
            self._percolate_down(smallest)

    def extract(self):
        root = self.items[1]
        self.items.remove(root)
        self.items.insert(1, self.items.pop())
        self._percolate_down(1)

        # print(self.items)
        return root


s = BinaryHeap()
s.extract()
