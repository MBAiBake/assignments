import math, os, pickle, re
from typing import Tuple, List, Dict


class BayesClassifier:
    """A simple BayesClassifier implementation

    Attributes:
        pos_freqs - dictionary of frequencies of positive words
        neg_freqs - dictionary of frequencies of negative words
        pos_filename - name of positive dictionary cache file
        neg_filename - name of positive dictionary cache file
        training_data_directory - relative path to training directory
        neg_file_prefix - prefix of negative reviews
        pos_file_prefix - prefix of positive reviews
    """

    def __init__(self):
        """Constructor initializes and trains the Naive Bayes Sentiment Classifier. If a
        pickled version of a trained classifier is stored in the current folder it is loaded,
        otherwise the system will proceed through training.  Once constructed the
        classifier is ready to classify input text."""
        # initialize attributes
        self.pos_freqs: Dict[str, int] = {}
        self.neg_freqs: Dict[str, int] = {}
        self.pos_filename: str = "pos.dat"
        self.neg_filename: str = "neg.dat"
        self.training_data_directory: str = "movie_reviews/"
        self.neg_file_prefix: str = "movies-1"
        self.pos_file_prefix: str = "movies-5"

        self.total_pos_reviews = 11129
        self.total_neg_reviews = 2735

        # check if both cached classifiers exist within the current directory
        if os.path.isfile(self.pos_filename) and os.path.isfile(self.neg_filename):
            print("Data files found - loading to use pickled values...")
            self.pos_freqs = self.load_dict(self.pos_filename)
            self.neg_freqs = self.load_dict(self.neg_filename)
        else:
            print("Data files not found - running training...")
            self.train()

    def train(self) -> None:
        """Trains the Naive Bayes Sentiment Classifier

        Train here means generates 'self.pos_freqs' and 'self.neg_freqs' dictionaries with frequencies of
        words in corresponding positive/negative reviews
        """
        files: List[str] = next(os.walk(self.training_data_directory))[2]
        for index, filename in enumerate(files, 1):
              print(f"Training on file {index} of {len(files)}")
              text = self.load_file(os.path.join(self.training_data_directory, filename))
              neg = '1'
              pos = '5'
              lst_words = self.tokenize(text)
              if filename[7] == neg:
                  self.update_dict(lst_words,self.neg_freqs)
              elif filename[7] == pos:
                  self.update_dict(lst_words,self.pos_freqs)
              else:
                  continue

    def classify(self, text: str) -> str:

        lst_words = self.tokenize(text)
        pos = 0
        neg = 0
        total_pos = 0
        total_neg = 0
        pos_values = self.pos_freqs.values()
        neg_values = self.neg_freqs.values()

        for word in lst_words:
            if word in self.pos_freqs:
                pos = (self.pos_freqs[word] + 1) / self.total_pos_reviews
                total_pos += math.log(pos)
            else:
                pos = 1 / self.total_pos_reviews
                total_pos += math.log(pos)
            if word in self.neg_freqs:
                neg = (self.neg_freqs[word] + 1) / self.total_neg_reviews
                total_neg += math.log(neg)
            else:
                neg = 1 / self.total_neg_reviews
                total_neg += math.log(neg)
        if total_pos < total_neg:
            return "negative"
        else:
            return "positive"

        print(pos)
        print(neg)
        print(total_pos)
        print(total_neg)


        """Classifies given text as positive, negative or neutral from calculating the
        most likely document class to which the target string belongs

        Args:
            text - text to classify

        Returns:
            classification, either positive or negative
        """

        pass

        # get the sum of all of the frequencies of the features in each document class
        # (i.e. how many words occurred in all documents for the given class) - this
        # will be used in calculating the probability of each document class given each
        # individual feature

        # for each token in the text, calculate the probability of it occurring in a
        # positive document and in a negative document and add the logs of those to the
        # running sums. when calculating the probabilities, always add 1 to the numerator
        # of each probability for add one smoothing (so that we never have a probability
        # of 0)

        # for debugging purposes, it may help to print the overall positive and negative
        # probabilities

        # determine whether positive or negative was more probable (i.e. which one was
        # larger)

        # return a string of "positive" or "negative"


        # for debugging purposes, it might be useful to print out the tokens and their
        # frequencies for both the positive and negative dictionaries

        # once you have gone through all the files, save the frequency dictionaries to
        # avoid extra work in the future (using the save_dict method). The objects you
        # are saving are self.pos_freqs and self.neg_freqs and the filepaths to save to
        # are self.pos_filename and self.neg_filename

    def load_file(self, filepath: str) -> str:
        """Loads text of given file

        Args:
            filepath - relative path to file to load

        Returns:
            text of the given file
        """
        with open(filepath, "r", encoding='utf8') as f:
            return f.read()

    def save_dict(self, dict: Dict, filepath: str) -> None:
        """Pickles given dictionary to a file with the given name

        Args:
            dict - a dictionary to pickle
            filepath - relative path to file to save
        """
        print(f"Dictionary saved to file: {filepath}")
        with open(filepath, "wb") as f:
            pickle.Pickler(f).dump(dict)

    def load_dict(self, filepath: str) -> Dict:
        """Loads pickled dictionary stored in given file

        Args:
            filepath - relative path to file to load

        Returns:
            dictionary stored in given file
        """
        print(f"Loading dictionary from file: {filepath}")
        with open(filepath, "rb") as f:
            return pickle.Unpickler(f).load()

    def tokenize(self, text: str) -> List[str]:
        """Splits given text into a list of the individual tokens in order

        Args:
            text - text to tokenize

        Returns:
            tokens of given text in order
        """
        tokens = []
        token = ""
        for c in text:
            if (
                re.match("[a-zA-Z0-9]", str(c)) != None
                or c == "'"
                or c == "_"
                or c == "-"
            ):
                token += c
            else:
                if token != "":
                    tokens.append(token.lower())
                    token = ""
                if c.strip() != "":
                    tokens.append(str(c.strip()))

        if token != "":
            tokens.append(token.lower())
        return tokens

    def update_dict(self, words: List[str], freqs: Dict[str, int]) -> None:

        for word in words:
            #print("word is: " + word)
            if word in freqs:
                freqs[word] += 1
            else:
                freqs[word] = 1

        """Updates given (word -> frequency) dictionary with given words list
        This involves incrementing the count of each word in `words` in the `freqs`
        dictionary or adding words with a starting count of 1 if they don't already exist in `freqs`.
        By updating we mean increment the count of each word in words in the dictionary.
        If any word in words is not currently in the dictionary add it with a count of 1.
        (if a word is in words multiple times you'll increment it as many times
        as it appears)

        Args:
            words - list of tokens to update frequencies of
            freqs - dictionary of frequencies to update
        """

        pass


from classifier_lib import *

b = BayesClassifier()
a_list_of_words = ["I", "really", "like", "this", "movie", ".", "I", "hope", \
                    "you", "like", "it", "too"]
a_dictionary = {}
b.update_dict(a_list_of_words, a_dictionary)

print(b.classify('rainy days are the worst'))
#== "negative"