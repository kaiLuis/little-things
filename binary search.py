def is_in(arry, target):
    '''this is used for a binary search algorithm'''
    new_array = arry
    while len(new_array) > 1:
        if new_array[len(new_array)//2] > target:
            new_array = new_array[:len(new_array)//2]
        elif new_array[len(new_array)//2] < target:
            new_array = new_array[len(new_array)//2:]
        elif new_array[len(new_array)//2] == target:
            return True
            break
    if new_array[0] == target:
        return True
    else:
        return False



practice = list(range(0,600))
print(is_in(practice, 555))
    