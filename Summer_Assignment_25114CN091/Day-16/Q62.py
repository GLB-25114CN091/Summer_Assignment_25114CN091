from collections import Counter

def max_frequency_element(arr):
    freq = Counter(arr)
    element, count = freq.most_common(1)[0]
    return element, count

arr = [1, 3, 2, 3, 4, 3, 5]
element, count = max_frequency_element(arr)
print(f"Element with max frequency: {element} (Frequency: {count})")
