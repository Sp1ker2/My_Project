class Node (object):
    def __init__(self,data=None,next=None):
        self.data = data
        self.next= next
        # методи
    def get_data(self):
        return self.data
    def get_next(self):
        return  self.next
    def set_data(self,data):
        self.data = data
    def set_next(self,next):
        self.next = next
