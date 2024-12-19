def single_root_words(root_word, *other_words):
    same_words = []

    for word in other_words:
        if root_word.lower() in word.lower():
            same_words.append(word)

    return same_words

root_word = "дом"

result1 = single_root_words(root_word, "дым", "домашний", "домовой", "сад")

result2 = single_root_words(root_word, "ПРИДОМОВОЙ", "Дом", "одомашненный", "Домовой")

print(result1)
print(result2)
