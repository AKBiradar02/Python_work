def init(self):
    self.st = []
    self.d = 0


def next(self, price: int) -> int:
    l = -1

    while self.st and self.st[-1][0] <= price:
        self.st.pop()

    if self.st:
        l = self.st[-1][-1]
        ans = self.d - l
        self.st.append((price, self.d))
        self.d += 1

    return ans

