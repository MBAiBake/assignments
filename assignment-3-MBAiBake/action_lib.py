# Netid: tmb9978

from data import features
from match import match

import re


# import pdb


##########Action Functions###############################


def country_by_rank(matches):
    """Takes a list of matches as input - specifically one that holds a rank
        and a feature, like 'population.' Finds the country with that rank
        using tha feature and returns it in a list.

        Args: matches - a list of strings resulting from a call to match. It
        holds a rank and a feature.

        Returns: a list of one string - the rank of the country for the
        specified feature. If the country or feature is not found, returns an
        empty list.
    """
    data = features[matches[1]]
    try:
        country = ""
        for key in data:
            if data[key][0] == matches[0]:
                country = key

    # KeyError 映射中没有这个键
    except KeyError:  # not find any data in csv
        print("Oops! Try other key word again...")
        return None

    # 如果在try子句执行时没有发生异常，python将执行else语句后的语句（如果有else的话），然后控制流通过整个try语句。
    else:
        if country:
            return [country]
        else:
            return []


def rank_by_country(matches):
    """Takes a list of matches as input - specifically one that holds a country
        and a feature, like 'population.' Finds the rank for that country
        using tha feature and returns it in a list.

        Args: matches - a list of strings resulting from a call to match. It
        holds a country and a feature.

        Returns: a list of one string - the rank of the country for the
        specified feature. If the country or feature is not found, returns an
        empty list.
    """
    data = features[matches[1]]
    try:
        rank = ""
        rank = data[matches[0]][0]
    # KeyError 映射中没有这个键
    except KeyError:  # not find any data in csv
        print("Oops! Try other key word again...")
        return None
    # 如果在try子句执行时没有发生异常，python将执行else语句后的语句（如果有else的话），然后控制流通过整个try语句。
    else:
        if rank:
            return [rank]
        else:
            return []


def list_countries(unused):
    """Takes an input that is unused (empty list resulting from a call to match).
        Constructs a list of countries by looking at the keys from one of the
        dictionaries.

        Args: unused - an empty list resulting from a call to match.

        Returns: a list of countries.
    """

    if len(unused) == 0:
        return None
    else:
        return unused


def list_patterns(unused):
    """Takes an input that is unused (empty list resulting from a call to match).
        Constructs a list of the patterns from the pa_list and returns it.

        Args: unused - an empty list resulting from a call to match.

        Returns: a list of the known patterns.
    """

    if len(unused) == 0:
        return None
    else:
        return unused


def bye_action(unused):
    """This action function gets called when the user writes 'bye'.
        It raises KeyboardInterrupt in order to break out of the query loop.

        Args: unused - an empty list resulting from a call to match.
    """

    if len(unused) == 0:
        raise KeyboardInterrupt
    else:
        return unused

def ranking_by_country(matches):
    try:
        data1 = features[matches[0]]
        data2 = features[matches[1]]
        top10data1 = []
        top10data2 = []

        for k, v in data1.items():
            if int(v[0]) <= 10:
                top10data1.append(k)

        for k, v in data2.items():
            if int(v[0]) <= 10:
                top10data2.append(k)
    except KeyError:  # not find any data in csv
        print("Oops! Try other key word again...")
        return None
    else:
        return sorted(list(set(top10data1)&set(top10data2)))

def gdp_by_country(matches):
    data = features['gdp']
    try:
        gdp = data[matches[0]][1]
    except KeyError:  # not find any data in csv
        print("Oops! Try other key word again...")
        return None
    else:
        if gdp:
            return [gdp]
        else:
            return []

def life_exp_by_country(matches):
    data = features['life expectancy']
    try:
        life_exp = data[matches[0]][1]
    except KeyError:  # not find any data in csv
        print("Oops! Try other key word again...")
        return None
    else:
        if life_exp:
            return [life_exp]
        else:
            return []

def gdp_and_life_by_country(matches):
    data = features['gdp']
    data_2 = features['life expectancy']
    try:
        gdp = data[matches[0]][1]
    except KeyError:  # not find any data in csv
        print("Oops! Try other key word again...")
        return None
    else:
        if gdp:
            try:
                life_exp = data_2[matches[0]][1]
            except KeyError:
                print("Oops! Try other key word again...")
                return None
            else:
                return [gdp] + [life_exp]
        else:
            return []


def two_by_country(matches):
    data_a1 = features[matches[0]]
    data_a2 = features[matches[1]]
    try:
        a1 = data_a1[matches[2]][1]
        a2 = data_a2[matches[2]][1]
    except KeyError:  # not find any data in csv
        print("Sorry! I don't find any data!")
        return None
    else:
        return [a1] + [a2]

# #########Pattern, Action list###############################


pa_list = [(str.split("which country is ranked number _ for %"), country_by_rank),
           (str.split("what is % ranked for %"), rank_by_country),
           (str.split("which countries do you know about"), list_countries),
           (str.split("what kinds of questions do you understand"), list_patterns),
           (str.split("what is the gdp of _"), gdp_by_country),
           (str.split("what is the life expectancy of _"), life_exp_by_country),
           (str.split("what are the gdp and life expectancy of _"), gdp_and_life_by_country),
           (str.split("which countries are in the top 10 for % and %"), ranking_by_country),
           (str.split("what are the _ and _ of %"), two_by_country),
           (["bye"], bye_action)]


def search_pa_list(src):
    """Takes source, finds matching pattern and calls corresponding action. If it finds
    a match but has no answers it returns ["No answers"]. If it finds no match it
    returns ["I don't understand"].

    Args:
        source - a phrase represented as a list of words (strings)

    Returns:
        a list of answers. Will be ["I don't understand"] if it finds no matches and
        ["No answers"] if it finds a match but no answers
    """
    result = ["I don't understand"]
    # pdb.set_trace()
    for item in pa_list:
        temp = match(item[0], src)
        if temp:
            if item[1](temp):
                return item[1](temp)
            else:
                return ["No answers"]

    return result


def query_loop():
    """Query_loop asks the user for input, then "cleans" that input
        by converting all characters to lowercase, removing any training
        punctuation (e.g. ?). After then converting the input to a list
        of strings, we pass the list off to search_pa_list to get answers,
        then display the answers to the user.
        Use a try/except structure to catch Ctrl-C or Ctrl-D characters
        and exit gracefully. You'll need to except KeyboardInterrupt and
        EOFError.
    """

    try:
        pat = '[a-z0-9_%]+'
        word = input("please input:").lower()
        lst = re.findall(pat, word)
        print(search_pa_list(lst))
    except KeyboardInterrupt:
        pass
    except EOFError:
        pass


if __name__ == "__main__":
    # uncomment the line below to interact with your chatbot
    query_loop()
    pass
