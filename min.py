#How would you design a stack that has a function that would return the min element?

#linked list for stack, store mininum into node min.data, if next item pushed has a lower value, then replace that min.data.
import unittest

class Node():

    def __init__(self, data):
        self.data = data
        self.next = None
    

class MinStack():

    def __init__ (self):
        self.top = None
        self.mini = None

    def push(self, num):



        
        if self.mini is not None and self.mini.data < num:
            self.mini = Node(self.mini.data)
            self.mini.next = self.mini
        else:
            self.mini = Node(num)
            self.mini.next = self.mini
        self.top = Node(num)
        self.top.next = self.top

    def pop(self):

        if not self.top:
            return None
        #gotta adjust for old min 
        self.mini = self.mini.next
        item = self.top.data
        self.top = self.top.next
        return item

    def min(self):
        if not self.mini:
            return None
        return self.mini.data

        
        # if self.min is not None and self.min.data < num:
        #     self.min = Node(self.min.data)
        # else:
        #     self.min = Node(num)
        #     self.min.next = self.min
        # #if there's an empty stack, assign top with the num
        # self.top = Node(num)

# class MinStack():
#   def __init__(self):
#     self.top, self._min = None, None
    
#   def min(self):
#     if not self._min:
#       return None
#     return self._min.data
    
#   def push(self, item):
#     if self._min and (self._min.data < item):
#       self._min = Node(data=self._min.data, next=self._min)
#     else:
#       self._min = Node(data=item, next=self._min)
#     self.top = Node(data=item, next=self.top)
  
#   def pop(self):
#     if not self.top:
#       return None
#     self._min = self._min.next
#     item = self.top.data
#     self.top = self.top.next
#     return item


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
    self.assertEqual(min_stack.pop(), 5)
    self.assertEqual(min_stack.min(), 6)
    self.assertEqual(min_stack.pop(), 6)
    self.assertEqual(min_stack.pop(), 7)
    self.assertEqual(min_stack.min(), None)

if __name__ == "__main__":
  unittest.main()