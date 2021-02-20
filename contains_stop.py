
# this function is the clearest and fastest way I've tried that saves the bigrams which do not contain stopwords

def contains_stop(bigram, my_stop_words):
    if my_stop_words.intersection(bigram):
        return True
    else:
        return False