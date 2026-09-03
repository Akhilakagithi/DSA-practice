def count_character_types(text):
    u_c = 0
    l_c = 0
    d_c = 0

    for i in text:
        if i.isupper():
            u_c += 1
        elif i.islower():
            l_c += 1
        elif i.isdigit():
            d_c += 1

    return u_c, l_c, d_c


text = input()

uppercase, lowercase, digits = count_character_types(text)

print(f"Uppercase: {uppercase}")
print(f"Lowercase: {lowercase}")
print(f"Digits: {digits}")
