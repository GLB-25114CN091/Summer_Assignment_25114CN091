from collections import Counter

def common_chars(strings):
    common = Counter(strings[0])
    for s in strings[1:]:
        common &= Counter(s)
    return list(common.elements())

print(common_chars(["bella", "label", "roller"]))
