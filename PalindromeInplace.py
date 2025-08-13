def palindrome(a):
    a = list(a.lower())
    left, right = 0, len(a) - 1
    while left < right:
        if a[left] != a[right]:
            return(False)
        left += 1
        right -= 1

    else:
        return(True)

print(palindrome("madam"))