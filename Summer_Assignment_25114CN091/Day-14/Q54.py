def frequency(arr, element):
    return arr.count(element)

arr = [1, 2, 2, 3, 4, 2, 5]
element = 2
print(f"Frequency of {element}:", frequency(arr, element))
