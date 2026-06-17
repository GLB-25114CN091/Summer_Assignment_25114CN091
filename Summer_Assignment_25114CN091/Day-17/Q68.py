def common_elements(*arrays):
    common = set(arrays[0])
    for arr in arrays[1:]:
        common &= set(arr)
    return list(common)

a = [1, 2, 3, 4]
b = [2, 3, 5]
c = [2, 3, 6]
print("Common Elements:", common_elements(a, b, c))
