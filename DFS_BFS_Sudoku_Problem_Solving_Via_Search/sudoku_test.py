from sudoku_lib import *

def test_most_cons_1():
    myb = Board()
    myb.rows[7][5] = [2,4,6,7]
    myb.rows[1][8] = [4,6,7]
    myb.rows[3][5] = [1,3,4,5]
    myb.rows[8][7] = [1,2,3,4,5]
    assert myb.find_most_constrained_cell() == (1,8), "find most constrained test 1"

def test_most_cons_2():
    myb = Board()
    myb.rows[7][5] = [2,4,6,7]
    myb.rows[1][8] = [4,6,7]
    myb.rows[3][5] = [1,3,4,5]
    myb.rows[8][7] = [1,2,3,4,5]
    myb.rows[6][5] = [2,3]
    assert myb.find_most_constrained_cell() == (6,5), "find most constrained test 2"

def test_most_cons_3():
    myb = Board()
    myb.rows[7][5] = [2,4,6,7]
    myb.rows[1][8] = [4,6,7]
    myb.rows[3][5] = [1,3,4,5]
    myb.rows[8][7] = [1,2,3,4,5]
    myb.rows[6][5] = [2,3]
    myb.rows[4][3] = 5
    assert myb.find_most_constrained_cell() == (6,5), "find most constrained test 3"
    

def test_failure_1():
    myb = Board()
    myb.rows[7][5] = [2,4,6,7]
    myb.rows[1][8] = [4,6,7]
    myb.rows[3][5] = [1,3,4,5]
    myb.rows[8][7] = [1,2,3,4,5]
    myb.rows[6][5] = [2,3]
    myb.rows[4][3] = 5
    assert myb.failure_test() == False, "failure test test 1"

def test_failure_2():
    myb = Board()
    myb.rows[7][5] = [2,4,6,7]
    myb.rows[1][8] = [4,6,7]
    myb.rows[3][5] = [1,3,4,5]
    myb.rows[8][7] = [1,2,3,4,5]
    myb.rows[6][5] = [2,3]
    myb.rows[4][3] = 5
    myb.rows[6][5] = []
    assert myb.failure_test() == True, "failure test test 2"

def test_goal_1():
    myb = Board()
    myb.rows[7][5] = [2,4,6,7]
    myb.rows[1][8] = [4,6,7]
    myb.rows[3][5] = [1,3,4,5]
    myb.rows[8][7] = [1,2,3,4,5]
    myb.rows[6][5] = [2,3]
    myb.rows[4][3] = 5
    myb.rows[6][5] = []
    assert myb.goal_test() == False, "goal test test 1"

def test_goal_2():
    myb = Board()
    myb.rows[7][5] = [2,4,6,7]
    myb.rows[1][8] = [4,6,7]
    myb.rows[3][5] = [1,3,4,5]
    myb.rows[8][7] = [1,2,3,4,5]
    myb.rows[6][5] = [2,3]
    myb.rows[4][3] = 5
    myb.num_nums_placed = 81
    assert myb.goal_test() == True, "goal test test 2"

def test_update_1():
    myb = Board()
    myb.rows[7][5] = [2,4,6,7]
    myb.rows[1][8] = [4,6,7]
    myb.rows[3][5] = [1,3,4,5]
    myb.rows[8][7] = [1,2,3,4,5]
    myb.rows[6][5] = [2,3]
    myb.rows[4][3] = 5
    myb.num_nums_placed = 1
    myb.update(0, 0, 3)
    assert myb.rows[0][0] == 3, "update test 1"

def test_update_2():
    myb = Board()
    myb.rows[7][5] = [2,4,6,7]
    myb.rows[1][8] = [4,6,7]
    myb.rows[3][5] = [1,3,4,5]
    myb.rows[8][7] = [1,2,3,4,5]
    myb.rows[6][5] = [2,3]
    myb.rows[4][3] = 5
    myb.num_nums_placed = 1
    myb.update(0, 0, 3)
    assert myb.num_nums_placed == 2, "update test 2"

