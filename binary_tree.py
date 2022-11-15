class BinarySearchTree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def add_child(self,data):
        if self.data == data:
            print("Data already present in BST.")
            return
        #add data in left subtree
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left=BinarySearchTree(data)

        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right=BinarySearchTree(data)
    
    def in_order_traversal(self):
        elements=[]

        #visit left tree
        if self.left:
            elements+=self.left.in_order_traversal()

        #visit root node
        elements.append(self.data)

        #visit right node
        if self.right:
            elements+=self.right.in_order_traversal()

        return elements


def build_tree(elements):
    root=BinarySearchTree(elements[0])

    for i in elements[1:]:
        root.add_child(i)


    return root


if __name__=="__main__":
    numbers=[70,78,65,52,99,91,88,23,98,35]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.in_order_traversal())