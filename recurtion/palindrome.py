def palindrome(s):
    if len(s) < 2:
        return True

    if s[0]!=s[-1]:
        return False

    return palindrome(s[1:-1])


s = "racecar"
a =palindrome(s)
print(a)