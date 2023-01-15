#####################################
# THE MAIN UTILITIES FILE:
#####################################


import copy
from typing import List, Tuple, Callable, Iterable, Optional,Dict
from bisect import bisect_left


Board = List[List[str]]
Path = List[Tuple[int, int]]
Coordinate = Tuple[int, int]
SortedWords = list[str]


class PathsFound():
    def __init__(self):
        self.path_list : List[str]= []
        self.found_words_dict: Dict[str,Path] = {}
        self.amount_of_backtracking = 0

def path_to_word(path: Path, board: Board ) -> str:
    '''
    This function accepts a LEGAL path and a board, and returns the represented word.
    '''
    word = ''
    for cell in path:
        row, col = cell[0], cell[1]
        word += board[row][col]
    return word

def cell_in_board(cell: Coordinate, board: Board) -> bool:
    '''
    boolean function that returns whether a certain cell is in the boundaries of the board.
    '''
    return (0 <= cell[0] <= len(board) - 1) and  (0 <= cell[1] <= len(board[0]) - 1)

def path_intersects(path: Path) -> bool:
    '''
    A boolean function that returns whether a path intersects itself.
    '''
    return not len(set(path)) == len(path)


def is_neighbor(base_cell: Coordinate, previous_cell: Coordinate) -> bool:
    '''
    This function accepts two cell coordinates and accepts whether they are neighbors of each other or not.
    '''
    y1, x1, y2, x2 = base_cell[0], base_cell[1], previous_cell[0], previous_cell[1]
    return abs(y1-y2) <= 1 and abs(x1-x2) <= 1 and not (x1 == x2 and y1 == y2)


def check_if_legal_path(board: Board, path: Path) -> bool:
    '''
    This functions check if a certain given path is legal: Note that it does not check to see if
    the associated word is in the dictionary or not.
    '''
    if not path:
        return True
    if path_intersects(path):
        return False 
    path_length =len(path)
    if not cell_in_board(path[0],board):
        return False
    for i in range(1, path_length):
        if not cell_in_board(path[i],board):
            return False
        if not is_neighbor(path[i], path[i-1]):
            return False
    return True



def is_valid_path(board: Board, path: Path, words: Iterable[str]) -> Optional[str]:
    '''
    This function checks to see if a given path is both legal and represents a legal word in the dictionary.
    If both of these are true, it returns True; otherwise, it returns false.
    Note that this is one of the required functions, and may be tested by itself: since it tests only one word, it
    isn't worth it to convert the list into an ordered list in order to implement binary search.
    '''
    if check_if_legal_path(board,path):
        candidate_word = path_to_word(path, board)
        if candidate_word in words:
            return candidate_word
    return None

#################################################################################################################
# Note THAT UP UNTIL THIS POINT, ALL OF THE FUNCTIONS HAVE BEEN TO ENABLE THIS LAST FUNCTION is_valid_path.
# HOWEVER, ALL OF THE ABOVE FUNCTIONS ARE NOT USED FOR THE THREE FUNCTIONS AHEAD THAT USE BACKTRACKING.
##################################################################################################################


def sort_words_alphebetically(words:Iterable) -> SortedWords:
    '''
    This function accepts some iterable data type of words and sorts them alphebetically. Note
    That the original input is not changed.
    '''
    return sorted(words)


def binary_search(letter_string: str, sorted_words_list: SortedWords, full_word=True) -> bool:
    '''
    This function accepts a specific word and a sorted words list, as well as a boolean called full_word.
    If full_word is set to be True (which it is by default), then the function will only return True if that exact
    word is in the dictionary. If full_word is set to be false, then the function checks whether there is at least
    one word in the dictionary that begins with the string accepted by the function.
    '''
    index_found = bisect_left(sorted_words_list,letter_string)
    if full_word:
        return index_found != len(sorted_words_list) and sorted_words_list[index_found] == letter_string
    else:
        return index_found < len(sorted_words_list) and  letter_string in sorted_words_list[index_found]


