class Node:
    def __init__(self,data=None,next=None):
     self.data=data
     self.next=next

    def __str__(self):
     return str(self.data)


node1=Node(1)
node2=Node(2)
node3=Node(3)
node4=Node(4)
node1.next=node2
node2.next=node3
node3.next=node4

def print_list(node):
     while node is not None:
      print node,
      node=node.next

print_list(node1)