
class VigenereCipher(object):
    def __init__(self, key: str, alphabet: str):
        self.key = key
        self.alphabet = alphabet
        self.current_pos = 0
    
    def encode(self, text):
        self.current_pos = 0
        # Go to key using current pos, Get the index from alpha and go back to the current pos of the letter and move it forward
        word: list = []
        for each_word in text:
            # print(each_word)
            # Now get the current index from alpha
            if each_word.isalpha() and each_word in self.alphabet:
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
        self.current_pos = 0
        word: list = []

        for each_word in text:
            if each_word.isalpha() and each_word in self.alphabet:
                current_index_from_text = self.alphabet.index(each_word)
                current_index_from_alphabet = self.alphabet.index(self.key[self.current_pos])

                # print(f"key: {current_index_from_alphabet} \ttext:{current_index_from_text}" )
                # break
                total = (current_index_from_text - current_index_from_alphabet)
                # print(total)

                word.append(self.alphabet[total])

                self.current_pos += 1

            else: word.append(each_word)

        return "".join(word)


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