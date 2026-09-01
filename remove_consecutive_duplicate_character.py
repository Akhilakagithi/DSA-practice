def remove_consecutive_duplicates(text):
    r = text[0]

    for i in range(1, len(text)):
        if text[i] != text[i-1]:
            r = r + text[i]

    return r
