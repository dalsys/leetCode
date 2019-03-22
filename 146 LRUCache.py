class LRUCache(object):
            

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.head=self.tail=None
        self.capacity=max(capacity, 0)
        self.cache={}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1

        node = self.cache[key]
        head = self.cache[self.head]
        prv = node["prev"]
        nxt = node["next"]
        if nxt:
            if not prv:
                self.tail = nxt
                self.cache[nxt]["prev"] = None
            else:
                self.cache[prv]["next"] = nxt
                self.cache[nxt]["prev"] = prv
            node["prev"] = self.head
            node["next"] = None
            head["next"] = self.head = key
        return node["value"]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.cache:
            node = self.cache[key]
            head = self.cache[self.head]
            prv = node["prev"]
            nxt = node["next"]
            print(prv, nxt)

            if nxt:                
                if not prv:
                    self.tail = nxt
                    self.cache[nxt]["prev"] = None
                else:
                    self.cache[prv]["next"] = nxt
                    self.cache[nxt]["prev"] = prv
                node["prev"] = self.head
                node["next"] = None                
                head["next"] = self.head = key
            self.cache[key]["value"] = value
            return

        if self.capacity==0:
            if not self.tail:
                return 
            tail = self.tail
            self.tail = self.cache[tail]["next"]
            if self.tail:
                self.cache[self.tail]["prev"] = None
            else:
                self.head = None
            del self.cache[tail]
            self.capacity+=1

        self.cache[key] = {"value":value, "prev":self.head, "next":None}
        if self.head:
            self.cache[self.head]["next"] = key
        if not self.tail:
            self.tail = key

        self.head = key
        self.capacity-=1

    def printCache(self):
        point = self.tail
        while point:
            print(point, end = " ")
            point = self.cache[point]["next"]

        print((self.tail, self.head, self.capacity))

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
        

if __name__ == '__main__':
    cache = LRUCache(2)

    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))
    cache.put(3, 3)
    cache.put(1, 1)
    cache.get(2)
    cache.put(4, 4)
    cache.get(1)
    cache.get(3)
    cache.get(4)


    # import random

    # n=random.randint(0, 100)
    # a = ["LRUCache"]
    # b = [[n]]


    # for i in range(random.randint(1, 8)*n):
    #     if random.randint(0, 1):
    #         a.append("put")
    #         b.append([random.randint(0, n*2)]*2)
    #     else:
    #         a.append("get")
    #         b.append([random.randint(0, n*2)])
    # print(a)
    # print(b)
