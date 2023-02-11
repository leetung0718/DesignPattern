"""
Behavioral Pattern - Strategy 策略模式
定義一系列的演算法，並且把這些算法，用介面封裝到有公共介面的策略類中，使他們可以互相替換。
"""

from abc import ABC, abstractclassmethod


class FilterStrategy(ABC):
    @abstractclassmethod
    def removeValue(self, val):
        pass


class RemoveNegStrategy(FilterStrategy):
    def removeValue(self, val):
        return val < 0


class RemoveOddStrategy(FilterStrategy):
    def removeValue(self, val):
        return abs(val) % 2


class Values:
    def __init__(self, vals):
        self.vals = vals

    def filter(self, strategy):
        res = []
        for n in self.vals:
            if not strategy.removeValue(n):
                res.append(n)
        return res


values = Values([-7, -4, -1, 0, 2, 6, 9])

print(values.filter(RemoveNegStrategy()))
print(values.filter(RemoveOddStrategy()))
