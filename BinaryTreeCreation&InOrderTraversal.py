class Queue(object):
    def __init__(self):
        self.l = []
        self.index_to_pop = 0

    def add(self, data):
        self.l.append(data)

   
   def pop(self):
        if self.l and self.index_to_pop < len(self.l):
            temp = self.l[self.index_to_pop]
            self.index_to_pop += 1
            return temp
        else:
            return None

    def peek(self):
        if self.l and self.index_to_pop < len(self.l):
            return self.l[self.index_to_pop]
        else:
            return None


class Node(object):
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


class BinaryTree(object):
    def __init__(self):
        self.root = None
        self.queue = Queue()

    def add_data(self, data):
        node = Node(data)
        if self.root == None:
            self.root = node

        else:
            n = self.queue.peek()

            if n.left == None:
                n.left = node

            elif n.right == None:
                n.right = node
                self.queue.pop()

        self.queue.add(node)

    def pre_order(self):
        return self.pre_order_helper(self.root)

    def pre_order_helper(self, n):
        if n:
            print (n.data)
            self.pre_order_helper(n.left)
            self.pre_order_helper(n.right)


def create_tree():
    l = [1, 2, 3, 4, 5]

    bt = BinaryTree()
    for element in l:
        bt.add_data(element)

    bt.pre_order()
create_tree()
