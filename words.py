def print_upper_words(word_list, letter):



    for word in words:
        if word.lower().startswith(letter.lower()):
            print(word.upper())


words = ["Cow","monkey","cat","bird","elephant"]
print_upper_words(words,"c")
