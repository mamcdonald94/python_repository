# given a list of numbers, sort them from smallest to largest

def selection_sort(list):
    for i in range(len(list)-1):
        min_index = i
        for j in range(i, len(list)):
            if list[j] < list[min_index]:
                min_index = j

        list[min_index], list[i] = list[i], list[min_index]

    return list

list_one = [2, 5, 3, 1, 4, 6, 8, 0, 9]

print(selection_sort(list_one))
