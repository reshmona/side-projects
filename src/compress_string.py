# a function compress_string(s) that performs basic string compression using the counts of repeated characters

def compress_string(s):
    if not s:
        return ""
    compressed = ""
    count = 1
    prev = s[0]
    for i in range(1, len(s)):
        if s[i] == prev:
            count += 1
        else:
            compressed += prev + str(count)
            prev = s[i]
            count = 1
    compressed += prev + str(count)
    #return s if compressed > s else compressed
    if len(compressed) >= len(s):
        return s
    else:
        return compressed
