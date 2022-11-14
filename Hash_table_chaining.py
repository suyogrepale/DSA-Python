# creating hash function for hash table

class Hashtable:
    def __init__(self):
        self.MAX=100
        self.arr=[[] for i in range(self.MAX)]

    def get_hash(self,key):
        h=0
        for char in key:
            h+=ord(char)
        return h%self.MAX

    def __setitem__(self,key,value):   #pre-defined method to set value at an index
        h=self.get_hash(key)
        found = False
        for idx,element in enumerate(self.arr[h]):
            if(len(element)==2 and element[0]==key):
                self.arr[h][idx]=(key,value)
                found=True
                break
        if not found:
            self.arr[h].append((key,value))

    def __getitem__(self,key):                 #pre-defined method to get value at an index
        h=self.get_hash(key)
        for element in self.arr[h]:
            if element[0]==key:
                return element[1]

    def __delitem__(self,key):
        h=self.get_hash(key)
        for index,element in enumerate(self.arr[h]):
            if element[0]==key:
                del self.arr[h][index]


t=Hashtable()
t["March 6"]=301
t["March 7"]=305
t["March 17"]=315


print(t["March 6"])
print(t["March 7"])
print(t.arr)
del t["March 7"]
print(t.arr)