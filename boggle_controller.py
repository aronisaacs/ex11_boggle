from boggle_board_gui import BoggleBoardGui
import tkinter as tki
from typing import Callable, Dict, List, Any
from boggle_board_randomizer import *
from boggle_model import BoggleModel
from boggle_after_screen import BoggleBetweenScreenGui
Board = List[List[str]]
QUIT = 0
CONTINUE = 1


def create_dict_list() -> List[str]:
    with open("boggle_dict.txt") as f:
        words = []
        for line in f:
            words.append(line.strip())
    return words


class BoggleRoundController:
    def __init__(self, words_dict) -> int:
        self.active_color = "blue"
        self.non_active_color = "grey"
        self.board: Board = randomize_board()
        self.board_gui = BoggleBoardGui(self.board)
        self._model = BoggleModel(self.board, words_dict)
        for button_cell in self.board_gui.buttons:
            cmd = self.create_button_cmd(button_cell)
            self.board_gui.set_button_command(button_cell, cmd)
        self.board_gui.set_on_enter_click(self.submit_word_cmd)
        self.board_gui.set_display("Press Enter to Submit")
        self.board_gui.run()
        self.final_score = self._model.get_current_score()

    def create_button_cmd(self, button_cell: tuple[int]) -> Callable:
        def fun() -> None:
            current_path = self._model.get_current_path()
            print(button_cell)
            if self._model.path_checking_reaction(self.board[button_cell[0]][button_cell[1]], button_cell):
                self.board_gui.set_display(self._model.get_current_substring())
                self.board_gui.set_score(
                    "score: " + str(self._model.get_current_score()))
                self.board_gui.buttons[button_cell].change_color(
                    self.active_color)
            else:
                self.board_gui.set_display("Illegal Move!")
                self.reset_path(current_path)
        return fun

    def submit_word_cmd(self, event) -> None:
        current_word = self._model.get_current_substring()
        current_path = self._model.get_current_path()
        word_is_legit: int = self._model.word_checking_reaction()
        if word_is_legit == 1:
            self.board_gui.set_score(
                "score: " + str(self._model.get_current_score()))
            self.board_gui.add_word_to_list(current_word)
            self.board_gui.set_display("Great job!")
        elif word_is_legit == 2:
            self.board_gui.set_display("word already found :(")
        else:
            self.board_gui.set_display("Illegal Word :(")
        self.reset_path(current_path)

    def reset_path(self, path) -> None:
        for button_cord in path:
            self.board_gui.buttons[button_cord].change_color(
                self.non_active_color)


class BoggleBetweenController():
    def __init__(self, final_score: int = 0, start: bool = False) -> None:
        self.users_choice = QUIT
        self.gui = BoggleBetweenScreenGui(final_score, start)
        self.gui.run()
        self.users_choice = self.gui.users_choice


if __name__ == "__main__":
    words_dict: List[str] = sorted(create_dict_list())
    game_on = True
    after = BoggleBetweenController(0, True)
    if after.users_choice == QUIT:
        game_on = False
    while game_on:
        game_on = False
        round = BoggleRoundController(words_dict)
        final_score = round.final_score
        after = BoggleBetweenController(final_score)
        print(after.users_choice)
        if after.users_choice == QUIT:
            game_on = False
        else:
            game_on = True
