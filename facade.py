"""
Structural Pattern - Facade 外觀模式
為子系統中的一組介面提供一致的介面，外觀模式定義了一個高層介面，這個介面使得這一子系統更加容易使用。
"""

# Python arrays are dynamic by default, but this is an example of resizing.
class Array:
    def __init__(self):
        self.capacity = 2
        self.lenght = 0
        self.arr = [0] * 2  # Array of capacity = 2

    # Insert n in the last position of the array
    def pushback(self, n):
        if self.lenght == self.capacity:
            self.resize()

        # insert at next empty position
        self.arr[self.lenght] = n
        self.lenght += 1

    def resize(self):
        # Create new array of double capacity
        self.capacity = 2 * self.capacity
        newArr = [0] * self.capacity

        # Copy elements to newArr
        for i in range(self.lenght):
            newArr[i] = self.arr[i]