def valid_next_cell_list(path: Path, board: Board) -> List[Coordinate]:
    '''
    This function accepts an existing path and a board, and returns a list of acceptable cells that one can jump
    to to add more letters to the existing word string.
    '''
    result= []
    base_point = path[-1]
    for x in [-1,0,1]:
        for y in [-1,0,1]:
            candidate_cell = (base_point[0] + y, base_point[1] + x)
            if  candidate_cell not in path and cell_in_board(candidate_cell,board):
                result.append(candidate_cell)
    return result


###############################################################################################
# PART 2: SUB-FUNCTIONS FOR FINDING ALL WORDS WITH VARIOUS REQUIREMENTS:
###############################################################################################

def add_to_words_dict(path:Path, paths_found: PathsFound,board):
    word = path_to_word(path,board)
    if word in paths_found.found_words_dict:
        if len(paths_found.found_words_dict[word]) < len(path):
            paths_found.found_words_dict[word] = path
    else:
        paths_found.found_words_dict[word] = copy.deepcopy(path)
def find_words_helper(path: Path, sub_string: str, n: int, board: Board, words_found: PathsFound, sorted_dict: SortedWords, filter: Callable) -> None:
    '''
    This is the main backtracking helper function, that does all of the heavy logical lifting.
    '''
    if filter(path, sub_string, n):
        if binary_search(sub_string, sorted_dict):
            words_found.path_list.append(path[:])
            if filter == max_score_filter:
                add_to_words_dict(path,words_found,board)
            else:
                #optional line that counts the amount of times the function returns:
                words_found.amount_of_backtracking += 1
                return
    if not binary_search(sub_string, sorted_dict, False):
        #optional line that counts the amount of times the function returns:
        words_found.amount_of_backtracking += 1
        return
    for cell in valid_next_cell_list(path, board):
        path.append(cell)
        original_length = len(sub_string)
        sub_string += board[cell[0]][cell[1]]
        find_words_helper(path, sub_string, n, board, words_found, sorted_dict, filter)
        path.pop()
        sub_string = sub_string[:original_length]

def chosen_filter(n: int, board: Board, words: Iterable[str], filter) -> PathsFound:
    #This function accepts a certain filter, and then iterates over the entire gameboard, recursively calling the helper function
    #with the desired filter for each cell.
    sorted_words_list = sort_words_alphebetically(words)
    words_found = PathsFound()
    for i in range(len(board)):
        for j in range(len(board[0])):
            initial_letter = path_to_word([(i,j)],board)
            find_words_helper([(i,j)], initial_letter, n, board, words_found, sorted_words_list, filter)
    if filter == max_score_filter:
        return words_found
    return words_found

def path_length_filter(path: Path, subs_string: str, n: int) -> bool:
    #This filter checks to see if the given path length is exactly equal to the given n:
    if len(path) == n:
        return True
    return False

def word_length_filter(path: Path, sub_string: str, n: int) -> bool:
    # This filter checks to see if the given substring is exactly equal to the given n:

    if len(sub_string) == n:
        return True
    return False

def max_score_filter(path: Path, sub_string: str, n: int) -> bool:
    #This filter  is supposed to check to see if the word has already been recorded with a higher score,
    #though i'm too tired to write or think about the logic right now.
    return True

########################################################################################################
# MAIN PART: FINDS ALL OF THE WORDS ACCORDING TO EACH ONE'S REQUIREMENTS:
########################################################################################################

def find_length_n_paths(n: int, board: Board, words: Iterable[str]) -> List[Path]:
    paths_found = chosen_filter(n, board, words, path_length_filter)
    return paths_found.path_list


def find_length_n_words(n: int, board: Board, words: Iterable[str]) -> List[Path]:
    paths_found = chosen_filter(n, board, words, word_length_filter)
    return paths_found.path_list


def max_score_paths(board: Board, words: Iterable[str]) -> List[Path]:
    n = 0
    paths_found = chosen_filter(n, board, words, max_score_filter)
    return [paths_found.found_words_dict[word] for word in paths_found.found_words_dict]


############################################################################################################
 

