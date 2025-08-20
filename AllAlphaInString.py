def is_pangram_26bits(s):
    flag = 0
    for ch in s.lower():
        if 'a' <= ch <= 'z':
            flag |= 1 << (ord(ch) - ord('a'))

    return flag == (1 << 26)-1

print(is_pangram_26bits("The quick brown fox jumps over the lazy dog"))
print(is_pangram_26bits("Hello World"))
