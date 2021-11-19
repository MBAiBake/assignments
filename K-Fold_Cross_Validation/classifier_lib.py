#tmb9978, jnz1489

import math, os, pickle, re
from typing import Tuple, List, Dict
import random


class BayesClassifier:
    """A Naive Bayes Classifier.
    Attributes:
        pos_freqs - dictionary of frequencies of positive words
        neg_freqs - dictionary of frequencies of negative words
        training_data_directory - relative path to training directory
        neg_file_prefix - prefix of negative reviews
        pos_file_prefix - prefix of positive reviews
        n - total number of data files
        pos_n - total number of positive data files
        neg_n - total number of negative data files
        k - for k-fold cross validation
        sets - a list of lists - the k sets of file names
    """

    def __init__(self):
        self.pos_freqs: Dict[str, int] = {}
        self.neg_freqs: Dict[str, int] = {}
        self.training_data_directory: str = "movie_reviews/"
        self.neg_file_prefix: str = "movies-1"
        self.pos_file_prefix: str = "movies-5"
        #data members added for cross validation
        self.n: int = 0     #total number of files
        self.pos_n: int = 0 #total number of pos files
        self.neg_n: int = 0 #total number of neg files
        self.k: int = 10    #for k-fold cross validation
        self.sets: List[List[str]] = [] #k sets of filenames for k-fold cross validation

    def train(self, files: List[str]) -> None:
        """Trains the Naive Bayes Classifier.
        Train here means generates 'self.pos_freqs' and 'self.neg_freqs' dictionaries with
        frequencies of words in corresponding positive/negative reviews. Additionally
        sets self.pos_n and self.neg_n with the appropriate values (number of positive
        files and negative files in files).

        Args: files - a list of files to use as training data.

        Returns: None
        """

        #reset the following 4 attributes to wipe out any prior training
        self.pos_freqs = {}
        self.neg_freqs = {}
        self.pos_n = 0
        self.neg_n = 0

        for index, filename in enumerate(files, 1):
            text = self.load_file(os.path.join(self.training_data_directory, filename))

            tokens: List[str] = self.tokenize(text)

            if filename.startswith(self.pos_file_prefix):
                self.update_dict(tokens, self.pos_freqs)
                self.pos_n += 1

            elif filename.startswith(self.neg_file_prefix):
                self.update_dict(tokens, self.neg_freqs)
                self.neg_n += 1

    def classify(self, text: str) -> str:
        """Classifies given text as positive or negative by calculating the
        most likely document class to which the target string belongs

        Args:
            text - text to classify

        Returns:
            classification as a str, either positive or negative
        """
        tokens = self.tokenize(text)

        #initialize the probabilities with the prior probabilities of each class
        pos_prob = math.log(self.pos_n/(self.pos_n+self.neg_n))
        neg_prob = math.log(self.neg_n/(self.pos_n+self.neg_n))

        num_pos_words = sum(self.pos_freqs.values())
        num_neg_words = sum(self.neg_freqs.values())

        for word in tokens:
            num_pos_appearances = 1
            if word in self.pos_freqs:
                num_pos_appearances += self.pos_freqs[word]

            pos_prob += math.log(num_pos_appearances / num_pos_words)

            num_neg_appearances = 1
            if word in self.neg_freqs:
                num_neg_appearances += self.neg_freqs[word]

            neg_prob += math.log(num_neg_appearances / num_neg_words)

        if pos_prob > neg_prob:
            return "positive"
        else:
            return "negative"

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
        """Updates given (word -> frequency) dictionary with given words list

        By updating we mean increment the count of each word in words in the dictionary.
        If any word in words is not currently in the dictionary add it with a count of 1.
        (if a word is in words multiple times you'll increment it as many times
        as it appears)

        Args:
            words - list of tokens to update frequencies of
            freqs - dictionary of frequencies to update
        """
        for word in words:
            if word in freqs:
                freqs[word] += 1
            else:
                freqs[word] = 1

    def split(self) -> None:
        """ Splits the files into k sets. Positive files and negative files must
        be spread evenly among the sets. That is, separate the files into a
        list of positive files and a list of negative files. Divide each of those
        lists into k equal sizes chunks and store them in self.sets (the list of k
        sets). Note that it might not be possible for the files to be divided
        evenly into k sets, the size of the sets might be off by one.

        Returns: None
        """
        files: List[str] = next(os.walk(self.training_data_directory))[2]
        random.shuffle(files)
        file_pos = []
        file_neg = []

        for item in files:
            if item.startswith(self.pos_file_prefix):
                file_pos.append(item)
            else:
                file_neg.append(item)

        pos_set = len(file_pos) // self.k
        neg_set = len(file_neg) // self.k

        for i in range(self.k):
            #produce set i
            pos_set_list = file_pos[i * pos_set:(i + 1) * pos_set]
            neg_set_list = file_neg[i * neg_set:(i + 1) * neg_set]
            self.sets.append(pos_set_list + neg_set_list)

    def classify_all(self, testing_data_set: List[str]) -> List[Tuple[str, str, str]]:
        """Runs self.classify on the contents of each file in the input list.

        Args:', 'positive', 'positive'),
             ('movies-5-13188.txt', 'positive', 'positive'),
             ('movies-5-7898.txt', 'positive', 'negative'),
            ...]
        """
        classify_all_list = []
        for name in testing_data_set:
            text = self.load_file(os.path.join(self.training_data_directory, name))
            if name[7] == '5':
                a = 'positive'
            else:
                a = 'negative'
            b = self.classify(text)
            classify_all_list.append((name, a, b))

        return classify_all_list

    def analyze_results(self, classy_results: List[Tuple[str, str, str]]) -> Tuple[float, float, float, float, float, float, float]:
        """Given a list of classification results as input, computes and returns
        a list of values for the performance metrics.

        Args:
            classy_results: classy_results will be a list of tuples of the following format....
            (file_name, truth value, classifier result)
            For example,

            [('movies-5-14993.txt', 'positive', 'positive'),
             ('movies-5-13188.txt', 'positive', 'positive'),
             ('movies-5-7898.txt', 'positive', 'negative'),
            ...]

        Returns:
            Using the classy_results data, this function will produce and return a
            tuple of the following metrics:
            (accuracy, pos_precision, pos_recall, pos_f1, neg_precision, neg_recall, neg_f1)
        """
        tp = 0
        tn = 0
        fp = 0
        fn = 0

        for items in classy_results:
            if items[1] == 'positive' and items[2] == 'positive':
                tp += 1
            elif items[1] == 'negative' and items[2] == 'negative':
                tn += 1
            elif items[1] == 'positive' and items[2] == 'negative':
                fn += 1
            elif items[1] == 'negative' and items[2] == 'positive':
                fp += 1

        accuracy = (tp + tn) / (tp + fp + tn + fn)
        pos_precision = tp / (tp + fp)
        pos_recall = tp / (tp + fn)
        pos_f1 = (2*pos_precision*pos_recall)/ (pos_precision + pos_recall)
        neg_precision = tn / (tn + fn)
        neg_recall = tn / (tn + fp)
        neg_f1 = (2*neg_precision*neg_recall) / (neg_precision + neg_recall)
        return (accuracy, pos_precision, pos_recall, pos_f1, neg_precision, neg_recall, neg_f1)

    def calculate_averages(self, k_sets_of_metrics: List[Tuple]) -> List[float]:
        """Calculates and returns the average of each of the metrics across the k runs.

        Args:
            k_sets_of_metrics:
            a list of k tuples (each of 7 items - performance metric data). For example,
            [(0.8057761732851986, 0.9720044792833147, 0.7805755395683454, 0.8658354114713217, 0.5040650406504065, 0.9084249084249084, 0.6483660130718955),
             (0.8067772170151406, 0.9806598407281001, 0.7744833782569631, 0.8654618473895581, 0.5059055118110236, 0.9379562043795621, 0.6572890025575447),
             (0.7936507936507936, 0.9704209328782708, 0.766397124887691, 0.856425702811245, 0.48717948717948717, 0.9047619047619048, 0.6333333333333333),
             ...]

        Returns:
            Produces and returns a list of 7 items, the average value for each metric across the k runs.
        """
        accuracy = 0.0
        pos_precision = 0.0
        pos_recall = 0.0
        pos_f1 = 0.0
        neg_precision = 0.0
        neg_recall = 0.0
        neg_f1 = 0.0

        for tuple in k_sets_of_metrics:
            accuracy += tuple[0]
            pos_precision += tuple[1]
            pos_recall += tuple[2]
            pos_f1 += tuple[3]
            neg_precision += tuple[4]
            neg_recall += tuple[5]
            neg_f1 += tuple[6]
        return [accuracy/self.k, pos_precision/self.k, pos_recall/self.k, pos_f1/self.k, neg_precision/self.k, neg_recall/self.k, neg_f1/self.k]

    def evaluate(self) -> None:
        """ This method drives the k-fold cross validation process. First, it calls the
        split method to generate k sets of filenames, stored in self.sets. Next, it loops
        over those sets, letting each have a turn being the testing data (training a
        classifier with the other 9 sets).  More details can be found in the assignment pdf.

        Returns: None
        """
        self.split() #split the data (file names) into self.k sets, stored self.sets
        k_metrics = []
        for i in range(self.k): #execute k-fold cross validation
            td = self.sets[0:i] + self.sets[i+1:] #grab everything other than set i
            training_data = []
            for lst in td:
                training_data += lst
            self.train(training_data) #training on all sets other than set i

            testing_data = self.sets[i] #testing data is set i
            classification_results = self.classify_all(testing_data)
            metrics = self.analyze_results(classification_results)
            k_metrics.append(metrics)
        summary_results = self.calculate_averages(k_metrics)

        print(f"summary of results")
        print(f"average {summary_results[0]}")
        print(f"positive precision {summary_results[1]}")
        print(f"positive recall {summary_results[2]}")
        print(f"positive f-measure {summary_results[3]}")
        print(f"negative precision {summary_results[4]}")
        print(f"negative recall {summary_results[5]}")
        print(f"negative f-measure {summary_results[6]}")

if __name__ == "__main__":
    b = BayesClassifier()
    b.evaluate()
    b.classify_all()
    b.analyze_results()
