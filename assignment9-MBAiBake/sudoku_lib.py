# we will use copy to make a deepcopy of the board
import copy
from typing import List, Any, Tuple

# import Stack and Queue classes for BFS/DFS
from stack_and_queue import Stack, Queue


def remove_if_exists(lst: Any, elem: Any) -> None:
    """Takes a list and element and removes that element if it exists in the list.

    Args:
        lst - the list you're trying to remove an item from
        elem - item to remove
    """
    if isinstance(lst, list) and elem in lst:
        lst.remove(elem)


class Board:
    """Represents a state (situation) in a Sudoku puzzle. Some cells may have filled in
    numbers while others have not. Cells that have not been filled in hold a list of
    the potential values that could be assigned to the cell (i.e. have not been ruled out
    from the row, column or subgrid)

    Attributes:
        num_nums_placed - number of numbers placed so far (initially 0)
        size - the size of the board (this will always be 9, but is convenient to have
            an attribute for this for debugging purposes)
        rows - a list of 9 lists, each with 9 elements (imagine a 9x9 sudoku board).
            Each element will itself be a list of the numbers that remain possible to
            assign in that square. Initially, each element will contain a list of the
            numbers 1 through 9 (so a triply nested 9x9x9 list to start) as all numbers
            are possible when no assignments have been made. When an assignment is made
            this innermost element won't be a list of possibilities anymore but the
            single number that is the assignment.
    """

    def __init__(self):
        """Constructor for a board, sets up a board with each element having all
        numbers as possibilities"""
        self.size: int = 9
        self.num_nums_placed: int = 0

        # triply nested lists, representing a 9x9 sudoku board
        # 9 quadrants, 9 cells in each 3*3 subgrid, 9 possible numbers in each cell
        # Note: using Any in the type hint since the cell can be either a list (when it
        # has not yet been assigned a value) or a number (once it has been assigned)
        self.rows: List[List[Any]] = []
        for i in range(self.size):
            arow = []
            for j in range(self.size):
                arow.append([1, 2, 3, 4, 5, 6, 7, 8, 9])
            self.rows.append(arow)

    def __str__(self) -> str:
        """String representation of the board"""
        row_str = ""
        for r in self.rows:
            row_str += f"{r}\n"

        return f"num_nums_placed: {self.num_nums_placed}\nboard (rows): \n{row_str}"

    def print_pretty(self):
        """Prints all numbers assigned to cells, excluding lists of possible numbers
        that can still be assigned to cells"""
        row_str = ""
        for i, r in enumerate(self.rows):
            if not i % 3:
                row_str += " -------------------------\n"

            for j, x in enumerate(r):
                row_str += " | " if not j % 3 else " "
                row_str += "*" if isinstance(x, list) else f"{x}"

            row_str += " |\n"

        row_str += " -------------------------\n"
        print(f"num_nums_placed: {self.num_nums_placed}\nboard (rows): \n{row_str}")

    def subgrid_coordinates(self, row: int, col: int) -> List[Tuple[int, int]]:
        """Get all coordinates of cells in a given cell's subgrid (3x3 space)

        Integer divide to get column & row indices of subgrid then take all combinations
        of cell indices with the row/column indices from those subgrids (also known as
        the outer or Cartesian product)

        Args:
            row - index of the cell's row, 0 - 8
            col - index of the cell's col, 0 - 8

        Returns:
            list of (row, col) that represent all cells in the box.
        """
        # Note: row // 3 gives the index of the subgrid for the row index, this is one
        # of 0, 1 or 2, col // 3 gives us the same for the column
        coords = []
        for r in range(self.size):
            for c in range(self.size):
                if r // 3 == row // 3 and c // 3 == col // 3:
                    coords.append((r, c))
        return coords

    def find_most_constrained_cell(self) -> Tuple[int, int]:
        """Finds the coordinates (row and column indices) of the cell that contains the
        fewest possible values to assign (the shortest list). Note: in the case of ties
        return the coordinates of the first minimum size cell found

        Returns:
            a tuple of row, column index identifying the most constrained cell
        """
        pass

        best_row = 0
        best_col = 0
        shortest_len = 10
        for i in range(self.size):
            for j in range(self.size):
                z = self.rows[i][j]
                if isinstance(z, list):
                    if len(z) < shortest_len:
                        best_row = i
                        best_col = j
                        shortest_len = len(z)
        return best_row, best_col

    def failure_test(self) -> bool:
        """Check if we've failed to correctly fill out the puzzle. If we find a cell
        that contains an [], then we have no more possibilities for the cell but haven't
        assigned it a value so fail.

        Returns:
            True if we have failed to fill out the puzzle, False otherwise
        """

        for i in range(self.size):
            for j in range(self.size):
                z = self.rows[i][j]
                if z == []:
                    return True
        else:
            return False

    def goal_test(self) -> bool:
        """Check if we've completed the puzzle (if we've placed all the numbers).
        Naively checks that we've placed as many numbers as cells on the board

        Returns:
            True if we've placed all numbers, False otherwise
        """
        if self.size * self.size == self.num_nums_placed:
            return True
        else:
            return False

    def update(self, row: int, column: int, assignment: int) -> None:
        """Assigns the given value to the cell given by passed in row and column
        coordinates. By assigning we mean set the cell to the value so instead the cell
        being a list of possibities it's just the new assignment value.  Update all
        affected cells (row, column & subgrid) to remove the possibility of assigning
        the given value.

        Args:
            row - index of the row to assign
            column - index of the column to assign
            assignment - value to place at given row, column coordinate
        """

        self.rows[row][column] = assignment
        self.num_nums_placed += 1
        lst = self.subgrid_coordinates(row, column)

        for i in range(len(self.rows)):
            for j in range(len(self.rows)):
                if (i, j) in lst or i == row or j == column:
                    if isinstance(self.rows[i][j], list):
                        remove_if_exists(self.rows[i][j], assignment)


