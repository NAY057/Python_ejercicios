# -*- coding: utf-8 -*-

def binary_search(numbers, number_to_find, low, high):


    if low > high:
        return False

    mid = (low + high) / 2

    if numbers[mid] == number_to_find:
        return True
    elif numbers[mid] > number_to_find:
        return binary_search(numbers, number_to_find, low, mid - 1)
    else:
        return binary_search(numbers, number_to_find, mid + 1, high)



if __name__ == '__main__':
    
    numbers = [44,33,22,56,23,65,222,334,556,2342,1235,23423,12123,40,1, 3, 4, 5, 6, 9, 10, 11, 25, 27, 28, 34, 36, 49, 51]

    numbers.sort()


    print(numbers)

    number_to_find = int(raw_input('Ingresa un numero: '))

    result = binary_search(numbers, number_to_find, 0, len(numbers) - 1)

    if result is True:
        print('El numero si esta¡ en la lista.')
    else:
        print('El numero NO esta¡ en la lista.')