# https://leetcode.com/problems/design-hashmap/
import collections


class ListNode:
    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next


class MyHashMap:
    def __init__(self):
        self.capacity = 1000000
        self.table = collections.defaultdict(ListNode)

    def hash_value(self, key):
        return key % self.capacity

    def put(self, key: int, value: int) -> None:
        hash = self.hash_value(key)
        p = self.table[hash]

        while p:
            if p.key == key:
                p.value = value
                return
            p = p.next

        tmp = ListNode(key, value, self.table[hash])
        self.table[hash] = tmp

    def get(self, key: int) -> int:
        hash = self.hash_value(key)
        p = self.table[hash]

        while p:
            if p.key == key:
                return p.value

            p = p.next

        return -1

    def remove(self, key: int) -> None:
        hash = self.hash_value(key)
        p = self.table[hash]
        pp = None

        while p:
            if p.key == key:
                if pp is None:
                    self.table[hash] = p.next
                else:
                    pp.next = p.next

            pp = p
            p = p.next


# Your MyHashMap object will be instantiated and called as such:
obj = MyHashMap()
obj.put(2, 2)
obj.put(2, 3)
param_2 = obj.get(2)
print(param_2)
remove = obj.remove(2)
param_2 = obj.get(2)
print(param_2)
