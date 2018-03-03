"""cipher of Vigener"""

#alphabet
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m'
            ,'n','o','p','q','r','s','t','u','v','w','x','y','z']

def gen_matrix(matrix_size):
    """matrix_size X matrix_size matrix generator"""
    try:
        abet = alphabet * 2
        # slice index
        start = 0
        matrix = [0 for i in range(matrix_size)]
        for i in range(matrix_size):
            matrix[i] = abet[start:start + matrix_size]
            start = start + 1
        return matrix
    except Exception:
        return []

#generate alphabet matrix with size = alphabet length
matrix = gen_matrix(int(alphabet.__len__()))

def get_hash(message, key):
    """hash function"""
    try:
        # empty list for hash
        key_hash = []
        # index for iterate procedure
        count = 0
        for l in message:
            if l == ' ':
                key_hash.append(' ')
            else:
                if count < key.__len__():
                    key_hash.append(key[count])
                    count = count + 1
                else:
                    count = 0
                    key_hash.append(key[count])
                    count = count + 1
        return ''.join(key_hash)
    except Exception:
        return 'Only single-word keys and messages made of your alphabet ' \
               'lowercase letters and spaced by space symbol are allowed'

def confuse(message, key_hash):
    """function transforming input message to encoded one by hash generated with key and return it"""
    try:
        # empty list
        code = []
        for i in range(message.__len__()):
            if message[i] == ' ':
                code.append(' ')
            else:
                column = alphabet.index(message[i])
                row = alphabet.index(key_hash[i])
                code.append(matrix[column][row])
        return code
    except Exception:
        return 'Only single-word keys and messages made of your alphabet ' \
               'lowercase letters and spaced by space symbol are allowed'

def deconfuse(coded_message, key_hash):
    """function transforming input code to decoded one by hash generated with key and return it"""
    try:
        code = []
        for i in range(key_hash.__len__()):
            if key_hash[i] == ' ':
                code.append(' ')
            else:
                column = alphabet.index(key_hash[i])
                row_index = 0
                for row in matrix:
                    if row[column] == coded_message[i]:
                        code.append(row[0])
        return code
    except Exception:
        return 'Only single-word keys and messages made of your alphabet ' \
               'lowercase letters and spaced by space symbol are allowed'

def encode_mes(message, key):
    """encoding function that receives message, key string and returns encoded message"""
    #message hashed by key
    # get key_hash
    key_hash = get_hash(message, key)
    # encode message
    code = confuse(message, ''.join(key_hash))
    return ''.join(code)

def decode_mes(code, key):
    """decoding function that receives code, key string and returns decoded message"""
    key_hash = get_hash(code, key)
    decoded_mes = deconfuse(code, key_hash)
    return ''.join(decoded_mes)

def print_matrix():
    """print out alphabet matrix"""
    try:
        for i in matrix:
            print(' '.join(i))
    except Exception:
        print("matrix is empty")

def test_vigener(message, key):
    """test telemetry function"""
    code = encode_mes(message, key)
    print()
    print('INPUT: =>')
    print('message: ' + str(message))
    print('key: ' + str(key))
    print('<= END')
    print()
    print('OUTPUT: =>')
    print('key_hash: ' + str(get_hash(message, key)))
    print('code: ' + str(encode_mes(message, key)))
    print('<= END')
    print()
    print('DECODE: =>')
    print('code: ' + str(encode_mes(message, key)))
    print('key: ' + str(key))
    print('decode:' + str(decode_mes(encode_mes(message, key),key)))
    print('<= END')
    print()
    if str(decode_mes(encode_mes(message, key),key)) == message:
        print('Result: Encryption works fine')
    else:
        print('Result: Encryption failed')
