import random

suits = ('Hearts','Diamonds','Spades','Clubs')
ranks = ('Ace','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King')
value = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':11,'Queen':12,'King':13,'Ace':14}

class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = value[rank]
    
    def __str__(self):
        return self.rank + " of " + self.suit
    
#two_of_spades = Card("spades","2")
#print(two_of_spades)
#print(value[two_of_spades.rank])
#print(two_of_spades.value)

#two_of_spades = Card("Spades","Two")
#jack_of_clubs = Card("Clubs","jack")
#print(jack_of_clubs.value)
#print(two_of_spades.value)
#print( jack_of_clubs.value < two_of_spades.value )

#Creating a Deck class that can:
    # Create all 53 cards objects
    # Hold as a list of card Objects - it will return Card Class object instances , not normal data types
    # Shuffle the Deck through a method call - Using Random library: shuffle() func
    # Deal cards from the deck object - Using pop method from card list

class Deck:
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)

    
    def shuffle(self):
        random.shuffle(self.all_cards) #it is an IN PLACE function, it doesn't return any alue
        return self.all_cards

    def deal_one(self):
        return self.all_cards.pop()


#new_deck = Deck()
#print(new_deck.all_cards[0])
#print(new_deck.all_cards[-1])

#for card_objects in new_deck.all_cards:
    #print(card_objects)

#for new in new_deck.shuffle():
#    print(new)

#new_deck.shuffle()
#print(new_deck.deal_one())

#print(len(new_deck.all_cards))

class Player:
    def __init__(self,name):
        self.name = name
        self.player_cards = []

    def remove_cards(self):
        if self.player_cards != []:
            return self.player_cards.pop()
    
    def add_cards(self,new_cards):
        # for multiple cards to be added, after the war
        if type(new_cards) == type([]):
            return self.player_cards.extend(new_cards)
        # for only 1 card
        else:
            return self.player_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.player_cards)} cards'
    

#new_player = Player("Jose")
#print(new_player)
#new_player.add_cards("mycard")
#print(new_player)
#new_player.remove_cards()
#print(new_player)
#new_player.remove_cards()



'''=========================================================================================================='''

# LOGIC OF THE WAR GAME:
# Create 2 instances for Player 1 and Player 2
p1_name = input("Player 1 enter your name: ")
Player_1 = Player(p1_name)
p2_name = input("Player 2 enter your name: ")
Player_2 = Player(p2_name)
# create a deck instance
new_deck = Deck()
# Shuffle the deck
new_deck.shuffle()

# Deal cards:

# FIRST DEALING WAY
#first_half = new_deck.all_cards[0:26]
#Player_1.add_cards(first_half)
#second_half = new_deck.all_cards[26:]
#Player_2.add_cards(second_half)

# SECOND DEALING WAY
for x in range(0,26):
    Player_1.add_cards(new_deck.deal_one())
    Player_2.add_cards(new_deck.deal_one())
game_on = True
round_num = 0
# get them in a loop to confirm if there are cards in their hands
while game_on:
    round_num += 1
    print(f'Round {round_num}')

    if len(Player_1.player_cards) == 0:
        print(f"{p1_name} is out of cards, {p2_name} wins")
        game_on = False
        break
    elif len(Player_2.player_cards) == 0:
        print(f"{p2_name} is out of cards, {p1_name} wins")
        game_on = False
        break
    
    #Starting the round
    # then get then to grab 1 card each and compare the value
    P1_cards_table = []
    P1_cards_table.append(Player_1.remove_cards())
    P2_cards_table = []
    P2_cards_table.append(Player_2.remove_cards())

    # anothe while loop if in war - in case there are multiple war's at the same time
    at_war = True
    while at_war:
        
        # if there is a winner, both cards are added to the winner's hand
        if P1_cards_table[-1].value > P2_cards_table[-1].value:

            Player_1.add_cards(P1_cards_table)
            Player_1.add_cards(P2_cards_table)

            at_war=False

        elif P1_cards_table[-1].value < P2_cards_table[-1].value:

            Player_2.add_cards(P1_cards_table)
            Player_2.add_cards(P2_cards_table)

            at_war=False


        # if there is a tie, we go to war: each player remove 5 cards and grab another card and compares them to see who wins - add all cards to their hands
        else:
            print("WAR")
            if len(Player_1.player_cards) < 5:
                print("Player 1 out of cards. Player 2 wins")
                game_on = False
                break
            elif len(Player_2.player_cards) < 5:
                print("Player 2 out of cards. Player 1 wins")
                game_on = False
                break
            else:
                for num in range(5):
                    P1_cards_table.append(Player_1.remove_cards())
                    P2_cards_table.append(Player_2.remove_cards())

        # confirm if they still have cards to keep playing

            
    
    
    
    
    
    
    
    
    '''# then get then to grab 1 card each and compare the value
    if  Player_1.player_cards[-1].value == Player_2.player_cards[-1].value:
        print(Player_1.player_cards[-1])
        print(Player_2.player_cards[-1])
        print("Same value")
        War = True
    elif Player_1.player_cards[-1].value > Player_2.player_cards[-1].value:
        print(Player_1.player_cards[-1])
        print(Player_2.player_cards[-1])
        P2_card_comp = Player_2.remove_cards()
        print(P2_card_comp)
        Player_1.add_cards(P2_card_comp)
        print(len(Player_1.player_cards))
        print(len(Player_2.player_cards))
        print(f'{Player_1.player_cards[-1]} Player 1 win')
    elif Player_1.player_cards[-1].value < Player_2.player_cards[-1].value:
        print(Player_1.player_cards[-1])
        print(Player_2.player_cards[-1])
        P1_card_comp = Player_1.remove_cards()
        print(P1_card_comp)
        Player_2.add_cards(P1_card_comp)
        print(len(Player_1.player_cards))
        print(len(Player_2.player_cards))
        print(f'{Player_2.player_cards[-1]} Player 2 win')
    # anothe while loop if in war - in case there are multiple war's at the same time
    # if there is a winne, both cards are added to the winner's hand
    # if there is a tie, we go to war: remove 3 cards for each hand and grab another card (total of 5 cards in play per each player - total 10), and see who wins and add all cards to their hands
    # confirm if they still have cards to keep playing'''




