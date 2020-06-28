class BinaryTree:
    def __init__(self, key):
        self.key = key
        self.left_child = None
        self.right_child = None

    def insert_left(self, key):
        if self.left_child:
            new_node = BinaryTree(key)
            new_node.left_child = self.left_child
            self.left_child = new_node
        else:
            self.left_child = BinaryTree(key)
        return self.left_child

    def insert_right(self, key):
        if self.right_child:
            new_node = BinaryTree(key)
            new_node.right_child = self.right_child
            self.right_child = new_node
        else:
            self.right_child = BinaryTree(key)
        return self.right_child

    def get_right(self):
        return self.right_child

    def get_left(self):
        return self.left_child

    def set_key(self, key):
        self.key = key

    def get_key(self):
        return self.key

    def preorder(self):
        print(self.key)
        if self.left_child:
            self.left_child.preorder()
        if self.right_child:
            self.right_child.preorder()

    def inorder(self):
        if self.left_child:
            self.left_child.inorder()
        print(self.key)
        if self.right_child:
            self.right_child.inorder()

    def postorder(self):
        if self.left_child:
            self.left_child.inorder()
        if self.right_child:
            self.right_child.inorder()
        print(self.key)


a = BinaryTree('a')
b = a.insert_left('b')
c = a.insert_right('c')
d = b.insert_left('d')
e = b.insert_right('e')
f = c.insert_left('f')

# b = a.get_left()
# c = a.get_right()
# d = b.get_left()
# e = b.get_right()
# f = c.get_left()

# print(a.key)
# print(b.key)
# print(c.key)
# print(d.key)
# print(e.key)
# print(f.key)

a.preorder()
a.inorder()
a.postorder()
