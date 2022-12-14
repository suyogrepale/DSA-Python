# creating hash function for hash table

class Hashtable:
    def __init__(self):
        self.MAX=100
        self.arr=[None for i in range(self.MAX)]

    def get_hash(self,key):
        h=0
        for char in key:
            h+=ord(char)
        return h%self.MAX

    def __setitem__(self,key,value):   #pre-defined method to set value at an index
        h=self.get_hash(key)
        self.arr[h]=value

    def __getitem__(self,key):                 #pre-defined method to get value at an index
        h=self.get_hash(key)
        return self.arr[h]

    def __delitem__(self,key):
        h=self.get_hash(key)
        self.arr[h]=None


t=Hashtable()
t['March 6']=301
t['March 7']=305

print(t['March 6'])
print(t['March 7'])
print(t.arr)
del t['March 7']
print(t.arr)