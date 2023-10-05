def main():
    message = input("Введите сообщение для дешифровки: ")
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
            if ord('а') <= ord(c) - shift:
                print(chr(ord(c) - shift), end='')
            else:
                print(chr(ord('я') - shift + (ord(c) - ord('а')) + 1), end='')
        elif c.isupper():
            if ord('А') <= ord(c) - shift:
                print(chr(ord(c) - shift), end='')
            else:
                print(chr(ord('Я') - shift + (ord(c) - ord('А')) + 1), end='')
        else:
            print(c, end='')



if __name__ == "__main__": main()