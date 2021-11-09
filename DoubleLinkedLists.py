class Node():
    def __init__(self, dataval = None):
        self.dataval = dataval
        self.nextval = None
        self.prevval = None

class DLinkedList():
    def __init__(self):
        self.headval = None
    def print_slist(self):
        pointer = self.headval
        while pointer != None:
            print(pointer.dataval)
            pointer = pointer.nextval
    
    def length_dlist(self):
        pointer = self.headval
        counter = 0
        while pointer != None:
            pointer = pointer.nextval
            counter += 1
        return counter
    
    def value(self, position):
        #if position > self.length_slist():
        #    return None
        pointer = self.headval
        for i in range(0,position):
            pointer = pointer.nextval
        return pointer

    def find_value(self, value_to_look_for):
        pointer = self.headval
        counter = 0
        while pointer != None:
            if pointer.dataval == value_to_look_for:
                return counter
            else:
                pointer = pointer.nextval
                counter += 1
        print('Value not found!')

    def append_value(self, append_val):
        pointer = self.headval
        pointer2 = pointer.nextval
        e = Node(append_val)
        while pointer2 != None:
            pointer = pointer.nextval
            pointer2 = pointer.nextval
        pointer.nextval = e
        pointer.nextval.prevval = pointer
        print('Value appended correctly')  

    def add_value(self, added_value, position):
        #if position > self.length_slist():
        #    print('Error! Position invalid! Cannot add the value!')
        pointer = self.headval
        e = Node(added_value)
        for i in range(position-1):
            pointer = pointer.nextval
        e.nextval = pointer.nextval
        e.prevval = pointer
        pointer.nextval.prevval = e
        pointer.nextval = e
        print('Value added correctly!')

    def delete_value(self, position):
        #if position > self.length_slist():
        #    print('Error! Position invalid! Cannot add the value!')
        pointer = self.headval
        for i in range(position-1):
            pointer = pointer.nextval
        pointer.nextval = pointer.nextval.nextval
        pointer.nextval.prevval = pointer
       
        print('Value deleted correctly!')  


list2 = DLinkedList()
list2.headval = Node('Mon')
e2 = Node('Tue')
e3 = Node('Wed')
e4 = Node('Thu')
e5 = Node('Fry')
e6 = Node('Sat')
e7 = Node('Sun')

list2.headval.nextval = e2
e2.nextval = e3
e3.nextval = e4
e4.nextval = e5
e5.nextval = e6
e6.nextval = e7
e7.nextval = None

e2.prevval = list2.headval
e3.prevval = e2
e4.prevval = e3
e5.prevval = e4
e6.prevval = e5
e7.prevval = e6

list2.add_value('Thu',4)
list2.delete_value(4)

for i in range(1,list2.length_dlist()-1):
    print(list2.value(i).dataval, list2.value(i).nextval.dataval, list2.value(i).prevval.dataval)