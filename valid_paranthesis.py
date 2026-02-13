def isValid(s: str) -> bool:
        stack = []
        valid = {
            "(": ")",
            "[": "]",
            "{": "}"
            }
        v = "{}()[]"
        # print(v)
        for i in s:
            if s.count(i) == len(s):
                return False
        if len(s) < 2:
            return False
        for i in range(len(s)):
            idx = v.index(s[i])
            if idx % 2 == 0:
                stack.insert(0, s[i])
            elif idx % 2 != 0 and len(stack) == 0:
                return False
            else:
                if stack[0] == v[idx-1]:
                    stack.pop(0)
                else:
                    return False
        return True if len(stack) == 0 else False



# print(isValid("()[]{}"))
# print(isValid("(]"))
# print(isValid("([)]"))
# print(isValid("){"))
print(isValid("(){}}{"))