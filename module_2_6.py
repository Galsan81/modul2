def single_root_words(root_word, *other_words):
    same_words = []
    print(type(other_words))
    ad = list(other_words)
    print(type(ad))
    for i in ad:
        md = str(i)
        sl = root_word.lower()
        sl2 = md.lower()
        if sl in sl2:
            same_words.append(i)
            continue
    return same_words


print(single_root_words('rich', 'richiest', 'oRichalcum', 'cheers', 'riChies'))
