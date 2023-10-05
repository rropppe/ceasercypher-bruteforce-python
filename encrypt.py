def main():
    message = input("Введите сообщение для шифровки: ")
    shift = input("Введите сдвиг: ")
    try: shift = int(shift)
    except ValueError:
        print("Сдвиг должен являться целым числом > 0 и < {}".format(33))
        return
    if 0 > shift or shift >= 33:
        print("Сдвиг должен являться целым числом > 0 и < {}".format(33))
        return
    for c in message:
        if c.islower():
            if ord(c) <= ord('я') - shift:
                print(chr(ord(c) + shift), end='')
            else:
                print(chr(ord('а') + shift - (ord('я') - ord(c)) - 1), end='')
        elif c.isupper():
            if ord(c) <= ord('Я') - shift:
                print(chr(ord(c) + shift), end='')
            else:
                print(chr(ord('А') + shift - (ord('Я') - ord(c)) - 1), end='')
        else:
            print(c, end='')

if __name__ == "__main__": main()