class VigenereCipher(object):
    def __init__(self, key: str, alphabet: str):
        self.key = key
        self.alphabet = alphabet

    def encode(self, text):
        result = []
        for i, char in enumerate(text):
            if char in self.alphabet:
                # Use i to keep the key aligned with the full text length
                shift = self.alphabet.index(self.key[i % len(self.key)])
                char_index = self.alphabet.index(char)
                
                new_index = (char_index + shift) % len(self.alphabet)
                result.append(self.alphabet[new_index])
            else:
                result.append(char)
        return ''.join(result)

    def decode(self, text):
        result = []
        for i, char in enumerate(text):
            if char in self.alphabet:
                # Use i to keep the key aligned with the full text length
                shift = self.alphabet.index(self.key[i % len(self.key)])
                char_index = self.alphabet.index(char)
                
                new_index = (char_index - shift) % len(self.alphabet)
                result.append(self.alphabet[new_index])
            else:
                result.append(char)
        return ''.join(result)


s = VigenereCipher(key="password",alphabet="abcdefghijklmnopqrstuvwxyz" )
# abc = "abcdefghijklmnopqrstuvwxyz"
# key = "password"


# ovnlqbpvt hznzeuz
# print(s.decode("rovwsoiv") )# rovwsoiv #codewars



print(s.encode('codewars'))#, 'rovwsoiv'
print(s.decode('rovwsoiv'))#, 'codewars'
print(s.encode('waffles'))#, 'laxxhsj'
print(s.decode('laxxhsj'))#, 'waffles'
print(s.encode('CODEWARS'))#, 'CODEWARS'
print(s.decode('CODEWARS'))#, 'CODEWARS'
print(s.encode(("it's a shift cipher!"))) # , "xt'k o vwixl qzswej!"