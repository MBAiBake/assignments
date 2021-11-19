from profile_lib import *

# some profiles to work with
sara = Profile("Sara Sood", "Professor of Computer Science", "Northwestern")
peter = Profile("Peter Zhong", "Software Engineer Intern", "Teladoc Health")
milan = Profile("Milan McGraw", "Consultant", "FEV Consulting")
milan.employment_history = [("some role", "some company", 1995, 2001),
                            ("another role", "another company", 2001, 2009),
                            ("yet another role", "yet another company", 2009, 2018)]
masum = Profile("Masum Patel", "Consultant", "Deloitte")
masum.employment_history = [("another role", "another company", 1995, 1996),
                            ("yet another role", "yet another company", 1996, 2010)]
kris = Profile("Kris Hammond", "Professor of Computer Science", "Northwestern")
bob = Profile("Bob", "Northwestern")

connect(sara, peter)
connect(sara, peter)  # adding this to make sure no duplicates in connections
connect(peter, milan)
connect(masum, milan)
connect(masum, kris)
connect(milan, kris)


def test_connection_number_is_1():
    assert len(sara.connections) == 1, "connect test 1"


def test_connection_number_is_3():
    assert len(milan.connections) == 3, "connect test 2"


def test_in_two_connections():
    assert milan in kris.connections and kris in milan.connections, "connect test 3"


def test_no_connection():
    assert sara not in kris.connections, "connect test 4"


def test_where_work_together():
    assert where_did_they_work_together(milan,
                                        masum) == "yet another company", "where_did_they_work_together test 1"


def test_did_not_work_together():
    assert where_did_they_work_together(milan,
                                        kris) == False, "where_did_they_work_together test 2"


def test_shortest_path():
    assert shortest_path(sara, kris) == (3,
                                         ["Sara Sood",
                                          "Peter Zhong",
                                          "Milan McGraw",
                                          "Kris Hammond"]), "shortest path 1"


def test_no_path_at_all():
    assert shortest_path(sara, bob) == None, "shortest path 2"


# uncomment the following two test cases if you decide to complete the optional extension
# def test_shortest_path_to_someone_at_deloitte():
#     # find someone connected to sara who works for deloitte
#     assert shortest_path_to_someone_who(sara,
#                                         lambda x:
#                                         x.company == "Deloitte") == (3,
#                                                                      ['Sara Sood',
#                                                                       'Peter Zhong',
#                                                                       'Milan McGraw',
#                                                                       'Masum Patel'])
#
#
# def test_shortest_path_to_connected_to_and_work_with_sara():
#     # find someone connected to sara, who works with sara (but is not herself)
#     assert shortest_path_to_someone_who(sara,
#                                         lambda x:
#                                         x.company == sara.company
#                                         and x.name != sara.name) == (3,
#                                                                      ['Sara Sood',
#                                                                       'Peter Zhong',
#                                                                       'Milan McGraw',
#                                                                       'Kris Hammond'])
