from classifier_lib import *

b = BayesClassifier()
b.split()
first_file_1 = b.sets[0][0]

def test_split_1():
    assert len(b.sets) == b.k, "split test 1"

def test_split_2():
    assert abs(len(b.sets[0]) - len(b.sets[1])) < 3, "split test 2"

def test_split_3():
    assert abs(len(b.sets[0]) - len(b.sets[-1])) < 3, "split test 3"

def test_split_4():
    assert first_file_1 not in b.sets[1], "split test 4"

def test_split_5():
    b.split()
    first_file_2 = b.sets[0][0]
    assert first_file_2 not in b.sets[1], "split test 5"

#def test_split_6():
    #first_file_2 = b.sets[0][0]
    #the following test makes sure that split is shuffling the data
    #assert first_file_1 != first_file_2, "split test 6"

some_files = ['movies-5-2997.txt', 'movies-5-14493.txt', 'movies-5-5803.txt',
              'movies-5-15857.txt', 'movies-5-12100.txt', 'movies-5-13604.txt',
              'movies-5-12831.txt', 'movies-5-412.txt', 'movies-5-21825.txt',
              'movies-5-23469.txt', 'movies-5-3089.txt', 'movies-5-13672.txt',
              'movies-1-13558.txt', 'movies-1-20209.txt', 'movies-1-13936.txt',
              'movies-1-18942.txt', 'movies-1-3489.txt', 'movies-1-19588.txt',
              'movies-1-4738.txt', 'movies-1-20549.txt']

files: List[str] = next(os.walk(b.training_data_directory))[2]
b.train(files)
results = b.classify_all(some_files)

def test_classify_all_1():
    #tests that classify_all returns a list of the same length
    assert len(results) == len(some_files), "classify_all test 1"


def test_classify_all_2():
    #tests that each item in the returned list is a list or tuple of 3 items
    assert len(results[0]) == 3, "classify_all test 2"


def test_classify_all_3():
    #tests the truth data for a positive file
    assert results[0][1] == "positive", "classify_all test 3"


def test_classify_all_4():
    #tests the truth data for a negative file
    assert results[14][1] == "negative", "classify_all test 4"

classy = [('movies-5-2997.txt', 'positive', 'positive'),
          ('movies-5-14493.txt', 'positive', 'positive'),
          ('movies-5-5803.txt', 'positive', 'positive'),
          ('movies-5-15857.txt', 'positive', 'negative'),
          ('movies-5-12100.txt', 'positive', 'positive'),
          ('movies-5-13604.txt', 'positive', 'positive'),
          ('movies-5-12831.txt', 'positive', 'positive'),
          ('movies-5-412.txt', 'positive', 'positive'),
          ('movies-5-21825.txt', 'positive', 'positive'),
          ('movies-5-23469.txt', 'positive', 'positive'),
          ('movies-5-12331.txt', 'positive', 'negative'),
          ('movies-5-3089.txt', 'positive', 'positive'),
          ('movies-5-13672.txt', 'positive', 'positive'),
          ('movies-1-13558.txt', 'negative', 'negative'),
          ('movies-1-20209.txt', 'negative', 'negative'),
          ('movies-1-13936.txt', 'negative', 'negative'),
          ('movies-1-18942.txt', 'negative', 'negative'),
          ('movies-1-3489.txt', 'negative', 'negative'),
          ('movies-1-19588.txt', 'negative', 'negative'),
          ('movies-1-4738.txt', 'negative', 'negative'),
          ('movies-1-20549.txt', 'negative', 'positive')]

metrics = b.analyze_results(classy)

def test_accuracy():
    assert metrics[0] == 0.8571428571428571, "accuracy test"


def test_positive_precision():
    assert metrics[1] == 0.9166666666666666, "positive precision test"


def test_positive_recall():
    assert metrics[2] == 0.8461538461538461, "positive recall test"


def test_positive_f1():
    assert metrics[3] == 0.8799999999999999, "positive f1 test"


def test_negative_precision():
    assert metrics[4] == 0.7777777777777778, "negative precision test"

def test_negative_recall():
    assert metrics[5] == 0.875, "negative recall test"

def test_negative_f1():
    assert metrics[6] == 0.823529411764706, "negative f1 test"

k_results = [(0.8115523465703971, 0.9829738933030647, 0.7787769784172662, 0.8690416457601605,
              0.5119047619047619, 0.945054945054945, 0.664092664092664),
             (0.8168709444844989, 0.97669256381798, 0.7906558849955077, 0.8738828202581926,
              0.5205761316872428, 0.9233576642335767, 0.6657894736842106),
             (0.8037518037518038, 0.9827784156142365, 0.7690925426774483, 0.8629032258064515,
              0.5009708737864078, 0.945054945054945, 0.6548223350253807),
             (0.7952415284787311, 0.9769850402761795, 0.7628032345013477, 0.8567103935418768,
              0.49034749034749037, 0.927007299270073, 0.6414141414141414),
             (0.8167388167388168, 0.97669256381798, 0.7906558849955077, 0.8738828202581926,
              0.5195876288659794, 0.9230769230769231, 0.6649076517150396),
             (0.8010093727469358, 0.9634551495016611, 0.7816711590296496, 0.8630952380952381,
              0.49793388429752067, 0.8795620437956204, 0.6358839050131926),
             (0.8080808080808081, 0.9721293199554069, 0.7834681042228212, 0.8676616915422886,
              0.5071574642126789, 0.9084249084249084, 0.6509186351706037),
             (0.802451333813987, 0.9718785151856018, 0.7762803234501348, 0.8631368631368631,
              0.5, 0.9087591240875912, 0.6450777202072538),
             (0.810966810966811, 0.9818799546998868, 0.7789757412398922, 0.8687374749498998,
              0.510934393638171, 0.9413919413919414, 0.6623711340206185),
             (0.8103821196827685, 0.9786036036036037, 0.7807726864330637, 0.8685657171414293,
              0.5110220440881763, 0.9306569343065694, 0.6597671410090555)]
summary_results = [0.8077045885315558, 0.9764069019775603, 0.779315253996264, 0.8667617890490593,
                   0.5070434672828428, 0.9232346728697094, 0.654504480135216]

def test_calculate_averages_1():
    assert len(b.calculate_averages(k_results)) == 7, "calculate averages test 1"

def test_calculate_averages_2():
    assert b.calculate_averages(k_results) == summary_results, "calculate averages test 2"

def test_calculate_averages_3():
    b.k = 2
    k_results = [(0.8115523465703971, 0.9829738933030647, 0.7787769784172662, 0.8690416457601605,
                0.5119047619047619, 0.945054945054945, 0.664092664092664),
                (0.8168709444844989, 0.97669256381798, 0.7906558849955077, 0.8738828202581926,
                0.5205761316872428, 0.9233576642335767, 0.6657894736842106)]
    summary_results = [0.814211645527448, 0.9798332285605224, 0.7847164317063869, 0.8714622330091766,
                    0.5162404467960023, 0.9342063046442608, 0.6649410688884373]
    assert b.calculate_averages(k_results) == summary_results, "calculate averages test 3"
