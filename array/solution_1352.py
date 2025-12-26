class ProductOfNumbers:

    def __init__(self):
        self.preSum = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.preSum = [1]
        else:
            self.preSum.append(self.preSum[-1] * num)

    def getProduct(self, k: int) -> int:
        if len(self.preSum) <= k:
            return 0
        return self.preSum[-1] // self.preSum[-1 - k]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

productOfNumbers = ProductOfNumbers();
productOfNumbers.add(3);
productOfNumbers.add(0);
productOfNumbers.add(2);
productOfNumbers.add(5);
productOfNumbers.add(4);
productOfNumbers.getProduct(2);
productOfNumbers.getProduct(3);
productOfNumbers.getProduct(4);
productOfNumbers.add(8);
productOfNumbers.getProduct(2);
