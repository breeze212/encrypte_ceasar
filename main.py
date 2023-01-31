print(ord('А'))
print(ord('Я'))
print(ord('а'))
print(ord('я'))
print(ord(','))
print(ord('a'))
print(ord('z'))
print(ord('A'))
print(ord('Z'))
const_upper_en = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
const_lower_en = 'abcdefghijklmnopqrstuvwxyz'

def encryption_text(text, shift):
    result = ''
    for i in text:
        ord_i = ord(i)
        if i in ',./!?;: ':
            encry = ord_i
        else:
            encry = ord_i + shift
        if i.isupper() and encry >= 122 or (i.islower() and encry <= 200):
            encry -= 26
        elif i.isupper() and encry > 1071 or (i.islower() and encry > 1103):
            encry -= 32
        result += chr(encry)
    return result


def input_text():
    text = input('Введите ваш текст: ')
    shift = int(input('Введите сдвиг вправо: '))
    print(encryption_text(text, shift))


input_text()
