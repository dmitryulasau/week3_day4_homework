# Given an array nums, write a function 
# to move all zeroes to the end of it 
# while maintaining the relative order of the non-zero elements.

array1 = [0, 1, 0, 3, 12] # -> [1, 3, 12, 0, 0]
array2 = [1, 7, 0, 0, 8, 0, 10, 12, 0, 4] # -> [1, 7, 8, 10, 12, 4, 0, 0, 0, 0]

def zeros_end(list):
    """Put every zero in a list to the end of the list"""
    zeros_temp = []

    while 0 in list:
        for index, element in enumerate(list):
            if element == 0:
                zeros_temp.append(list.pop(index))

    return list + zeros_temp

