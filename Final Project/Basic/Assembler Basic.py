
def assemble(filename):
    lineCounter = 0
    newdict = {'add':'00000', 'and':'00001', 'or':'00010', 'sub':'00011', 'addi':'10000', 'andi':'10010',
               'ori':'10010', 'subi':'10011', 's0':'000', 's1':'001', 's2':'010', 's3':'011',
               's4':'100',  's5':'101', 's6':'110', 's7':'111', 'lw':'11000', 'sw':'10100'}
    newfile = open(filename,'r')
    
    hexstring = ""
    hexstring += "v2.0 raw"
    hexstring += '\n'

    for line in newfile.readlines():
        if line == '\n':
            
            
        else:
            
            binarystring = ""
            lineCounter += 1
            newline = line.strip('\n')
            splitLine = newline.split(" ")
            
            
            for item in splitLine:
                
                if item in newdict:
                    binarystring += newdict[item]
                    
                elif is_number(item):
                    
                    binarystring += int2bs(item,3)
                   
                    
                else:
                    return ("not valid assembly at line " + str(lineCounter))
           
            newhex = hex(int(binarystring,2))
            hexstring += newhex[2:]
           
            
            hexstring +='\n'

        newHexFile = open('newHexFile.hex','w')
        newHexFile.write(hexstring)
    
                         
    
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False

    
    
def int2bs(s, n):
    """ Converts an integer string to a 2s complement binary string.

        Args: s = Integer string to convert.to 2s complement binary.
              n = Length of outputted binary string.
        
        Example Input: stpd("4", 4)
        Example Output: "0100"

        Example Input: stpd("-3", 16)
        Example Output: "1111111111111101" """
    x = int(s)                              # Convert string to integer, store in x.
    if x >= 0:                              # If not negative, use python's binary converter and strip the "0b"
        ret = str(bin(x))[2:]
        return ("0"*(n-len(ret)) + ret)     # Pad with 0s to length.
    else:
        ret = 2**n - abs(x)                 # If negative, convert to 2s complement integer
        return bin(ret)[2:]                 # Convert to binary using python's binary converter and strip the "0b"




    
def bs2hex(v):
    """ Converts a binary string into hex.

        Args: v = Binary string to convert to hex

        Example Input: bs2hex("1010000010001111") 
        Example Output: "a08f" """
        
    ret = ""                                                            # Initialize ret string.
    bschunks = ["0b" + v[i*4:(i+1)*4] for i in range(0, len(v) / 4)]    # Chunk the binary string into groups of 4.
    for chunk in bschunks:                  
        ret += hex(int(chunk, 2))[2:]                                   #Convert each chunk to hex and strip the "0x"
    return ret   

def hexToBinary(stringOfHex):
    
    newInt = int(stringOfHex,16)

    num_of_bits = 32
    if stringOfHex != ' ':
        x = bin(newInt)[2:].zfill(num_of_bits)

        return x
    else:
        return ""
