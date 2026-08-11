class max_heap:
    def __init__(self):
        self.heap = []

    def parent(self, i): return (i - 1) // 2
    def left_child(self, i): return 2 * i + 1
    def right_child(self, i): return 2 * i + 2

    def pop(self):

        try:

            if len(self.heap) == 1:
                return self.heap[0]

            max_value = self.heap[0]

            last_element = self.heap.pop()

            self.heap[0] = last_element
            self.shift_down(0)
            return max_value

        except IndexError as e:
            print(f"{e}")

    def push(self, value):
        self.heap.append(value)

        self.shift_up(len(self.heap) - 1)   """ this helps to sort the new appended element to the list according to heap tree"""

    def shift_up(self, i):
        parent_i = self.parent(i)

        while i > 0 and self.heap[i] > self.heap[parent_i]:

            self.heap[i], self.heap[parent_i] = self.heap[parent_i], self.heap[i]
            i = parent_i

    def shift_down(self, i):

        while True:
            left = self.left_child(i)
            right = self.right_child(i)

            if left >= len(self.heap):
                break
            
            largest = left

            if right < len(self.heap) and self.heap[right] > self.heap[left]:   """ right and left are just indicies not values, you need to access the values through the heap. """
                largest = right

            if self.heap[i] >= self.heap[largest]:
                break

            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]

            i = largest
             

heap = max_heap()

heap.push(10)
heap.push(4)
heap.push(15)
heap.push(20)
heap.push(8)

print(heap.pop())
print(heap.heap)




""" now this is just a different approach to help understanding problem-solving better. """
class  max_heap:
    parent = staticmethod(lambda i: (i - 1) // 2)    
    left_child = staticmethod(lambda i: 2 * i + 1)
    right_child = staticmethod(lambda i: 2 * i + 2)
    
    """here you can't just say lambda because it is assigned as a class attribute with a function value
       so python treats it as any other method, so when python calls it, it automatically kick is 'self' as the first argument
    (just like you would normally do with def parent(self, i) ) but lambda takes only 1 parameter so it will throw an error !
     to prevent such a thing, we wrap it using a staticmethod since it tells python to ignore the 'self' auto-bound

     
    also important note: lambda is NOT faster than a normal function at all !!, its only purpose is to be used ONLY when the function is just a simple one line
     and you don't want to spend time thinking for a name for i"""
    
    def __init__(self):
        self.heap = []

    def pop(self):
        try:
            if len(self.heap) == 1:
                return self.heap[0]

            max_value = self.heap[0]

            last_element = self.heap.pop()

            self.heap[0] = last_element

            self.shift_down(0)
            return max_value

        except IndexError:
            print("The list is empty !!")

    def push(self, value):

        self.heap.append(value)

        self.shift_up(len(self.heap) - 1)

    def shift_up(self, i):
        while i > 0 and self.heap[i] > self.heap[self.parent(i)]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]   """ here of cousrse it is better to create variables for each thing for readability
                                                                    unlike many claim, variables almost never affect the time nor the space complixity of the code.
                                                                    so it is better to assign variables but here I'm just doing this hardcore code for fun to test my optimization
                                                                    but do NOT do this in a real-life program"""
            i = self.parent(i)

    def shift_down(self, i):
        while True:
            
            if self.left_child(i) >= len(self.heap):
                break

            largest = self.left_child(i)

            if self.right_child(i) < len(self.heap) and self.heap[self.right_child(i)] > self.heap[self.left_child(i)]:
                largest = self.right_child(i)

            if self.heap[i] >= self.heap[largest]:
                break

            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]

            i = largest
