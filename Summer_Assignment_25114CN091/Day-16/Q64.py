def remove_duplicates(arr):
    return list(dict.fromkeys(arr))  # Preserves order

arr = [1, 2, 2, 3, 4, 4, 5]
print("Array without duplicates:", remove_duplicates(arr))
