'''
Implementing our own List Class

Custom Dynamic Array

In this exercise, you will implement a custom dynamic array class, 
similar to Python’s built-in list. Your task is to create a class CustomList that 
supports dynamic resizing and several list operations.
'''

import ctypes

class CustomList:
    def __init__(self):
        initialCapacity = 1
        self.capacity = initialCapacity
        self.size = 0
        self.array = self.__create_array(self.capacity)

    def __create_array(self, capacity):
        # Create a new referential array with the given capacity
        return (capacity * ctypes.py_object)()

    def __resize(self, new_capacity):
        new_array = self.__create_array(new_capacity)
        for i in range(self.size):
            new_array[i] = self.array[i]
        
        self.array = new_array # Replace the old array
        self.capacity = new_capacity

    def append(self, item):
        # Implement the append method
        if self.size == self.capacity:
            self.__resize(2*self.capacity)
        
        self.array[self.size]=item
        self.size += 1
        

    def __len__(self):
        # Implement the __len__ method
        return self.size

    def __str__(self):
        # Implement the __str__ method
        if self.size == 0:
            return '[]'
        output = ''
        for i in range(self.size):
            output += str(self.array[i]) + ', '
        return '[' + output[:-2] + ']'

    def pop(self):
        # Implement the pop method
        if self.size == 0:
            return 'Empty List, IndexError: pop from empty list'
        
        popped_item = self.array[self.size - 1]
        self.size -= 1
        return popped_item

    def __getitem__(self, index):
        # Implement the __getitem__ method
        if index>=0 and index<self.size:
            return self.array[index]
        else:
            return "Index Error: Invalid index"

    def clear(self):
        # Implement the clear method
        self.size=0

    def insert(self, position, element):
        # Implement the insert method
        if position < 0 or position > self.size:
            return 'Index Error: Invalid position'
        
        if self.size == self.capacity:
            self.__resize(2 * self.capacity)
        
        for index in range(self.size, position, -1):
            self.array[index] = self.array[index - 1]
        
        self.array[position] = element
        self.size += 1

    def remove(self, element):
        # Implement the remove method
        for i in range(self.size):
            if self.array[i] == element:
                for j in range(i, self.size - 1):
                    self.array[j] = self.array[j + 1]
                self.size -= 1
                return
        return 'Element not found'
            
            
# Example Usage
myList = CustomList()
myList.append(1)
myList.append(2)
myList.append(3)
myList.append(4)
print(myList)  # Expected Output: [1, 2, 3, 4]
myList.insert(1, 100)
print(myList)  # Expected Output: [1, 100, 2, 3, 4]
