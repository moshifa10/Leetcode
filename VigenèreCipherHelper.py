class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.key = key
        self.plain_text = alphabet
        self.alphabets = "abcdefghijklmnopqurstuvwxyz"
        print(len(self.alphabets))
    
    def encode(self, text):
        pass
    
    def decode(self, text):
        pass


s = VigenereCipher(key=2,alphabet="da" )
