class OrderedStream:

    def __init__(self, n: int):
        self.idx = 0
        self.table = [0] * n

    def insert(self, idKey: int, value: str) -> List[str]:
        idKey -= 1
        self.table[idKey] = value
        result = []
        
        if self.idx != idKey:
            return result
        while self.idx < len(self.table) and self.table[self.idx]:
            result.append(self.table[self.idx])
            self.idx += 1
        return result


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)