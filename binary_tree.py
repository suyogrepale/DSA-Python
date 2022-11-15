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

    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements

    def pre_order_traversal(self):
        elements = [self.data]
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()

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

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data + left_sum + right_sum


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


    numbers = [15,12,7,14,27,20,23,88 ]

    numbers_tree = build_tree(numbers)
    print("")
    print("Input numbers:",numbers)
    print("Min:",numbers_tree.find_min())
    print("Max:",numbers_tree.find_max())
    print("Sum:", numbers_tree.calculate_sum())
    print("In order traversal:", numbers_tree.in_order_traversal())
    print("Pre order traversal:", numbers_tree.pre_order_traversal())
    print("Post order traversal:", numbers_tree.post_order_traversal())