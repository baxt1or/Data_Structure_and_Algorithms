class Node:
    def __init__(self, val):
        self.val = val 
        self.next = None



class LinkedList:
    def __init__(self):
        self.head = None
    
    def display(self):
        
        temp = self.head

        while temp:
            print(temp.val, end=" -> ")
            temp = temp.next
        print("None")
    

    def insert(self, value):
        
        new_node = Node(val=value)

        if not self.head:
            self.head = new_node
            return
        
        last = self.head

        while last.next:
            last = last.next
        last.next = new_node

    def insert_at_beginning(self, value):
        new_node = Node(val=value)
        new_node.next = self.head
        self.head = new_node
    
    def get_middle_element(self):
        slow = fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.val
    
    def duplicates_check(self):
        current = self.head

        seen = set()

        while current:
            if current.val in seen:
                return True
            seen.add(current.val)
            current = current.next
        return False
    
    def delete(self, data):
        
        temp = self.head
       
        if temp and temp.val == data:
            self.head = temp.next
            temp = None
            return
        
        prev = None
        while temp and temp.val != data:
            prev = temp
            temp = temp.next
        
        if not temp:
            return
        
        prev.next = temp.next
        temp = None
    
    def access_data(self, data):
        current = self.head

        while current:
            if current.val == data:
                return current.val
            current = current.next
        return "No data found"
    
    def get_elements(self, data):

        current = self.head

        while current and current.val != data:
            current = current.next
        
        while current:
            print(current.val, end=" -> ")
            current = current.next

