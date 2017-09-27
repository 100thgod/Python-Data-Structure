from Node import Node
class UnorderedList:
    def __init__(self):
        self.head = None
        self.last = None

    def is_empty(self):
        return self.head == None
    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        if self.head == None:
            self.last = temp
        self.head = temp
    def size(self):
        current = self.head
        count = 0
        while current!= None:
            count+=1
            current = current.get_next()
        return count
    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                current =current.get_next()
        return found
    def remove(self, item):
        current = self.head
        previous = None
        found = False

        while not found:
            if current.get_data() == item :
                found =True
            else:
                previous = current 
                current = current.get_next()
        if previous == None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def append(self, item):
        last = self.last
        temp = Node(item)
        last.set_next(temp)

mylist = UnorderedList()
mylist.add(31)
mylist.add(77) 
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)
print(mylist.size())
print(mylist.search(93))
mylist.append(100)
print(mylist.search(100)) 
