__author__ = 'administrador'
# Vamos a realizar un ejercicio haciendo uso de metodos y variables

def break_words(stuff):
    """This function will break up words for us"""
    words = stuff.split(' ')
    return words

def sort_words (words):
    """Sorts the words"""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off"""
    word = words.pop(0)
    print word

def print_last_word(words):
    """Prints the last word after popping it off"""
    word = words.pop(-1)
    print word

def sort_sentence(sentence):
    """Takes in a full sentence a return the shorted words"""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Print the first and last word of a sentence"""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def first_and_last_sorted(sentence):
    """Shorts the words, then print the firts and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
