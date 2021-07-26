# check first value against its neighbor, if it is lower than its neighbor, 
# move it left until it is either the lowest number or only higher than the number to its immediate left
# starting with the next value (index), repeat the process until entire list is sorted


def insertion_sort(list):
    for i in range(1, len(list)):
        value_to_sort = list[i]
        
        while list[i-1] > value_to_sort and i > 0:
            list[i-1], list[i] = list[i], list[i-1]
            i -= 1
    return list


test = [1, 4, 3, 0, 9, 2, 7]

insertion_sort(test)