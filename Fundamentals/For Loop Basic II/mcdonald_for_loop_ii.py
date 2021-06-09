# 1. Biggie Size - Given a list, write a function that changes all positive
# numbers in the list to "big".


def biggie_size(lst):
    for i in range(len(lst)):
        if lst[i] > 0:
            lst[i] = "big"
    return lst

print(biggie_size([-1, 3, -4, 5, 6, -2]))


# 2. Count Positives - Given a list of numbers, create a function to replace
# the last value with the number of positive values.


def count_positives(lst):
    count = 0
    for i in range(len(lst)):
        if lst[i] > 0:
            count += 1
    lst[-1] = count
    return lst

print(count_positives([-1, 3, -4, 5, 6, 2]))


# 3. Sum Total - Create a function that takes a list and returns the sum of
# all the values in the array.


def sum_total(lst):
    sum = 0
    for x in lst:
        sum += x
    return sum


print(sum_total([2, 4, 1, 6, 3]))


# 4. Average - Create a function that takes a list and returns
# the average of all the values.


def average(lst):
    sum = 0
    for x in lst:
        sum += x
    return sum / len(lst)


print(average([2, 4, 1, 6, 3]))

# 5. Length - Create a function that takes a list
# and returns the length of the list.


def length(lst):
    return len(lst)


print(length([]))


# 6. Minimum - Create a function that takes a list of numbers and returns the
# minimum value in the list. If the list is empty, have the function return False.


def minimum(lst):
    if len(lst) == 0:
        return False
    else:
        min = lst[0]
        for x in lst:
            if x < min:
                min = x
        return min


print(minimum([1, 2, 3, 4]))

# 7. Maximum - Create a function that takes a list and returns the maximum
# value in the array. If the list is empty, have the function return False.

def maximum(lst):
    if len(lst) == 0:
        return False
    else:
        max = lst[0]
        for x in lst:
            if x > max:
                max = x
        return max


print(maximum([1, 0, 3, 4]))


# 8. Ultimate Analysis - Create a function that takes a list and returns a
# dictionary that has the sumTotal, average, minimum,
# maximum and length of the list.

def ultimate_analysis(lst):
    keys = ['sumTotal', 'average', 'minimum', 'maximum', 'length']
    values = [sum_total(lst), average(lst), minimum(lst), maximum(lst), len(lst)]
    new_dict = dict(zip(keys, values))
    return new_dict


print(ultimate_analysis([1, 0, 3, 4]))


# 9. Reverse List - Create a function that takes a list and return that list
# with values reversed. Do this without creating a second list.

def reverse_lst(lst):
    lst = lst[::-1]
    return lst

print(reverse_lst([1, 2, 3, 4]))

