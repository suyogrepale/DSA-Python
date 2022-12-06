def bubble_sort(elements):
    size=len(elements)

    for i in range(size-1):
        swapped = False
        for j in range(size-1-i):
            if(elements[j]>elements[j+1]):
                temp=elements[j]
                elements[j]=elements[j+1]
                elements[j+1]=temp
                swapped=True

        if not swapped:
            break




        





if __name__=="__main__":
    elements = [29,1,0,51,28,5,8,2]

    elements = ["mona", "dhaval", "aamir", "tina", "chang"]

    print(elements)
    bubble_sort(elements)
    print(elements)