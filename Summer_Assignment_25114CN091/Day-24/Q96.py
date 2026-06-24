def remove_duplicates(s):
    seen, result = set(), []
    for ch in s:
        if ch not in seen:
            seen.add(ch)
            result.append(ch)
    return ''.join(result)


print(remove_duplicates("programming"))  
