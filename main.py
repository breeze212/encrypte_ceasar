def encryption_text(text, shift):
    result = ''
    for i in text:
        ord_i = ord(i)
        if i in ',./!?;:" ':
            encry = ord_i
        else:
            encry = ord_i + shift
        if i.isupper() and encry >= 90 and encry <= 200 or (i.islower() and encry > 122 and encry <= 300):
            encry -= 26
        elif i.isupper() and encry > 1071 or (i.islower() and encry > 1103):
            encry -= 32
        result += chr(encry)
    return result

def decryption_text(text, shift):
    result = ''
    for i in text:
        ord_i = ord(i)
        if i in ',./!?;: ':
            encry = ord_i
        else:
            encry = ord_i - shift
        if (i.isupper() and encry < 1040 and encry > 200) or (i.islower() and encry < 1072 and encry > 200):
            encry += 32
        elif i.isupper() and encry < 65 or (i.islower() and encry < 97):
            encry += 26
        result += chr(encry)
    return result


def input_text():
    text = input().split()
    punct = ',.!"'
    for i in text:
        counter = 0
        for j in range(len(i)):
            for symbol in range(len(punct)):
                if punct[symbol] in i[j]:
                    counter += 1
        length_encry = int(len(i)) - counter
        print(encryption_text(i, length_encry), end=' ')

input_text()
