def list_divide(numbers, divide=2):
    elements = 0
    for number in numbers:
        if (number % divide == 0):
            elements = elements + 1
    return elements

print (list_divide([1, 2, 3, 4, 5]))
print (list_divide([2,4,6,8,10]))