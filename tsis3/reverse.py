def reverse_sentence(sentence):
    # Split the sentence into a list of words
    words = sentence.split()

    # Reverse the order of the words
    words.reverse()

    # Join the words back into a sentence
    reversed_sentence = ' '.join(words)

    return reversed_sentence
