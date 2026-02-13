def isHappy( n: int) -> bool:
        
        if n < 0:
            return False
        seen = [n]
        

        while n > 1:
            mapping = sum(map(lambda x: int(int(x)**2), list(str(n))))
            print(mapping)
            # come =  ''.join(str(mapping))
            # print(come)
            n = mapping
            if n in seen:
                return False
            seen.append(n)

        return True

if __name__ == '__main__':
    isHappy()