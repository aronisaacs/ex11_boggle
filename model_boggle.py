#####################################################
# This is the model o the boggle program: it is completely independant from everything else.


from typing import *

from ex11_utils import *

Path = list[int,int]
Coordinate = tuple(int, int)

class BoggleGame:

	def __init__(self):
		self.legal_words_dict = ''
		self.substring = ''
		self.score = 0
		self.path: Path = []
		self.found_words: list[str] = []
		self.time = 0
		self.dice_list: Path = []

	def path_checking_reaction(self, letter, coordinate) -> bool:
		#This function is called whenever any button is pressed.
		if check_if_legal_path(self.path, coordinate):
			self.path += coordinate
			self.substring += letter
			return True
		else:
			self.path = []
			self.substring = ''
			return False
	
	def word_checking_reaction(self) -> bool:
		#This function is called when the "enter" key is hit:
		word_is_valid = False
		if binary_search(self.substring, self.legal_words_dict):
			self.found_words.append(self.substring)
			self.score += len(self.path) ** 2
			word_is_valid = True
		self.substring = ''
		self.path = []
		return word_is_valid





