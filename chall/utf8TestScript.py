from time import sleep

def isUTF8ReacableUserInput(st, base, verbosity = 1):
    addr = 0
    for i in st.split(' '):
        tmpAddr = int(i, int(base))
        if tmpAddr > 255:
            raise ValueError("One byte cannot be larger than 255")
        addr = addr * 256 + int(i)
    print(hex(addr))
    return isUTF8Reacable(addr, verbosity)

def isUTF8Reacable(addr, verbosity = 1):
    prevByte = None
    while addr != 0:
        byte = addr & 0xff
        prevByte = {"byte": byte, "nextByte": prevByte}
        addr = addr >> 8
    prestartedBytes, ultimateTrailingBytes, result = isUTF8ReacableRec(prevByte, -1, 0, verbosity)
    charArray = []
    if prestartedBytes != 0:
        if prestartedBytes == 1:
            startChar = 0b11000010
        elif prestartedBytes == 2:
            startChar = 0b11100010
        elif prestartedBytes == 3:
            startChar = 0b11110010
        else:
            return ([], False)
        charArray += [startChar]
    while prevByte != None:
        charArray += [prevByte['byte']]
        prevByte = prevByte['nextByte']
    if ultimateTrailingBytes != 0:
        if ultimateTrailingBytes == 1:
            endChars = [0b10000000]
        elif ultimateTrailingBytes == 2:
            endChars = [0b10100000,0b10000000]
        elif ultimateTrailingBytes == 3:
            endChars = [0b10010000,0b10000000,0b10000001]
        else:
            return ([], False)
        charArray += endChars
    return charArray, result

def isUTF8ReacableRec(inputByte, trailBytesLeft, prestartedBytes, verbosity = 1):
    byte = inputByte["byte"]
    if verbosity: 
        print('Byte:', hex(byte), '| UTF-8 trail bytes left:', trailBytesLeft)
    if trailBytesLeft > 0: # Writing UTF-8 trailing bytes
        if byte >= 0b10000000 and byte < 0b11000000:
            trailBytesLeft -= 1
            if verbosity:
                print('Trailing byte allowed inside UTF-8 char')
        else:
            if verbosity:
                print('Error: Non-trailing byte not allowed inside UTF-8 char')
            return (prestartedBytes, trailBytesLeft, False)
    else: # Writing new UTF-8 number
        if 0b11000000 <= byte <= 0b11000001:
            if verbosity:
                print('Error: UTF-8 spec disallow 0xC0 and 0xC1 as start byte')
            return (prestartedBytes, trailBytesLeft, False)
        elif 0b11000010 <= byte <= 0b11110100: # Starting non-ASCII number A0 = 1010 0000
            binaryString = "{0:b}".format(byte)
            trailBytesLeft = -1
            for char in binaryString:
                if char == '1':
                    trailBytesLeft += 1
                else:
                    break
            if verbosity: 
                print('Starting new UTF-8 char with', trailBytesLeft, 'bytes')
        elif 0b11110101 <= byte <= 0b11111111:
            if verbosity: 
                print('Error: UTF-8 spec disallow 0xF5 through 0xFF as start byte')
            return (prestartedBytes, trailBytesLeft, False)
        elif byte < 0b10000000: # Writing ASCII number
            trailBytesLeft = 0
            if verbosity: 
                print('ASCII byte allowed outside UTF-8 char')
        else: # Met trailing byte
            if trailBytesLeft == 0:
                if verbosity:
                    print('Error: Trailing byte found outside UTF-8 char')
                return (prestartedBytes, trailBytesLeft, False)
            if verbosity: 
                print('Trailing byte allowed in prestarted UTF-8 char')
            prestartedBytes += 1
    nextByte = inputByte["nextByte"]
    if nextByte == None:
        return (prestartedBytes, trailBytesLeft, True)
    return isUTF8ReacableRec(nextByte, trailBytesLeft, prestartedBytes, verbosity)

if __name__ == "__main__":
    print("Enter ropper output to test:")
    x = input()
    sleep(0.1)
    print()
    print()
    print('valid addresses:')
    while(x != '\n'):
        addr = x.split(':')[0]
        arr, res = isUTF8Reacable(int(addr, 16), 0)
        if res:
            print(str(addr)+ ':', arr)
        x = input()
    