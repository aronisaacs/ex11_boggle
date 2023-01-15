#########
#This file tests ex11_utils.py
##########


from boggle_board_randomizer import *
from ex11_utils import *


EXAMPLE_BOARD = 		[
	['E', 'W', 'D', 'R'],
	['T', 'P', 'A', 'E'],
	['E', 'O', 'E', 'QU'],
	['A', 'H', 'P', 'N']
						]

WORD_LIST = ['HOPE', 'DEEP']
WORD_SET = ['HOPE', 'DEEP', 'HELLO', 'ROW']

def create_dict_list():
	with open("boggle_dict.txt") as f:
		words = []
		for line in f:
			words.append(line.strip())
	return words

FULL_DICTIONARY = create_dict_list()
	
Dictionary = create_dict_list()
#random_board = randomize_board()
paths = max_score_paths(EXAMPLE_BOARD, Dictionary)

def print_words_from_paths(paths, board):
	words_list = [path_to_word(path, board) for path in paths]
	return words_list

def big_board_generator(size):
	big_board = [[chr(random.randint(ord('A'), ord('Z'))) for j in range(size)] for i in range(size)]
	return big_board



def test_path_to_word():
	assert 'DEEP' == path_to_word([(0,2), (1,3), (2,2), (3,2)], EXAMPLE_BOARD)
	assert 'HOPE' == path_to_word([(3,1), (2,1), (1,1), (2,2)], EXAMPLE_BOARD)

def test_cell_in_board():
	assert cell_in_board((0,0), EXAMPLE_BOARD)
	assert cell_in_board((3,2), EXAMPLE_BOARD)
	assert not cell_in_board((4,3), EXAMPLE_BOARD)
	assert not cell_in_board((-1,3), EXAMPLE_BOARD)

def test_path_intersects():
	assert not path_intersects([(1,1),(0,1),(1,0),(0,0), (3,0)])
	assert path_intersects([(0,0),(1,1),(0,1),(1,0),(0,0)])

def test_is_neighbor():
	assert is_neighbor((0,0), (1,1))
	assert is_neighbor((0,1), (1,0))
	assert not is_neighbor((2,2), (2,2))
	assert not is_neighbor((1,0), (3,0))

def test_check_if_legal_path():
	assert check_if_legal_path(EXAMPLE_BOARD, [(1,1),(0,0),(1,0),(2,0)])
	#this path is not connected:
	assert not check_if_legal_path(EXAMPLE_BOARD, [(1,1),(0,1),(1,0),(0,0),(3,0)])
	#this path intersects itself:
	assert not check_if_legal_path(EXAMPLE_BOARD, [(0,0),(1,1),(0,1),(1,0),(0,0)])
	#this path contains a square not on the board:
	assert not check_if_legal_path(EXAMPLE_BOARD, [(1,1),(0,0),(1,0),(2,0),(3,0),(4,0)])

def test_is_valid_word_path():
	assert is_valid_path(EXAMPLE_BOARD, [(0,2), (1,3), (2,2), (3,2)], WORD_SET)
	assert is_valid_path(EXAMPLE_BOARD, [(3,1), (2,1), (1,1), (2,2)], WORD_SET)
	assert not is_valid_path(EXAMPLE_BOARD, [(3,1), (2,1), (1,1), (1,2)], WORD_SET)
	assert not is_valid_path(EXAMPLE_BOARD, [(0,3), (2,1), (0,1)], WORD_SET)


def test_sort_words_alphebetically():
	random_set = ['HOPE', 'DEEP', 'HELLO', 'ROW']
	assert ['DEEP', 'HELLO', 'HOPE', 'ROW'] == sort_words_alphebetically(random_set)

def test_binary_search_full_word():

	assert binary_search('AARDVARK', FULL_DICTIONARY)
	assert binary_search('ABACTERIAL', FULL_DICTIONARY)
	assert not binary_search('AABBBBD', FULL_DICTIONARY)
	assert not binary_search('ABACT', FULL_DICTIONARY)

def test_binary_search_substring():
	assert binary_search('AARDVARK', FULL_DICTIONARY)
	assert binary_search('ABACTERIAL', FULL_DICTIONARY)
	assert binary_search('ABACT', FULL_DICTIONARY, False)
	assert not binary_search('AABBBBD', FULL_DICTIONARY)

def test_valid_next_cell_list():
	assert [(3, 0), (2, 1), (3, 1)] == valid_next_cell_list([(1,1),(0,0),(1,0),(2,0)], EXAMPLE_BOARD)
	assert [(0, 0), (1, 0), (2, 0), (0, 1), (0, 2), (2, 2)] == valid_next_cell_list([(1,2), (2,1), (1,1)], EXAMPLE_BOARD)
	
