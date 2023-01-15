#####################################################
# This is the model o the boggle program: it is completely independant from everything else.


from typing import Tuple

from ex11_utils import *

Coordinate = tuple[int]
Path = List[Coordinate]
Board = List[List[str]]


class BoggleModel:

    def __init__(self, board: Board, words_dict: List[str]):
        self.legal_words_dict = words_dict
        self.substring = ''
        self.score = 0
        self.path: Path = []
        self.found_words: Dict[str] = {}
        self.time = 0
        self.dice_list: Path = []
        self.__board = board

    def path_checking_reaction(self, letter, coordinate) -> bool:
        # This function is called whenever any button is pressed.
        if check_if_legal_path(self.__board, self.path + [coordinate]):
            self.path.append(coordinate)
            self.substring += letter
            return True
        else:
            self.path = []
            self.substring = ''
            return False

    def word_checking_reaction(self) -> int:
        # This function is called when the "enter" key is hit:
        WORD__VALID = 1
        WORD_NOT_NEW = 2
        WORD_ILLEGAL = 0
        word_status = WORD_ILLEGAL
        if binary_search(self.substring, self.legal_words_dict):
            if self.substring not in self.found_words:
                self.found_words[self.substring] = ""
                self.score += len(self.path) ** 2
                word_status = WORD__VALID
            else:
                word_status = WORD_NOT_NEW
        self.substring = ''
        self.path = []
        return word_status

    def get_current_substring(self) -> str:
        return self.substring

    def get_current_score(self) -> int:
        return self.score

    def get_current_path(self) -> Path:
        return self.path
