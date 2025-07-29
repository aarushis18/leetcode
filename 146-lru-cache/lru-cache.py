class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value

        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.map = {}  # key -> Node
        self.capacity = capacity

        self.head = Node(None, None)
        self.tail = Node(None, None)

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        node = Node(None, None)

        if key not in self.map:
            return -1
        else:
            node = self.map[key]

        # remove node:
        node.prev.next = node.next
        node.next.prev = node.prev

        # add to tail (make node the MRU)
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node

        return node.value


    def put(self, key: int, value: int) -> None:
        node = Node(None, None)
        
        if key in self.map:
            node = self.map[key]
            node.value = value

            # remove node:
            node.prev.next = node.next
            node.next.prev = node.prev

            # add to tail (make node the MRU)
            node.prev = self.tail.prev
            node.next = self.tail
            self.tail.prev.next = node
            self.tail.prev = node

        else:
            node = Node(key, value)
            self.map[key] = node

            node.prev = self.tail.prev
            node.next = self.tail
            self.tail.prev.next = node
            self.tail.prev = node

            if len(self.map) > self.capacity:
                lru = self.head.next
                if lru == self.tail: return None  # empty
                lru.prev.next = lru.next
                lru.next.prev = lru.prev
                del self.map[lru.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
