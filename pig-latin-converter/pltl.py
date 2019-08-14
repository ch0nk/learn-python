## Pig Latin Translator:

def pig_latin_translator(word):

    first_letter = word[0]

    # check if vowel
    if first_letter in 'aeiou':
        pig_word = word + 'ay'
    else:
        pig_word = word[1:] + first_letter + 'ay'

    return pig_word

print(pig_latin_translator('Pete'))