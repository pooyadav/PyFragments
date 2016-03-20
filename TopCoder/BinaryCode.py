class BinaryCode:
    def decode(self, message):
        codelist = map(int, list(message));
        resultdict = {}

        option = [0, 1]
        for head in option:
            plaintx = self.decipher(head, codelist)
            if self.test(plaintx) == False :
                #print plaintx
                resultdict[head] = 'NONE'
            else :
                resultdict[head] = ''.join(str(x) for x in plaintx[:-1])

        result = []
        result.append(resultdict[0])
        result.append(resultdict[1])

        return tuple(result)

    def decipher(self, head, cipher):
        lenx = len(cipher)
        #cipher.insert(0, 0)
        plain = [0]*(lenx+2)
        plain[1] = head
        
        for i in range(1, lenx+1):
            plain[i+1] = cipher[i-1] - plain[i] - plain[i-1]
    
        return plain[1:]

    def test(self, plain):
        if plain[-1] != 0 :
            return False
        if min(plain) < 0 or max(plain) > 1 :
            return False
        return True
