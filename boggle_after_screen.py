from tkinter import ttk
import tkinter as tki
from typing import Callable, Dict, List, Any, Tuple
from boggle_board_randomizer import *
Board = List[List[str]]
QUIT = 0
CONTINUE = 1


class BoggleBetweenScreenGui():
    def __init__(self, final_score: int = 0, start: bool = False) -> None:
        QUIT = 0
        CONTINUE = 1
        if start:
            output = f"Boggle"
            button_text = "Play"
        else:
            output = f"You have scored {final_score} points!"
            button_text = "Play Again"
        root = tki.Tk()
        root.title("Boggle")
        root.resizable(False, False)
        root.geometry("500x500")
        self.users_choice = QUIT
        self.__main__window = root
        style = ttk.Style()
        style.configure("TButton", font=("Arial", 20, "bold"), padding=10)
        self._score_label = ttk.Label(self.__main__window,
                                      text=output, font=('Arial', 20, 'bold'))
        self._score_label.pack()

        exit_button = ttk.Button(
            self.__main__window, text="Exit", command=self.on_exit, style="TButton")
        exit_button.pack(side=tki.LEFT)

        continue_button = ttk.Button(
            root, text=button_text, command=self.on_continue, style="TButton")
        continue_button.pack(side=tki.RIGHT)

    def on_exit(self) -> None:
        self.users_choice = QUIT
        self.__main__window.destroy()

    def on_continue(self) -> None:
        self.users_choice = CONTINUE
        self.__main__window.destroy()

    def run(self) -> None:
        self.__main__window.mainloop()
