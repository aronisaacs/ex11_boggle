import tkinter as tki
from typing import Callable, Dict, List, Any, Tuple
from boggle_board_randomizer import *
Board = List[List[str]]


class BoggleBoardGui:

    def __init__(self, board: Board) -> None:
        """in this function we intialize the main frames"""
        root = tki.Tk()
        root.title("Boggle")
        root.resizable(False, False)
        root.geometry("500x500")
        self.__main__window = root
        self.buttons: Dict[(int, int), tki.Button] = {}
        self.__outer_frame = tki.Frame(root, bg='gray')
        self.__outer_frame.pack(side=tki.TOP, fill=tki.BOTH, expand=True)
        self._current_word_label = tki.Label(
            self.__outer_frame, text="random word", width=40, bg="red", font=("Helvetica", 30))
        self._current_word_label.pack(side=tki.TOP)
        self._grid_frame = tki.Frame(self.__outer_frame, bg="blue")
        self._grid_frame.pack(side=tki.LEFT, fill=tki.BOTH, expand=True)
        self.__data_frame = tki.Frame(self.__outer_frame, bg="green")
        self.__data_frame.pack(side=tki.RIGHT, fill=tki.BOTH)
        self.__create_buttons_in_grid_frame(board)
        self.__config_data_frame()
        self.countdown([3, 0, 1])
        self.__main__window.after(
            183*1000, self.__main__window.destroy)

    def countdown(self, time: List[int]):
        time_min = time[0]
        time_ten_sec = time[1]
        time_dig_sec = time[2]
        if not (time_min == 0 and time_ten_sec == 0 and time_dig_sec == 0):
            if time_ten_sec == 0 and time_dig_sec == 0:
                time_min -= 1
                time_dig_sec = 9
                time_ten_sec = 5
            elif time_ten_sec == 0:
                time_dig_sec -= 1
            elif time_dig_sec == 0:
                time_ten_sec -= 1
                time_dig_sec = 9
            else:
                time_dig_sec -= 1
            time[0], time[1], time[2] = time_min, time_ten_sec, time_dig_sec
            self.__countdown_label["text"] = f"{time_min}:{time_ten_sec}{time_dig_sec}"
            self.__main__window.after(1000, self.countdown, time)

    def __config_data_frame(self) -> None:
        self.__create_word_list()
        self.__create_countdown_label()
        self.__create_score_label()

    def __create_countdown_label(self) -> None:
        self.__countdown_frame = tki.Frame(self.__data_frame, bg="yellow")
        self.__countdown_frame.pack(side=tki.TOP, fill=tki.BOTH)
        self.__countdown_label = tki.Label(
            self.__countdown_frame, bg="blue", text="3:00", width=10, font=("Helvetica", 20))
        self.__countdown_label.pack(side=tki.TOP, fill=tki.BOTH)

    def __create_score_label(self) -> None:
        self.__score_frame = tki.Frame(self.__data_frame, bg="yellow")
        self.__score_frame.pack(side=tki.BOTTOM, fill=tki.BOTH)
        self.__score_label = tki.Label(
            self.__score_frame, bg="yellow", text="score:   ", width=10, font=("Helvetica", 20))
        self.__score_label.pack(side=tki.TOP,)

    def __create_word_list(self) -> None:
        self._words_list_frame = tki.Frame(self.__data_frame, bg="yellow")
        self._words_list_frame.pack(side=tki.BOTTOM, fill=tki.BOTH)
        self.__scrollbar = tki.Scrollbar(
            self._words_list_frame, orient="vertical")
        self.__found_words_listbox = tki.Listbox(
            self._words_list_frame, height=23, yscrollcommand=self.__scrollbar.set)
        self.__scrollbar.config(command=self.__found_words_listbox.yview)
        self.__scrollbar.pack(side=tki.RIGHT, fill=tki.Y)
        self.__found_words_listbox.pack(
            side=tki.BOTTOM, fill=tki.BOTH)

    def __create_buttons_in_grid_frame(self, board: Board) -> None:
        for i in range(4):  # creating the grid sturctures
            tki.Grid.columnconfigure(self._grid_frame, i, weight=1)
            tki.Grid.rowconfigure(self._grid_frame, i, weight=1)
        for row in range(len(board)):
            for col in range(len(board[0])):
                self.buttons[(row, col)] = self._make_button(
                    board[row][col], row, col)

    def _make_button(self, button_chars, row: int, col: int) -> tki.Button:
        button = tki.Button(
            self._grid_frame, text=button_chars, background="grey")
        button.grid(row=row, column=col, rowspan=1,
                    columnspan=1, sticky=tki.NSEW)

        def change_color(color: str) -> None:
            print("chanigs")
            print(button["background"])
            button["background"] = color
            print(button["background"])
        button.change_color = change_color
        return button

    def set_on_enter_click(self, cmd: Callable) -> None:
        self.__main__window.bind('<Return>', cmd)

    def set_button_command(self, button_cell: tuple[int, int], cmd: Callable) -> None:
        self.buttons[button_cell].configure(command=cmd)

    def set_display(self, word: str) -> None:
        self._current_word_label["text"] = word

    def set_score(self, score: str) -> None:
        self.__score_label["text"] = score

    def add_word_to_list(self, word: str) -> None:
        self.__found_words_listbox.insert("end", word)

    def run(self):
        self.__main__window.mainloop()
