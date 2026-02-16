
class VigenereCipher(object):
    def __init__(self, key: str, alphabet: str):
        self.key = key
        self.alphabet = alphabet
        self.current_pos = 0
    
    def encode(self, text):
        # Go to key using current pos, Get the index from alpha and go back to the current pos of the letter and move it forward
        word: list = []
        for each_word in text:
            # print(each_word)
            # Now get the current index from alpha
            if each_word.isalpha():
                current_index = self.alphabet.index(self.key[self.current_pos])
                

                # Now get index of the word from the text and shift forward
                word_index = self.alphabet.index(each_word)
                total = word_index + current_index
                if total > 25 :
                    shift = abs((total - (len(self.alphabet)-1)) - 1)   
                    word.append(self.alphabet[shift])

                else:word.append(self.alphabet[total])

                self.current_pos += 1
            else:
                word.append(each_word)


        return ''.join(word)
        # print(word)

    def decode(self, text):
        pass


s = VigenereCipher(key="password",alphabet="abcdefghijklmnopqrstuvwxyz" )
abc = "abcdefghijklmnopqrstuvwxyz"
key = "password"


# ovnlqbpvt hznzeuz
s.encode("codewars") # rovwsoiv