def test_update_3():
    myb = Board()
    myb.rows[7][5] = [2,4,6,7]
    myb.rows[1][8] = [4,6,7]
    myb.rows[3][5] = [1,3,4,5]
    myb.rows[8][7] = [1,2,3,4,5]
    myb.rows[6][5] = [2,3]
    myb.rows[4][3] = 5
    myb.num_nums_placed = 1
    myb.update(0, 0, 3)
    assert 3 not in myb.rows[0][8], "update test 3"

def test_update_4():
    myb = Board()
    myb.rows[7][5] = [2,4,6,7]
    myb.rows[1][8] = [4,6,7]
    myb.rows[3][5] = [1,3,4,5]
    myb.rows[8][7] = [1,2,3,4,5]
    myb.rows[6][5] = [2,3]
    myb.rows[4][3] = 5
    myb.num_nums_placed = 1
    myb.update(0, 0, 3)
    assert 3 not in myb.rows[5][0], "update test 4"

def test_update_5():
    myb = Board()
    myb.rows[7][5] = [2,4,6,7]
    myb.rows[1][8] = [4,6,7]
    myb.rows[3][5] = [1,3,4,5]
    myb.rows[8][7] = [1,2,3,4,5]
    myb.rows[6][5] = [2,3]
    myb.rows[4][3] = 5
    myb.num_nums_placed = 1
    myb.update(0, 0, 3)
    assert 3 not in myb.rows[2][2], "update test 5"


def driver_test_dfs_or_bfs(use_dfs: bool, moves: List[Tuple[int, int, int]]) -> None:
    b = Board()
    # make initial moves to set up board
    for move in moves:
        b.update(*move)

    # print initial board
    print("<<<<< Initial Board >>>>>\n")
    b.print_pretty()
    # solve board
    solution = (DFS if use_dfs else BFS)(b)
    # print solved board
    print("<<<<< Solved Board >>>>>\n")
    solution.print_pretty()
    return solution

    # sets of moves for the different games
first_moves = [
    (0, 1, 7),
    (0, 7, 1),
    (1, 2, 9),
    (1, 3, 7),
    (1, 5, 4),
    (1, 6, 2),
    (2, 2, 8),
    (2, 3, 9),
    (2, 6, 3),
    (3, 1, 4),
    (3, 2, 3),
    (3, 4, 6),
    (4, 1, 9),
    (4, 3, 1),
    (4, 5, 8),
    (4, 7, 7),
    (5, 4, 2),
    (5, 6, 1),
    (5, 7, 5),
    (6, 2, 4),
    (6, 5, 5),
    (6, 6, 7),
    (7, 2, 7),
    (7, 3, 4),
    (7, 5, 1),
    (7, 6, 9),
    (8, 1, 3),
    (8, 7, 8),
]

second_moves = [
    (0, 1, 2),
    (0, 3, 3),
    (0, 5, 5),
    (0, 7, 4),
    (1, 6, 9),
    (2, 1, 7),
    (2, 4, 4),
    (2, 7, 8),
    (3, 0, 1),
    (3, 2, 7),
    (3, 5, 9),
    (3, 8, 2),
    (4, 1, 9),
    (4, 4, 3),
    (4, 7, 6),
    (5, 0, 6),
    (5, 3, 7),
    (5, 6, 5),
    (5, 8, 8),
    (6, 1, 1),
    (6, 4, 9),
    (6, 7, 2),
    (7, 2, 6),
    (8, 1, 4),
    (8, 3, 8),
    (8, 5, 7),
    (8, 7, 5),
]

def test_dfs_1():
    assert isinstance(driver_test_dfs_or_bfs(True, first_moves), Board), "DFS test 1"

def test_dfs_2():  
    #test_dfs_or_bfs(True, second_moves)
    assert isinstance(driver_test_dfs_or_bfs(True, second_moves), Board), "DFS test 2"

def test_bfs_3():
    #test_dfs_or_bfs(False, first_moves)
    assert isinstance(driver_test_dfs_or_bfs(False, first_moves), Board), "BFS test 1"

def test_bfs_2():
    #test_dfs_or_bfs(False, second_moves)
    assert isinstance(driver_test_dfs_or_bfs(False, second_moves), Board), "BFS test 2"

