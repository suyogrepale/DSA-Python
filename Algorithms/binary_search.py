"""
Linear search has Time Complexity of Big O(n)

Binary Search works on Sorted List
Start from Middle of the Sorted list
Compare the element required with Middle element
Divide depending on value greater or less and repeat

Binary search has Time Complexity of Big Log(n)
"""
    

def linear_search(numbers_list,number_to_find):
    for index, element in enumerate(numbers_list):
        if element == number_to_find:
            return index
    return None

def binary_search(numbers_list,number_to_find):
    left_index = 0
    right_index = len(numbers_list)-1
    mid_index = 0

    while(left_index<=right_index):
        mid_index = (left_index + right_index )//2
        mid_number= numbers_list[mid_index]

        if mid_number==number_to_find:
            return mid_index

        if mid_number < number_to_find:
            left_index = mid_number+1

        else:
            right_index = mid_number-1

    return None

    
if __name__=="__main__":
    numbers_list = [15,12,7,14,27,20,23,88 ]
    numbers_list.sort()
    print(numbers_list)
    number_to_find=23

    index= linear_search(numbers_list,number_to_find)
    b_index = binary_search(numbers_list,number_to_find)

    print(f"Number found at index {index} using linear search")
    print(f"Number found at index {b_index} using Binary search")