def DFS(state: Board) -> Board:
    """Performs a depth first search. Takes a Board and attempts to assign values to
    most constrained cells until a solution is reached or a mistake has been made at
    which point it backtracks.

    Args:
        state - an instance of the Board class to solve, need to find most constrained
            cell and attempt an assignment

    Returns:
        either None in the case of invalid input or a solved board
    """

    fringe = Stack()
    fringe.push(state)
    while not fringe.is_empty():
        curr = fringe.pop()
        if curr.goal_test():
            return curr
        elif not curr.failure_test():
            pos = curr.find_most_constrained_cell()
            x = pos[0]
            y = pos[1]
            for i in curr.rows[x][y]:
                new = copy.deepcopy(curr)
                new.update(x,y,i)
                fringe.push(new)
    return None

def BFS(state: Board) -> Board:
    """Performs a breadth first search. Takes a Board and attempts to assign
    values to most constrained cells until a solution is reached or a mistake
    has been made at which point it backtracks.

    Args:
        state - an instance of the Board class to solve, need to find most
        constrained cell and attempt an assignment

    Returns:
        either None in the case of invalid input or a solved board
    """

    fringe = Queue()
    fringe.push(state)
    while not fringe.is_empty():
        curr = fringe.pop()
        if curr.goal_test():
            return curr
        elif not curr.failure_test():
            pos = curr.find_most_constrained_cell()
            x = pos[0]
            y = pos[1]
            for i in curr.rows[x][y]:
                new = copy.deepcopy(curr)
                new.update(x, y, i)
                fringe.push(new)
    return None

# the Stack and Queue classes for DFS and BFS
from typing import Generic, List, TypeVar

# stack element type variable
S = TypeVar("S")
# queue element type variable
Q = TypeVar("Q")

if __name__ == "__main__":
    myb = Board()
    myb.rows[7][5] = [2, 4, 6, 7]
    myb.rows[1][8] = [4, 6, 7]
    myb.rows[3][5] = [1, 3, 4, 5]
    myb.rows[8][7] = [1, 2, 3, 4, 5]
    # add more ad hoc testing code if you choose to

myb = Board()
myb.rows[7][5] = [2,4,6,7]
myb.rows[1][8] = [4,6,7]
myb.rows[3][5] = [1,3,4,5]
myb.rows[8][7] = [1,2,3,4,5]
myb.rows[6][5] = [2,3]
myb.rows[4][3] = 5
myb.num_nums_placed = 1
myb.update(0, 0, 3)
print(myb.rows[0][8])
