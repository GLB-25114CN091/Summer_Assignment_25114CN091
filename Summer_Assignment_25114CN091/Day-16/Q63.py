def find_pair_with_sum(arr, target):
    seen = set()
    for num in arr:
        if target - num in seen:
            return num, target - num
        seen.add(num)
    return None

arr = [2, 7, 11, 15]
target = 9
pair = find_pair_with_sum(arr, target)
print("Pair with sum", target, ":", pair)
