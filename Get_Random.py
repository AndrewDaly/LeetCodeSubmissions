print('running')
class RandomizedSet(object):

    def __init__(self):
        self.base_set = set()

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        present = True
        if val in self.base_set:
            present = False
        self.base_set.add(val)
        return present

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        present = False
        if val in self.base_set:
            present = True
        self.base_set.discard(val)
        return present

    def getRandom(self):
        """
        :rtype: int
        """
        val = next(iter(self.base_set))
        [self.base_set][]
        return val


# Your RandomizedSet object will be instantiated and called as such:
#["RandomizedSet","insert","remove","insert","getRandom","remove","insert","getRandom"]
#[[],[1],[2],[2],[],[1],[2],[]]
obj = RandomizedSet()
print('randomizedSet ' + str(obj.base_set))
param_1 = obj.insert(1)
print('inserted 1' + str(obj.base_set))
param_2 = obj.remove(2)
print('removed 2' + str(obj.base_set))
param_3 = obj.insert(2)
print('inserted 2' + str(obj.base_set))
param_4 = obj.getRandom()
print('getRandom' + str(obj.base_set))
param_5 = obj.remove(1)
print('remove 1' + str(obj.base_set))
#param_6 = obj.insert(2)
#print(obj.base_set)

print(param_1)
print(param_2)
print(param_3)
print(param_4)
print(param_5)
#print(param_6)