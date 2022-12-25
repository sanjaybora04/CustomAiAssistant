import nltk
nltk.download('punkt')
from nltk import word_tokenize
from nltk.stem.porter import PorterStemmer
import numpy as np

# nltk.download('punkt')
stemmer = PorterStemmer()


def tokenize(sentence):
    # Converting sentence into number of words (tokens)
    # sentence: 'May Force Be With You!'
    # token: ['May', 'Force', 'Be', 'With', 'You', '!']
    return word_tokenize(sentence)


def stem(word):
    # concept -  stemming
    # Generating the root form of the words.
    # words: ["organize", "organizes", "organizing"]
    # stemmed_words: ['organ', 'organ', 'organ']
    return stemmer.stem(word.lower())


def bag_of_words(tokenized_sentence, all_words):
    """
    sentence = ["hello", "how", "are", "you"]
    words = ["hi", "hello", "I", "you", "bye", "thank", "cool"]
    bag =   [0,     1,      0,     1,     0,      0,       0]
    """
    tokenized_sentence = [stem(w) for w in tokenized_sentence]
    bag = np.zeros(len(all_words), dtype=np.float32)
    for idx, w in enumerate(all_words):
        if w in tokenized_sentence:
            bag[idx] = 1.0

    return bag
