def isPalindrome(s: str) -> bool:
    import string
    check = [i.lower() for i in s if i !=" " and i not in string.punctuation]

    print(check)
    return ''.join(check) == ''.join(check)[::-1]

print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("race a car"))