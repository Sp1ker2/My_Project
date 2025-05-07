from node import Node


class LinkedList(object):
    def __init__(self):
        self.head = None
# добавление с начачла
    def append(self, data):
        new_node = Node(data)
        cur_node = self.head
        if cur_node == None:
            self.head = new_node
            return
        while cur_node.get_next() != None:
            cur_node = cur_node.get_next()
        cur_node.set_next(new_node)

    def show(self):
        cur_node = self.head
        output = ''
        while cur_node != None:
            output += str(cur_node.get_data()) + "->"
            cur_node = cur_node.get_next()
        print(output)
    #     вивод
    def lenght(self):
        cur_node = self.head
        count = 0
        while cur_node != None:
            count+=1
            cur_node=cur_node.get_next()
        print(count)
    #     длина
    def push_front(self,data):
        new_node=Node(data)
        cur_node = self.head
        new_node.set_next(cur_node)
        self.head=new_node
# добавление в конец

    def insert(self,index,data):
        new_node =Node(data)
        cur_node = self.head
        count = 0
        while cur_node.get_next()!=None:
            if index == 0:
                self.push_front(data)
                return
            elif count +1 == index:
                after_cur_node = cur_node.get_next()
                cur_node.set_next(new_node)
                new_node.set_next(after_cur_node)
                return
            count+=1
            cur_node= cur_node.get_next()