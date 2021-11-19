from action_lib import country_by_rank, rank_by_country, list_countries, list_patterns, bye_action, search_pa_list


def test_country_by_rank():
  assert country_by_rank(["2", "population"]) == ["india"], "country_by_rank test"


def test_rank_by_country():
  assert rank_by_country(["united states", "area"]) == ["4"], "rank_by_country test"


def test_search_pa_list1():
  assert search_pa_list(["hi", "there"]) ==["I don't understand"], "search_pa_list test 1"
 

def test_search_pa_list2():
  assert search_pa_list(["which", "country", "is", "ranked", "number", "2", "for",
                        "median", "age"]) == ["japan"], "search_pa_list test 2"

def test_search_pa_list3():
  assert search_pa_list(["what", "is", "XYZ", "ranked", "for", "population"]) == ["No answers"], "search_pa_list test 3"


def test_search_pa_list4():
  assert search_pa_list(["which", "country", "is", "ranked", "number", "2", "for",
                        "area"]) == ["antarctica"], "search_pa_list test 4"

def test_search_pa_list5():
  assert search_pa_list(['what', 'is', 'the', 'gdp', 'of', 'china']) == ['$22,526,502,000,000'], "search_pa_list test 5"

def test_search_pa_list6():
  assert search_pa_list(['what', 'is', 'the', 'life', 'expectancy', 'of' , 'andorra']) == ['83.23'], "search_pa_list test 6"

def test_search_pa_list7():
    assert search_pa_list(['what', 'are', 'the',
                           'gdp', 'and', 'life','expectancy' ,'of', 'japan']) == ['$5,231,066,000,000','84.65'], "search_pa_list 7"

def test_search_pa_list8():
    assert search_pa_list(['which', 'countries', 'are' ,'in', 'the', 'top', '10', 'for', 'gdp', 'and', 'area']) == ['brazil', 'china', 'india', 'russia', 'united states'], "search_pa_list 8"

def test_search_pa_list9():
    assert search_pa_list(["what", "are", "the",
                           "gdp", "and", "population", "of", "mexico"]) == ["$2,525,481,000,000", "130,207,371"], "search_pa_list 9"