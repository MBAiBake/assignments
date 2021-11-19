# we will use copy to make a deepcopy of the board
import copy
from typing import List, Any, Tuple


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
                arow.append([1,2,3,4,5,6,7,8,9])
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
                if r//3 == row//3 and c//3 == col//3:
                    coords.append((r,c))
        return coords

    def find_most_constrained_cell(self) -> Tuple[int, int]:
        """Finds the coordinates (row and column indices) of the cell that contains the
        fewest possible values to assign (the shortest list). Note: in the case of ties
        return the coordinates of the first minimum size cell found

        Returns:
            a tuple of row, column index identifying the most constrained cell
        """
        #for each row
        #    for each col
        #        if the cell in that spot is a list
        #            if the len is shorter than the shortest we've seen
        #                save the position and length
        #return the position
    

    def failure_test(self) -> bool:
        """Check if we've failed to correctly fill out the puzzle. If we find a cell
        that contains an [], then we have no more possibilities for the cell but haven't
        assigned it a value so fail.

        Returns:
            True if we have failed to fill out the puzzle, False otherwise
        """
        #are there any [] on the board?
        #loop over each row
        #    loop over each col
        #         does that spot have a []?
        #              return True!
        #return False

    def goal_test(self) -> bool:
        """Check if we've completed the puzzle (if we've placed all the numbers).
        Naively checks that we've placed as many numbers as cells on the board

        Returns:
            True if we've placed all numbers, False otherwise
        """
        #are there 81 (or self.size*self.size) numbers placed?

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
        # set the cell of self.rows at row, column position to assignment
        # update num_nums_placed (because we placed a num)

        # get the list of coordinates in the same subgrid as row, column using subgrid_coordinates

        # loop over each row (e.g. for i in range(len(self.rows)))
        #     loop over each col
        #          is i,j in "conflict" with row, column? - same row, column or subgrid?
        #               does i, j have a list in it?
        #                    remove assignment from that spot (use remove_if_exists - defined above)



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
    #create fringe
    #while fringe isn't empty
    #    grab a state from fringe - let's call it curr
    #    if curr is the goal
    #         return it, we're done!!
    #    else if curr is *not* a fail state
    #         find the position of the most constrained cell
    #         for each number we could possibly put there
    #              create a deep copy of the board
    #              put that number/assignment on that deepcopy
    #              add the deepcopy to fringe
    #if we reach this point, then we never found the goal
    

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
    #create fringe
    #while fringe isn't empty
    #    grab a state from fringe - let's call it curr
    #    if curr is the goal
    #         return it, we're done!!
    #    else if curr is *not* a fail state
    #         find the position of the most constrained cell
    #         for each number we could possibly put there
    #              create a deep copy of the board
    #              put that number/assignment on that deepcopy
    #              add the deepcopy to fringe
    #if we reach this point, then we never found the goal

# the Stack and Queue classes for DFS and BFS
from typing import Generic, List, TypeVar

# stack element type variable
S = TypeVar("S")
# queue element type variable
Q = TypeVar("Q")


class Stack:
    """A last in first out (LIFO) stack representation where elements are pushed and popped from the top. Think of a stack of plates, where you can't remove or add a plate in the middle, only take from, or add to, the top.
        
        Attributes:
        the_stack - the list that holds the elements of our stack
        """
    
    def __init__(self, initial: List[S] = []) -> None:
        """Constructor for a stack, simply sets the stack up with
            the given list if any is provided otherwise empty
            
            Args:
            initial - optional list of elements to fill the stack with
            """
        # can't have lists (mutable objects in general) as default values as
        # the default is shared among all instances. need to copy here to
        # avoid issues with aliases
        self.the_stack: List[S] = initial[:]
    
    def __str__(self) -> str:
        """String representation of the stack"""
        return f"The stack contains: {self.the_stack}"

    def is_empty(self) -> bool:
        """Check if stack has no elements
            
            Returns:
            True if stack has no elements, False otherwise
            """
        return len(self.the_stack) == 0

    def push(self, elt: S) -> None:
        """Add element (elt) to top of stack
            
            Args:
            elt - an item to add to the stack
            """
        self.the_stack.append(elt)
        
    def pop(self) -> S:
        """Remove and return the top item in the stack (corresponds to the last
            item in the list)
            
            Returns:
            the most recently added element
            """
        return self.the_stack.pop()


class Queue:
    """A first in first out (FIFO) queue representation where elements are pushed at the end of the queue and popped from the front. Think of a line at an amusement park where new people join (pushed) the line at the back and are
        let in (popped) from the front
        
        Attributes:
        the_queue - the list that holds the elements of our queue
        """
    
    def __init__(self, initial: List[Q] = []) -> None:
        """Constructor for a queue, simply sets the queue up with the given list if any is provided otherwise empty
            
            Args:
            initial - optional list of elements to fill the queue with
            """
        
        # can't have lists (mutable objects in general) as default values as
        # the default is shared among all instances. need to copy here to
        # avoid issues with aliases
        self.the_queue: List[Q] = initial[:]
    
    def __str__(self) -> str:
        """String representation of the queue"""
        return f"The queue contains: {self.the_queue}"

    def is_empty(self) -> bool:
        """Check if queue has no elements
            
            Returns:
            True if queue has no elements, False otherwise
            """
        return len(self.the_queue) == 0

    def push(self, elt: Q) -> None:
        """Add element (elt) to end of queue
            
            Args:
            elt - an item to add to the queue
            """
        self.the_queue.append(elt)
        
    def pop(self) -> Q:
        """Remove and return the start of the queue (corresponds to the first
            item in the list)
            
            Returns:
            the oldest added element
            """
        return self.the_queue.pop(0)

#PART 1 - alias

x = [1,2,3]

t = x #t is an alias for x

t.pop()

print(f"t is {t}")
print(f"x is {x}")

#PART 2 - list copy

z = x[:] #z is a copy of x

z.pop()

print(f"z is {z}")
print(f"x is {x}")

#PART 3 - list copy isn't always enough

q = [[1,2,3], [4,5,6], [7,8,9]]
v = q[:]

#v looks like its a copy of q. let's test that assumption

v[0][1] = 222 #change the 2 to 222

print(f"q is {q}")
print(f"v is {v}")

#ACK - with nested lists, just using [:] to copy a list
#   isn't sufficient. We need to "deep copy"

#PART 4 - the copy library

import copy

r = copy.deepcopy(q)
r[0][2] = 333

print(f"r is {r}")
print(f"q is {q}")

#yay, they're different!

#PART 5 - some structures to help with problem solving via search

#creating a stack
mys = Stack()
mys.push('d')
mys.push('c')
mys.push('b')
print(mys)
print(mys.pop())



