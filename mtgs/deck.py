from random import shuffle

class Deck(object):
	'''
	This class could also be called "Player", contains a list of cards for each player to
	play the game.
	'''

	def __init__(self):
		self.deck = []

	def get_deck(self):
		return self.deck

	def fill_deck(self, deck_list):
		'''
		Fill in deck object from text file of cards in the following format:
		<Number of card> Card
		<Number of card> Card
		'''
		for line in open(deck_list, 'r'):
			number_of_cards, card = line.split()
			for c in range(0, int(number_of_cards)):
				self.deck.append(card)
		return self.deck

#test
def main():
	deck = Deck()
	deck_one = deck.fill_deck('../docs/Deck Lists/deck_list.txt')
	shuffle(deck_one)
	print deck_one

main()