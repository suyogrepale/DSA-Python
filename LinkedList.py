class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None


    def insert_at_beginning(self,data):
        node=Node(data,self.head)
        self.head=node

    def print(self):
        if self.head is None:
            print("Linked List is empty.")
            return

        itr=self.head
        llstr=''
        while itr:
            llstr+=str(itr.data)+'-->'
            itr=itr.next

        print(llstr)

    def insert_at_end(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return

        itr = self.head
        while itr.next:
            itr=itr.next

        itr.next=Node(data,None)

    def insert_values(self,data_list):
        self.head=None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr=self.head
        while itr:
            count+=1
            itr=itr.next

        return count
    
    def remove_at(self,index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.head=self.head.next
            return

        count = 0
        itr= self.head
        while itr:
            if(count==index-1):
                itr.next=itr.next.next
                break
            itr = itr.next
            count+=1
    
    def insert_at(self,index,data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")
        if index ==0:
            self.insert_at_beginning(data)
            return

        count = 0
        itr = self.head
        while itr:
            if(count==index-1):
                itr.next=Node(data,itr.next)
                break
            itr = itr.next
            count+=1

    def insert_after_value(self,data_after,data_to_insert):
        
        found=0
        itr=self.head
        while itr:
            if(itr.data==data_after):
                itr.next=Node(data_to_insert,itr.next)
                found=1
                break
            itr=itr.next
            

        if(found==0):
            print(f"Data {data_after} not Found.")
    
    def remove_by_value(self,data):
        if(self.head.data==data):
            self.head=self.head.next
            return

        itr=self.head
        prev_itr=itr
        found=0
        while itr:
            if(itr.data==data):
                prev_itr.next=itr.next
                found=1
                break
            prev_itr=itr
            itr=itr.next
        if(found==0):
            print(f"Data {data} not Found.")




    
if __name__=="__main__":
    ll=LinkedList()
    ll.insert_at_beginning(5)
    ll.insert_at_beginning(88)
    ll.insert_at_beginning(90)
    ll.print()
    ll.insert_at_end(98)
    ll.insert_at_end(8)
    ll.print()

    l1=LinkedList()
    l1.insert_values(["banana","mango","Pineapple","gauva","apple"])
    l1.print()
    print("Length l1: ",l1.get_length())
    l1.remove_at(4)
    l1.print()
    print("Length l1: ",l1.get_length())
    l1.insert_at(0,"Figs")
    l1.insert_at(2,"JackFruit")
    l1.print()
    print("Length l1: ",l1.get_length())
    l1.insert_after_value("mango","Lichi")
    l1.print()
    l1.remove_by_value("mango")
    l1.print()
    