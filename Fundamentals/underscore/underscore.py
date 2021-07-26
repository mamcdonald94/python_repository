class Underscore:
    def map(self, iterable, callback):
        for i in range(len(iterable)):
            iterable[i] = callback(iterable[i])
        return iterable
    def find(self, iterable, callback):
        for x in iterable:
            if callback(x) == True:
                return x
            else:
                continue
    def filter(self, iterable, callback):
        matching_list = []
        for i in range(len(iterable)):
            if callback(iterable[i]) == True:
                matching_list.append(iterable[i])
        return matching_list
    def reject(self, iterable, callback):
        unmatching_list = []
        for i in range(len(iterable)):
            if callback(iterable[i]) == False:
                unmatching_list.append(iterable[i])
        return unmatching_list

test = Underscore()

result1 = test.map([1, 2, 3], lambda x: x * 2)
result2 = test.find([1, 2, 3, 4, 5], lambda x: x > 4)
result3 = test.filter([1, 2, 3, 4, 5, 6, 7, 8], lambda x: x % 2 == 0)
result4 = test.reject([1, 2, 3, 4, 5, 6, 7, 8], lambda x: x % 2 == 0)

print(result1)
print(result2)
print(result3)
print(result4)