#How would you design a stack that has a function that would return the min element?

#linked list for stack, store mininum into node min.data, if next item pushed has a lower value, then replace that min.data.
import unittest

class Node():

    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self): 
        return "Node({})".format(self.data) 

    __repr__ = __str__
    

class MinStack():

    def __init__ (self):
        self.top = None
        self.mini = None

    def push(self, num):



        if self.top is None:
            #if empty, then mini is num and top is num
            self.top = Node(num)
            self.mini = Node(num)
    
        elif self.mini is not None and self.mini.data > num:
            #if num is less than the current min, create new node that becomes new min
            #link that new min to old min, so that we can reference it later
            new_min = Node(num)
            new_min.next = self.mini
            self.mini = new_min
            #create new node based on num, which goes to the top of the stack
            #link new node's next to self.top, the old top
            #make sure self.top is now the new node
            new_node = Node(num)
            new_node.next = self.top
            self.top = new_node
        
        else:
            #basically the same thing just that mini is not updated
            new_node = Node(num)
            new_node.next = self.top
            self.top = new_node
        
        
    def peek(self):
        if self.top is None:
            print("empty")
        else:
            print("the top most element is : {}" .format(self.top.data))
            print("min is {} next is {}" .format(self.mini.data, self.mini.next.data))
    def __str__(self): 
        temp = self.top 
        out = [] 
        while temp: 
            out.append(str(temp.value)) 
            temp = temp.next
        out = '\n'.join(out) 
        return ('Top {} \n\nStack :\n{}'.format(self.top,out)) 
    __repr__ = __str__

    def pop(self):

        if not self.top:
            return None
        #gotta adjust for old min 
        # self.mini = self.mini.next
        else:
            item = self.top.data
            self.top = self.top.next
            if item == self.mini.data:
            # if the item that is being popped out, is also mini, then we gotta make sure mini updates to the "next" mini
                self.mini = self.mini.next

        return item

    def min(self):
        if not self.mini:
            return None
        return self.mini.data
        

    def print(self):
        print(self.top)

       

class Test(unittest.TestCase):
  def test_min_stack(self):
    min_stack = MinStack()
    self.assertEqual(min_stack.min(), None)
    min_stack.push(7)
    self.assertEqual(min_stack.min(), 7)
    min_stack.push(6)
    min_stack.push(5)
    self.assertEqual(min_stack.min(), 5)
    min_stack.push(10)
    self.assertEqual(min_stack.min(), 5)
    self.assertEqual(min_stack.pop(), 10)
    min_stack.peek()
    self.assertEqual(min_stack.pop(), 5)
    min_stack.peek()
    min_stack.min()
    self.assertEqual(min_stack.min(), 6)
    self.assertEqual(min_stack.pop(), 6)
    self.assertEqual(min_stack.pop(), 7)
    self.assertEqual(min_stack.min(), None)

if __name__ == "__main__":
  unittest.main()