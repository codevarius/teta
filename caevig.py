"""module to solve multiply (caesar & vigener) cipher encoding"""

#importing external libs
from ciph import caesar
from ciph import vigener

def encode(message, key):
    """encoding function"""
    try:
        encode_step1 = caesar.caesar(message)
        encode_step2 = vigener.encode_mes(encode_step1, key)
        return ''.join(encode_step2)
    except Exception:
        return 'Only single-word keys and messages made of your alphabet ' \
               'lowercase letters and spaced by space symbol are allowed'

def decode(code, key):
    """decoding function"""
    try:
        decode_step1 = vigener.decode_mes(code, key)
        decode_step2 = caesar.encode(decode_step1, -3)
        return ''.join(decode_step2)
    except Exception:
        return 'Only single-word keys and messages made of your alphabet ' \
               'lowercase letters and spaced by space symbol are allowed'

def test(message, key):
    """test telemetry function"""
    print()
    print('INPUT: =>')
    print('message: ' + str(message))
    print('key: ' + str(key))
    print('<= END')
    print()
    print('OUTPUT: =>')
    print('code: ' + str(encode(message, key)))
    print('<= END')
    print()
    print('DECODE: =>')
    print('decode:' + str(decode(encode(message, key), key)))
    print('<= END')
    print()
    if str(decode(encode(message, key), key)) == message:
        print('Result: Encryption works fine')
    else:
        print('Result: Encryption failed')
