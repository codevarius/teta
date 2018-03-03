"""cipher of Caesar"""


#alphabet list
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def confuse(letter, key):
    """function that returns a letter located through key indices from the letter passed as an argument"""
    count = 0
    for l in alphabet:
        if letter == l:
            if count + key > alphabet.__len__() - 1:
                count = count + key - alphabet.__len__()
                return alphabet[count]
            else:
                return alphabet[count + key]
        count = count + 1

def encode(message, key):
    """function returning a string encrypted by Caesar's code"""
    if key <= alphabet.__len__() and key >= -alphabet.__len__():
        try:
            box = []
            for letter in message:
                if letter == ' ':
                    box.append(' ')
                else:
                    box.append(confuse(letter, key))
            return ''.join(box)
        except Exception:
            return 'Only words made of lowercase letters are allowed'
    else:
        return 'Encode error: key value must be in range from -26 to 26'

def caesar(message):
    """If he had anything confidential to say, he wrote it in cipher, that is, by so
    changing the order of the letters of the alphabet, that not a word could be made out.
    If anyone wishes to decipher these, and get at their meaning, he must substitute the fourth
    letter of the alphabet, namely D, for A, and so with the others..."""
    key = 3
    try:
        box = []
        for letter in message:
            if letter == ' ':
                box.append(' ')
            else:
                box.append(confuse(letter, key))
        return ''.join(box)
    except Exception:
        return 'Only words made of lowercase letters are allowed'
