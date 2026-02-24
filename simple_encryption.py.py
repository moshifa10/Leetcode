


# # Simple Encryption #1 - Alternating Split

# encrypt("012345", 1)  =>  "135024"
# encrypt("012345", 2)  =>  "135024"  ->  "304152"
# encrypt("012345", 3)  =>  "135024"  ->  "304152"  ->  "012345"


def decrypt(encrypted_text, n):
    pass


def encrypt(text, n):
    c = 0
    while c != n:
        even = [text[i] for i in range(len(text)) if i %2==0]
        odd = [text[i] for i in range(len(text)) if not i %2==0]

        odd.extend(even)
        text = odd
        c +=1

    return ''.join(text)



print(encrypt("012345", 1))

