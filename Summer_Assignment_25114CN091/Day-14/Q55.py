def second_largest(arr):
    unique_nums = list(set(arr))
    if len(unique_nums) < 2:
        return None
    unique_nums.sort(reverse=True)
    return unique_nums[1]

arr = [10, 20, 4, 45, 99, 99]
print("Second largest element:", second_largest(arr))
