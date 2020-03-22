#describe how you could use a single array to implement three stacks.

#in order to do this an efficient way, where all free spots in the array(arr) should be available for all k stacks.

#create two extra arrays:
    #top[] - store the top index of all stacks. initialize with -1, indicates no element in particular stack.
    #next[] - stores the indexes of the next items. same size ass arr length. initialize as index plus 1 (so 1,2,3,4,5,....to -1) in order to show the next spot
    #free - a variable to store the next available free spot. initially 0, so you can push first element to 0 index 

#for push (20, in stack 2):
    #1. free shows us the "free" spot; if it is 0, then at index 0 in arr you can push the element 20.
    #2. go to same index number as the free variable, in this case 0, at next array. at index 0 in the next array, it has the element 1 (which is the next free spot. 
    #3. replace free with 1
    #4. in next array, replace 0 index with the element of top[2], which is currently -1. so at next array[0], it stores -1 so that we understand there is no next element in arr at the same index since there is only one element.
    #5. replace top[2] with 0

#push again (25, in stack 2):
    #1. free says 1, so push 25 to arr[1]
    #2. update free spot.. currently has 1
        #go to next[1], which is 2
        #free becomes 2
    #3. now 25 is the new top of the stack, so we have to link 25 and 20 as 20 is considered "next"
    #4. element 25 in arr is at arr[1], so next[1] gets updated to 0.
    #5. top[2] is now 1, since 25 is new top of stack
    #6. if we wanna find next, next[1] shows index of next element

#if we reach -1, stack is full.

class NStacks:

    def __init__(self, n, k):
        self.n = n #number of stacks
        self.k = k #size of the array

        #initialize array, which holds n stacks with size of k
        self.arr = [0] * self.k
        #initialize top, all -1 to show stack is empty, with the length of number of stacks
        self.top = [-1] * self.n

        self.free = 0

        #create next arr, same size as arr but elements are +1 index, last index is 0
        self.next = [i + 1 for i in range(self.k)]
        self.next[self.k - 1] = -1

    def isEmpty(self, stacknum):
        return self.top[stacknum] == -1

    def isFull(self):
        return self.free == -1

    def push(self, item, stacknum):
    #push item in given stack number, using arr efficiently
        if self.isFull():
            print("Stack Overflow")
            return

        insert_at = self.free
        self.free = self.next[self.free]
        self.arr[insert_at] = item
        self.next[insert_at] = self.top[stacknum]
   

        self.top[stacknum] = insert_at

    def pop(self, stacknum):
        if self.isEmpty(stacknum):
            return None

        popper = self.arr[self.top[stacknum]]
        i = self.arr.index(popper)
        self.top[stacknum] = self.next[i]
        self.next[i] = self.free
        free = i
        return popper

    def printstack(self, sn): 
        top_index = self.top[sn] 
        while (top_index != -1): 
            print(self.arr[top_index]) 
            top_index = self.next[top_index]







if __name__ == "__main__": 
      
    # Create 3 stacks using an  
    # array of size 10. 
    nstacks = NStacks(3, 10) 
  
    # Push some items onto stack number 2. 
    nstacks.push(15, 2) 
    nstacks.push(45, 2) 
  
    # # Push some items onto stack number 1. 
    nstacks.push(17, 1) 
    nstacks.push(49, 1) 
    nstacks.push(39, 1) 
  
    # Push some items onto stack number 0. 
    nstacks.push(11, 0) 
    nstacks.push(9, 0) 
    nstacks.push(7, 0) 
  
    print("Popped element from stack 2 is " + 
                         str(nstacks.pop(2))) 
    print("Popped element from stack 1 is " + 
                         str(nstacks.pop(1))) 
    print("Popped element from stack 0 is " + 
                         str(nstacks.pop(0))) 
  
    nstacks.printstack(0)









