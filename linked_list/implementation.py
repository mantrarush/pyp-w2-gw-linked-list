from .interface import AbstractLinkedList
from .node import Node


class LinkedList(AbstractLinkedList):
    def __init__(self, elements=None):
        self.start = None
        self.end = None
        if elements:
            for element in elements:
                self.append(element)
            self.end.next = None
    
 
    def __str__(self):
        str_list =[]
        temp = self.start
        while temp is not None:
            str_list.append(temp.elem)
            temp = temp.next
        return str(str_list)

        
    def __len__(self):
        return self.count()
    
    def __iter__(self):
        temp = self.start
        while temp is not None:
            yield temp
            temp = temp.next
        raise StopIteration
    
    def __getitem__(self, index):
        current = self.start 
        counter = 0 
        if current is None:
            raise KeyError("No elements in the list")
        while current and counter < index:
            counter = counter+1
            current = current.next
        if counter is not 0 and current is None:
            raise KeyError("Out of range")
        return current.elem
            
    def __add__(self, other):
        temp = LinkedList()
        if self is not None:
            for x in self:
                temp.append(x.elem) 
        if other is not None:
            for x in other:
                temp.append(x.elem)    
        return temp
    
    def __iadd__(self, other):
        if other is None: 
            return self
        if self.start is not None and other.start is not None: 
            self.end.next = other.start   
        elif self.start is None:
            self.start = other.start
            self.end = other.end
        return self
    
    def __eq__(self, other):
        current1 = self.start 
        current2 = other.start 
       
        while current1 is not None and current2 is not None:
            if current1.elem != current2.elem:
                return False
            current1 = current1.next 
            current2 = current2.next 
        if current1 is None and current2 is not None:
            return False
        if current2 is None and current1 is not None:
            return False
        return True

    def append(self, elm):
        temp = Node(elm) 
        if self.start is None:
            self.start = temp
        else:
            self.end.next = temp 
        self.end = temp    
       
        
    def count(self):
        current = self.start 
        counter = 0  
        while current is not None:
            counter = counter+1
            current = current.next
        return counter
    
    def __ne__(self, other):
        return not self == other
    
    def pop(self, index=None):
        temp = self.start
        temp_elem = None
        counter = 0 
        size = self.count()
        
        if self.start is None: 
            raise IndexError("Nothing in the list")
        if index is None and size != 0:
            index = size-1 
        if size<=index:
            raise IndexError("index exceeds size")
        
    
        if index == 0: 
            temp_elem = self.start.elem
            self.start = self.start.next
            if size == 1:
               self.end = None  
        else:
            while temp and counter < index-1: 
                temp= temp.next
                counter = counter+1
                
            #when counter = index-1
            if temp.next is not None:
                temp_elem = temp.next.elem
                temp.next = temp.next.next
            else:
                temp_elem = temp.elem

        return temp_elem 
        
    ''' 
        temp = self.start 
        temp_elem = None
        counter = 0 
        size = self.count()
        print size 
        if self.start is None: 
            raise IndexError("Nothing in the list") 
        if index is None:
            index = size + 1 
        elif size<index:
            raise ("Invalid index")
            
        if index<2: 
            index = index+2
       
        while temp and counter < index: 
            if (counter == index-2):
                if temp.next is not None:
                    temp_elem = temp.next.elem 
                    temp.next = temp.next.next 
                     
                else:
                    temp_elem = temp.elem 
                    temp = None
                    counter = counter+1

        return temp_elem     
    '''         
    '''
        temp_elem = 0 
        if self.start is None:
            raise IndexError("List is empty")
        elif index is None:
            if self.start is not self.end:
                temp = self.start
                while temp.next is not self.end:
                    temp = temp.next
                temp_elem = temp.next.elem 
                self.end = temp
                
        if index is 0:
            temp_elem = self.start.elem
            self.start = self.start.next
        else:
            count = 0 
            temp = self.start
            while count < (index-1) and temp is not None and temp.next is not self.end:
                count = count+1
                temp = temp.next
            if temp.next is self.end and count is not index-2:
                raise IndexError("Index out of range")
            elif count is index-2:
                temp_elem = temp.next.elem 
                temp.next = temp.next.next
    
        return temp_elem        
'''