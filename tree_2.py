class TreeNode:
    def __init__(self,data):
        self.data=data
        self.child=[]
        self.parent=None
        
    def add_child(self,child):
        child.parent=self
        self.child.append(child)

    def get_level(self):
        level=0
        p=self.parent
        while p:
            level+=1
            p=p.parent

        return level

    def print_tree(self):
        spaces=' '* self.get_level()*3
        prefix= spaces + "|__" if self.parent else ""
        print(prefix+self.data)
        if self.child:
            for child in self.child:
                child.print_tree()
        

    
def build_product_tree():
    root = TreeNode("CEO")

    cto = TreeNode("CTO")
    ih=TreeNode("Infrastructure Head")
    ih.add_child(TreeNode("Cloud Manager"))
    ih.add_child(TreeNode("App Manager"))
    cto.add_child(ih)
    cto.add_child(TreeNode("Application Head"))

    hr=TreeNode("HR Head")
    hr.add_child(TreeNode("Recruitment Manager"))
    hr.add_child(TreeNode("Policy Manager"))
    root.add_child(cto)
    root.add_child(hr)
    root.print_tree()

if __name__=="__main__":
    build_product_tree()

