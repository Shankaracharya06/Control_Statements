class KErr(Exception):
    ...
class KeyType(Exception):
    ...

class KeyedList:
    def __init__(self):
        # to store the keys and values in this KeyedList
        self.data = []
        # To store only keys in this set
        self.keys = {}
    def add(self, *args):
        count = 0
        start = 0
        end = len(args) // 2
        while start < end + 1:

            if count < len(args):
                if type(args[count]) not in [list,set,dict]:
                    if args[count] not in self.data:
                        item = (args[count],args[count+1])
                        self.data.append(item)
                        self.keys = args[count]
                        count += 2
                        start += 1
                    else:
                        self.data[args[count]] = args[count+1]
                        count += 2
                        start += 1 
                else:
                    raise KeyType("key should be immutable type of data")
            else:
                break
list1 = KeyedList()
list1.add([50],56,'hii',70,'hie',50)
# print(list1.__dict__)
print(list1.data)