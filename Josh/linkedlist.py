class Node:
    def init(self, value):
        self.value = value
        self.next = None

# linked list must always know where it's head is

class LinkedList:
    def init(self):
        self.head = None

# using prepend to have a new head node
    def prepend(self, value):
      # no matter what we need to initialize the node
      new_node = Node(value)

      # if the list has no head, we just make this the head, and we are done
      if self.head == None:
        self.head = new_node
      # if the list has a head, we need to point the .next at the head
      else:
        # this points the .next for the new node at the current head
        new_node.next = self.head
        # we redifine the head to be our new prepended node, placing it at the beggining and pointing to the existing list
        self.head = new_node
      # then we need to move the head marker to the new node
      # if the list has no head, but a node in it, we make this the head, and then point the .next to the existing node
      # WE CANNOT CHANGE THE .NEXT ON THE EXISTING HEAD, IT WILL LOSE THE REST OF THE LIST

# start here!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!



#setting up methods for our linked list class
    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            print("head node created:", self.head.value)
            return


        node = self.head
        while node.next is not None:
            node = node.next

        node.next = new_node
        print("Appended new Node with value:", node.next.value)



llist = LinkedList()
llist.append("First Node")
llist.append("Second Node")
llist.append("Third Node")
llist.append("Fourth Node")