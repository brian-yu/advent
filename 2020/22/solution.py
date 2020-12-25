from collections import deque

file = open('input.txt')

player_1_cards, player_2_cards = [
    deque(
        map(int, chunk.split('\n')[1:])
    ) for chunk in file.read().rstrip('\n').split('\n\n')
]

class Deck:
    def __init__(self, cards):
        self.cards = deque(cards)
    
    def draw(self):
        return self.cards.popleft()
    
    def add_to_bottom(self, card):
        self.cards.append(card)
    
    def copy_n(self, n):
        return Deck(list(self.cards)[:n])
    
    def copy(self):
        return self.copy_n(len(self.cards))
    
    def score(self):
        return sum(
            (i + 1) * card for i, card in enumerate(reversed(self.cards))
        )
    
    def __len__(self):
        return len(self.cards)

    def __bool__(self):
        return len(self.cards) > 0
    
    def __hash__(self):
        return hash(str(self.cards))

def combat(deck_1, deck_2):
    while deck_1 and deck_2:
        player_1_card = deck_1.draw()
        player_2_card = deck_2.draw()

        if player_1_card > player_2_card:
            deck_1.add_to_bottom(player_1_card)
            deck_1.add_to_bottom(player_2_card)
        else:
            deck_2.add_to_bottom(player_2_card)
            deck_2.add_to_bottom(player_1_card)
    
    if deck_1:
        return deck_1
    
    return deck_2


player_1_deck = Deck(player_1_cards)
player_2_deck = Deck(player_2_cards)

winning_deck = combat(player_1_deck.copy(), player_2_deck.copy())

print(winning_deck.score())

def recursive_combat(deck_1, deck_2):
    seen = set()
    
    while deck_1 and deck_2:
        round_hash = hash(deck_1) + hash(deck_2)
        if round_hash in seen:
            return 1
        seen.add(round_hash)

        player_1_card = deck_1.draw()
        player_2_card = deck_2.draw()

        winner = None

        if player_1_card <= len(deck_1) and player_2_card <= len(deck_2):
            winner = recursive_combat(
                deck_1.copy_n(player_1_card),
                deck_2.copy_n(player_2_card),
            )
        elif player_1_card > player_2_card:
            winner = 1
        else:
            winner = 2
        
        if winner == 1:
            deck_1.add_to_bottom(player_1_card)
            deck_1.add_to_bottom(player_2_card)
        else:
            deck_2.add_to_bottom(player_2_card)
            deck_2.add_to_bottom(player_1_card)
        
    if deck_1:
        return 1
    
    return 2


recursive_combat(player_1_deck, player_2_deck)

if player_1_deck:
    print(player_1_deck.score())
else:
    print(player_2_deck.score())