FULL_FOUND_WORD_LIST = ['EWT', 'EPOPEE', 'EPEE', 'WET', 'WEPT', 'WAP', 'WAD', 'WADE', 'WADER', 'WAE', 'WAR', 'WARD',
 'WARE', 'WARED', 'DAW', 'DAWT', 'DAP', 'DAE', 'DARE', 'DRAW', 'DRAP', 'DRAPE', 'DRAPET', 'DREE', 'DEAW', 'DEAR',
  'DEE', 'DEEP', 'DEEN', 'RAW', 'RAP', 'RAPE', 'RAPT', 'RAD', 'RADE', 'RED', 'REAP', 'READ', 'REE', 'REEN', 'TEW',
   'TEPA', 'TEPEE', 'TEA', 'TWP', 'TWA', 'TWAE', 'TOE', 'TOEA', 'TOP', 'TOPE', 'TOPEE', 'TOAD', 'TOPH', 'TOPHE', 'PET',
    'PEW', 'PEA', 'PEAHEN', 'PEH', 'POT', 'POTE', 'POET', 'POA', 'POH', 'POEP', 'POP', 'POPE', 'PAW', 'PAD', 'PADRE',
	'PAR', 'PARD', 'PARDEE', 'PARE', 'PARED', 'PEAR', 'PEARE', 'PEP', 'PEPO', 'PEE', 'PEED', 'PEER', 'PEN', 'AWE',
	'AWETO', 'APE', 'APT', 'APO', 'ARD', 'ARE', 'ARED', 'EAR', 'EARD', 'EEN', 'ERA', 'OPE', 'OPT', 'OPA', 'OPAQUE',
	'OPAQUED', 'OPAQUER', 'OPEN', 'OAR', 'OARED', 'OPEPE', 'EARED', 'EPOPT', 'EPHA', 'QUA', 'QUAD', 'QUARE', 'QUEP',
	'QUEER', 'QUEEN', 'AHEAP', 'AHEAD', 'HET', 'HETE', 'HEP', 'HEPT', 'HEPAR', 'HAE', 'HAET', 'HAO', 'HOT', 'HOTE',
	'HOE', 'HOA', 'HOP', 'HOPE', 'HOAR', 'HOARD', 'HOARED', 'HOAED', 'HEAP', 'HEAD', 'HEADER', 'HEAR', 'HEARD',
	'HEARE', 'HEED', 'HEN', 'PHO', 'PHOT', 'PHEER', 'NEP', 'NEAP', 'NEAR', 'NEARED', 'NEE', 'NEED']

PATH_OF_LENGTH_5 = ['WADER', 'WARED', 'DRAPE', 'DRAPE', 'DRAPE', 'TEPEE', 'TEPEE', 'TOPEE', 'TOPHE', 'TOPHE', 'TOPEE',
 'PADRE', 'PARED', 'PEARE', 'AWETO', 'OPAQUE', 'OPAQUE', 'OARED', 'OPEPE', 'OPEPE', 'EARED', 'EPOPT', 'AHEAP', 'AHEAD',
  'HEPAR', 'HOARD', 'HOAED', 'HEPAR', 'HEARD', 'HEARE', 'PHEER', 'PEARE']

WORD_OF_LENGTH_5 = ['WADER', 'WARED', 'DRAPE', 'DRAPE', 'DRAPE', 'TEPEE', 'TEPEE', 'TOPEE', 'TOPHE', 'TOPHE', 'TOPEE',
 'PADRE', 'PARED', 'PEARE', 'AWETO', 'OARED', 'OPEPE', 'OPEPE', 'EARED', 'EPOPT', 'QUARE', 'QUEER', 'QUEEN', 'AHEAP',
  'AHEAD', 'HEPAR', 'HOARD', 'HOAED', 'HEPAR', 'HEARD', 'HEARE', 'PHEER', 'PEARE']

def test_max_score_paths():
	assert FULL_FOUND_WORD_LIST == print_words_from_paths(max_score_paths(EXAMPLE_BOARD,FULL_DICTIONARY), EXAMPLE_BOARD)


def test_find_length_n_paths():
	assert PATH_OF_LENGTH_5 == print_words_from_paths(find_length_n_paths(5, EXAMPLE_BOARD, FULL_DICTIONARY), EXAMPLE_BOARD)

def test_find_length_n_words():
	assert WORD_OF_LENGTH_5 == print_words_from_paths(find_length_n_words(5, EXAMPLE_BOARD, FULL_DICTIONARY), EXAMPLE_BOARD)


#############################################################################################################################
# WATER COOLER CORNER: THE FOLLOWING CODE IS VERY IMPORTANT IF OUR COURSE WAS ONE OF COMPLEXITY AND RUNTIME. OTHERWISE,
#IT IS A GIANT WASTE OF TIME AND SIMPLY ME PROCRASTINATING CAUSE I DON'T WANT TO LEARN HOW TO WRITE A GUI.
##############################################################################################################################

#print(print_words_from_paths(max_score_paths(big_board_generator(100), FULL_DICTIONARY), big_board_generator(100)))
#print(len(max_score_paths(big_board_generator(8), FULL_DICTIONARY)))
#print(words_found)

def max_score_backtracking(board: Board, words: Iterable[str]) -> List[Path]:
    n = 0
    paths_found = chosen_filter(n, board, words, max_score_filter)
    return paths_found.amount_of_backtracking


#for board_size in range(100):
	#print(board_size, max_score_backtracking(big_board_generator(board_size), FULL_DICTIONARY))

def data_analysis(num):
	cum_returns = 0
	for _ in range(num):
		num_backtracks = max_score_backtracking(randomize_board(),FULL_DICTIONARY)
		cum_returns += num_backtracks
	return cum_returns / (16 * num)

#print(data_analysis(1000))

