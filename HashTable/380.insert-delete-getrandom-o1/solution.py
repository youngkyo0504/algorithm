import random
class RandomizedSet:

    def __init__(self):
        self.hash_map = {}
        self.arr  =[]
        

    def insert(self, val: int) -> bool:
        if val not in self.hash_map:
            self.arr.append(val)
            self.hash_map[val] = len(self.arr)-1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.hash_map:
            self.arr[self.hash_map[val]],self.arr[len(self.arr)-1] =  self.arr[len(self.arr)-1],self.arr[self.hash_map[val]]
            del self.arr[len(self.arr)-1]
            self.hash_map[self.arr[len(self.arr)-1]] = self.hash_map[val]
            del (self.hash_map[val])
            return True
        return False


    def getRandom(self) -> int:
        k = len(self.arr)-1
        if k == 0:
            return self.arr[0]
        random_index = random.randrange(0, k)
        return self.arr[random_index]



# # Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
param_1 = obj.insert(1)
param_1 = obj.insert(2)
param_2 = obj.remove(1)
param_3 = obj.getRandom()