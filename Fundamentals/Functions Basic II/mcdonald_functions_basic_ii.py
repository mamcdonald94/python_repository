# 1. Countdown - Create a function that accepts a number as an input.
# Return a new list that counts down by one, from the number
# (as the 0th element) down to 0 (as the last element)

def countdown(num):
    new_list = []
    for i in range(num):
        while num >= 0:
            new_list.append(num)
            num -= 1
        return new_list


print(countdown(5))

# 2. Print and Return - Create a function that will receive a list with two
# numbers. # Print the first value and return the second.


def print_and_return(lst):
    print(lst[0])
    return lst[1]


print(print_and_return([0, 1]))


# 3. First Plus Length - Create a function that accepts a list and returns the
# sum of the first value in the list plus the list's length.


def first_plus_length(lst):
    return lst[0] + len(lst)


print(first_plus_length([-2, 1, 3, 4, 5]))

# 4. Values Greater than Second - Write a function that accepts a list and
# creates a new list containing only the values from the original list that
# are greater than its 2nd value. Print how many values this is and then
# # return the new list. If the list has less than 2 elements,
# have the function return False


def values_greater_than_second(lst):
    new_lst = []
    if len(lst) < 2:
        return False
    else:
        for i in range(len(lst)):
            if lst[i] > lst[1]:
                new_lst.append(lst[i])
        return new_lst


print(values_greater_than_second([0, 1, 2, 3, 4, 5]))
print(values_greater_than_second([0]))


# 5. This Length, That Value - Write a function that accepts two
# integers as parameters: size and value. The function should create
# and return a list whose length is equal to the given size,
# and whose values are all the given value

def this_length_that_value(size, value):
    new_lst = []
    while len(new_lst) < size:
        new_lst.append(value)
    return new_lst


print(this_length_that_value(6, 3))
