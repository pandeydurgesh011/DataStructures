#Creating Node structure
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
#Creating class for all Linked List Operations
class Linked_List:

    def __init__(self):
        self.head = None

    #Adding node at start of the linked list
    def insert_start(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    #Adding node at the End of the Linked List
    def insert_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head

        while(last.next):
            last = last.next
        last.next = new_node

    #Adding node after a particular node
    def insert_after(self,data,prev_data):
        temp = self.head
        while(temp):
            if temp.data == prev_data:
                new_node = Node(data)
                new_node.next = temp.next
                temp.next = new_node
                return
            temp = temp.next
        print("element not added as prev_data not found")

    #Searching element in Linked List
    def search_ll(self,search_data):
        temp = self.head
        count = 1
        while(temp):
            if temp.data == search_data:
                print("Data",search_data, "found in Linked list at position ",count)
                return
            temp = temp.next
            count+=1
        print("Data",search_data, "was not found in Linked List")

    #Deleting Node from linked list
    def delete_node(self,data):
        if self.head.data == data:
            self.head = self.head.next
            return
        forward = self.head.next
        temp = self.head
        while(forward):
            if forward.data == data:
                temp.next = forward.next
                return
            forward = forward.next
            temp = temp.next

    #Printing LInked List   
    def print_ll(self):
        temp = self.head
        while(temp):
            print(temp.data," ",end="")
            temp = temp.next
        print()

    #Reversing the Linked list
    def reverse_ll(self):
        prev = None
        current = self.head
        next = current
        while (current):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

if __name__ == '__main__':
    
    ll = Linked_List()

    ll.insert_start(3)
    ll.insert_start(2)
    ll.insert_end(1)
    ll.print_ll() 
    ll.insert_after(2,5)
    ll.print_ll()
    ll.search_ll(1)
    ll.delete_node(3)
    ll.print_ll()
    ll.reverse_ll()
    print("reversed linked list")
    ll.print_ll()
