class BinarySearchTree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def add_child(self,data):
        if self.data == data:
            print(f"Data: {data} already present in BST.")
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

    def search(self,val):
        if self.data==val:
            return True

        if val<self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False


def build_tree(elements):
    root=BinarySearchTree(elements[0])

    for i in elements[1:]:
        root.add_child(i)


    return root


if __name__=="__main__":
    countries = ["India","Pakistan","Germany", "USA","China","India","UK","USA"]
    country_tree = build_tree(countries)

    print("UK is in the list? ", country_tree.search("UK"))
    print("Sweden is in the list? ", country_tree.search("Sweden"))
    print("In order traversal gives this sorted list:",country_tree.in_order_traversal())

    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    print("In order traversal gives this sorted list:",numbers_tree.in_order_traversal())