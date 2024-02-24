class DoublyLinkedList:
    class Item:
        value = None
        next = None 
        last=None
        def __init__(self, value):
            self.value = value

    head:Item.next = None
    Last:Item.last = None
    
    def __len__(self):
        current = self.head
        ind = 0
        while current:
            current = current.next
            ind+=1
        return ind

    def append_begin(self, value):
        item = DoublyLinkedList.Item(value)
        item.next = self.head
        if self. head is None:
           self. Last=item
        self.head=item
        if self. head.next is not None:
            current=self.head.next
            current.last=item
            
    def append_end(self, value) :
        item = DoublyLinkedList.Item(value)
        if self. head is None:
            self. head=item
            self. Last=item
            return
        item. last=self. Last
        self. Last. next=item
        self. Last=item
    
    def append_by_index(self, index, value):
        item = DoublyLinkedList.Item(value)
        if index==0:
            item.next = self.head
            if self. head is None:
                self. Last=item
            self.head=item
            if self. head.next is not None:
                current=self.head.next
                current.last=item 
            return
        if self. head is None:
            raise ValueError("Элементов нет") 
        current=self.head
        for I in range(index-1) :
             current=current.next
             if current is None:
                 raise NameError("Error")             
        if current. next is not None:
            current.next.last=item
        else:
            self. Last=item
        item. last=current     
        item. next=current.next 
        current. next=item
        
    def remove_first(self):
        if self.head is None:
            raise NameError("Элементов нет")
        if self. head. next is None:
            self. head=None
            self. Last=None
            return
        self. head=self.head.next
        self. head. last=None
    
    def remove_last (self) :
        if self. head is None:
            raise NameError ("Элементов нет")
        if self. head. next is None:
            self. head=None
            self. Last=None
            return
        self. Last=self.Last.last
        self. Last. next=None
        
    def remove_at (self,index):
        if self. head is None:
            raise NameError ("Элементов нет") 
        if index==0:
            if self. head. next is None:
                self. head=None
                self. Last=None
                return
            self. head=self.head.next
            self. head. last=None
            return
        
        current=self.head
        for I in range(index-1) :
             current=current.next
             if current is None:
                 raise ValueError("Error")
        if current. next. next  is not None: 
            current.next=current.next.next
        else:
            current. next=None                  
            self. Last=current
            return
        current.next.last=current
        
    def remove_first_value (self,value):
        if self.head is None:
            raise ValueError("Элементов нет")
        if self.head.value == value:
            self.head = self.head.next
            self. Last=self.head.next
            return
        current=self.head
        perem = None
        while current:
                if current.next.value == value:
                    perem = current
                    current = current.next
                    break
                current = current.next
        if perem is not None:
            current. next. last=perem
            perem.next= current. next
        else:
            raise ValueError("Error")    
    
    def remove_last_value(self, value) :
        if self.head is None:
            raise ValueError("Элементов нет")
        if self.Last.value == value:
            self. Last=self.Last.last
            self. Last. next=None
            if self. Last. last is None:
                self.head = self. head. next
            return
        current=self.Last
        perem = None
        while current:
                if current.last.value == value:
                    perem = current
                    current = current.last
                    break
                current = current.last
        if perem is not None:
            current. last. next=perem
            perem.last= current. last
        else:
            raise ValueError("Error")