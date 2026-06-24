 def compress_string(s):
    result, count = [], 1
    for i in range(1, len(s) + 1):
        if i < len(s) and s[i] == s[i - 1]:
            count += 1
        else:
            result.append(s[i - 1] + str(count))
            count = 1
    return ''.join(result)

print(compress_string("aaabbc"))  
