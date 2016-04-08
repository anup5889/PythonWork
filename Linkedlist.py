class Linkedlist(object):

    """ this class will have the following methods for the linkedlist
    1. __init__ will set a head node
    2. insert
    3. size
    4. delete
    5. search
    """
def __init__(self, head=None):
    self.head=head


def insert(self, data):
    new_node=Node1(data)
    new_node.self_next(self.head)
    self.head=new_node


def size(self):
    current=self.head
    count=0
    while current:
        count+=1
        current=current.get_next()
    return count

def search(self, data):
    current=self.head
    found=False
    while current and found is False:
        if(current.get_data()==data):
            found=True
        else:
            current=current.get_next()
    if current is None:
        raise ValueError("Data not found")
    return current

def delete(self, data):
    current=current.head
    found=False

    while current and found is False:
        if current.get_data()==data:
            found=True
        else:
            previous=current
            current=current.get_next()
    if current is None:
        raise ValueError("Data Not found")
    if previous is None:
        self.head=current.get_next()
    else:
        previous.set_next(current.get_next())

        
            
    
    
