import random
suits = ('Hearts', 'Diamondas','Clubs','Spades')
ranks = ("Two",'Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King',"Ace")
value = {"Two":2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10,"Ace":11}

# Class for Cards
class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = value[rank]        

    def __str__(self):
        return f"{self.rank} of {self.suit}"


# Class for Deck the total value is {play
class Deck:
    def __init__(self):
        self.deck_cards = []

    def create_deck(self):
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.deck_cards.append(card)
        return self.deck_cards
    
    def shuffle(self):
        return random.shuffle(self.deck_cards)
    
    def __str__(self):
        deck_comp = ""
        for card in self.deck_cards:
            deck_comp = deck_comp + "\n"+ card.__str__()
        return deck_comp
            

# Class for Players
class Player:
    def __init__(self,name,bankroll):
        self.name = name
        self.bankroll = bankroll
        self.player_hand = []
        self.player_hand_value = 0
        

    def total_value(self):
        self.player_hand_value = 0
        for x in range(len(self.player_hand)):
            self.player_hand_value = self.player_hand_value + self.player_hand[x].value
                       
    
    def place_bet(self,bet):
        #while True:
            #bet = input("How much do you want to bet? ")
            #try:
                #int(bet)
                #break
            #except:
                #print("Please input a number value.")
        self.bankroll = self.bankroll - bet
        return self.bankroll
    
    def bet_won(self,bet):
        self.bankroll = self.bankroll + (2*bet)
        return self.bankroll
    
    def bet_lost(self):
        return self.bankroll

    def __str__(self):
        return f'{self.name} has ${self.bankroll} in his account.\nHis hand is {self.player_hand} and the total value is {self.player_hand_value}'

    
# Class for Dealer
class Dealer:
    def __init__(self,deck_cards):
        self.deck_cards = deck_cards
        self.dealer_hand = []
        self.dealer_hand_value = 0


    def total_value(self):
        self.dealer_hand_value = 0
        for x in range(len(self.dealer_hand)):
            self.dealer_hand_value = self.dealer_hand_value + self.dealer_hand[x].value
    
    def deal_one(self):
        return self.deck_cards.pop()
    
    def __str__(self):
        return f'Dealer hand is {self.dealer_hand} and the total value is {self.dealer_hand_value}'
        







# Function to start game
def game_on():
    game_on = True
    while game_on:
        start_game = input("Hi, are you ready to start to play? Y/N: ")
        if start_game.capitalize() == 'Y':
            game_on = True
            return game_on
        elif start_game.capitalize() == 'N':
            game_on = False
            break
        else:
            print("Please, introduce a correct value.")


# Function Hit/Stay
def hit_player():
    hit = True
    while hit:
        keep_hitting = input("Do you want to hit or stay? H/S ")
        if keep_hitting.lower() == "h":
            return True
        elif keep_hitting.lower() == "s":
            return False
        else:
            print("Please, enter the correct value.")


# Function to modify Ace value
def find_ace(player_hand):
    for cp in range(len(player_hand)):
        print(f'{player_hand[cp].rank} of {player_hand[cp].suit} with value {player_hand[cp].value} ')
        if player_hand[cp].rank == "Ace" and player_hand[cp].value == 11:
            return True

def change_ace(player_hand):
    for cp in range(len(player_hand)):
        if player_hand[cp].rank == "Ace" and player_hand[cp].value == 11:
            player_hand[cp].value = 1
            break



'''test_card1 = Card("Spades","Ace")
test_card2 = Card("Clubs","Ace")

player_test = Player("Emilio",200)
player_test.player_hand.append(test_card1)
player_test.player_hand.append(test_card2)
print(player_test.player_hand[0],player_test.player_hand[1])
if find_ace(player_test.player_hand):
    print(0)
change_ace(player_test.player_hand)
print(player_test.player_hand[0],player_test.player_hand[1])
print(player_test.player_hand[0].value,player_test.player_hand[1].value)
print("==================================================\n==================================================")
if find_ace(player_test.player_hand):
    print(1)
change_ace(player_test.player_hand)
print(player_test.player_hand[0],player_test.player_hand[1])
print(player_test.player_hand[0].value,player_test.player_hand[1].value)
print("==================================================\n==================================================")
if find_ace(player_test.player_hand):
    print(2)'''



# STAR GAME + PLAYER INFORMATION INPUT
play_again = True
player_name = input("Please, introduce your name: ")
while True:
    funds = input("How much do you wish to add to your backroll: ")
    try:
        funds_int = int(funds)
        break
    except:
        print("Please enter the proper value") 


# CREATE DECK OF CARDS + SUFFLE

# Loop to make sure the player wants to start the game or keep playing when relooping
while play_again and game_on():
    new_deck = Deck()
    new_deck.create_deck()
    new_deck.shuffle()


    # Create Dealer and Player instances
    dealer = Dealer(new_deck.deck_cards)
    player1 = Player(player_name,funds_int)
    
    #Resetting the Aces values:    
    
    # Resetting hands
    player1.player_hand = []
    dealer.dealer_hand = []      

    #Placing bet      
    while True:
        bet = input("How much do you wish to bet: ")
        try:
            bet_int = int(bet)
            if bet_int > player1.bankroll:
                print("Not enough money on the bankroll. Please enter a correct amount.")
            else:
                break
        except:
            print("Please enter the proper value")


    # Dealing cards
    for x in range(2):
        player1.player_hand.append(dealer.deal_one())
        dealer.dealer_hand.append(dealer.deal_one())

    
    # Calculating hands Value
    player1.total_value()
    dealer.total_value()

    #Checking both hands
    print(f'{player1.name} has {player1.player_hand[0]} and {player1.player_hand[1]} and the total value is {player1.player_hand_value}')
    print(f'Dealer has {dealer.dealer_hand[0]} and on hidden card')

    # Confirming bet was placed
    player_bet = player1.place_bet(bet_int)
    print(f'{player1.name} has {player1.player_hand[0]} and {player1.player_hand[1]} and the total value is {player1.player_hand_value}.\nThe bet is {bet_int} and the account money remaining is {player1.bankroll}')
    
    # Loop if Player wants to Hit or Stay
    while hit_player():
        player1.player_hand.append(dealer.deal_one())
        player1.total_value()
        print(f'New card for player 1 : {player1.player_hand[-1]}.\nNew hand value is: {player1.player_hand_value}')
        
        
        # Player 1 Bust
        if player1.player_hand_value > 21:
            # if there is an Ace when you pass 21, replace the value from 10 to 1
            if find_ace(player1.player_hand):
                print(f"Old player hand value is {player1.player_hand_value}")
                for cp in range(len(player1.player_hand)):
                    print(f"{player1.player_hand[cp].rank} of {player1.player_hand[cp].suit}, value {player1.player_hand[cp].value}")
                change_ace(player1.player_hand)
                player1.total_value()
                for cp in range(len(player1.player_hand)):
                    print(f"{player1.player_hand[cp].rank} of {player1.player_hand[cp].suit}, value {player1.player_hand[cp].value}")
                print(f"New player hand value is {player1.player_hand_value}")
            
            # if there is no Ace , close the turn with Dealer winning
            else:            
                print(f"{player_name} hand value is over 21. Dealer won")
                player1.bet_lost()
                print(f'Player 1 new balance is {player1.bankroll}')
                break
        
        # Player 1 WON Blackjack
        if player1.player_hand_value == 21:
            print(f"BLACKJACK!!! {player_name} hand value is 21, you won!!!")
            player1.bet_won(bet_int)
            print(f'Player 1 new balance is {player1.bankroll}')
            break

    
    # Delar hit until it passes the player or bust
    while player1.player_hand_value<21 and dealer.dealer_hand_value <=21:
        dealer.dealer_hand.append(dealer.deal_one())
        dealer.total_value()
        print(f'New card for Dealer : {dealer.dealer_hand[-1].rank} of {dealer.dealer_hand[-1].suit}.\nNew hand value is: {dealer.dealer_hand_value}')
        
        # Dealer bets player 1 hand and stays under 21
        if dealer.dealer_hand_value > player1.player_hand_value and dealer.dealer_hand_value <= 21:
            print(f"Dealer has a hand value of {dealer.dealer_hand_value}, mayor than the player {player1.name}who's hand is worth {player1.player_hand_value}. Dealer won")
            player1.bet_lost()
            print(f'Player 1 new balance is {player1.bankroll}')
            break
        
        # If Delaer bust
        elif dealer.dealer_hand_value > 21:
            print(f'Dealer hand value is {dealer.dealer_hand_value}, which is over 21.\nPlayer 1 won.')
            player1.bet_won(bet_int)
            print(f'Player 1 new balance is {player1.bankroll}')
            break
        else:
            pass
    

    # Confirm if player has money to keep playing
    if player1.bankroll <= 0:
        print("You have no more cash, you can not play anymore.")
        break
    else:
        pass

    # Confirm if player wants to play again
    while play_again:
        play_again = input("Do you want to keep playing? Y/N ")
        if play_again.lower() == "y":
            play_again = True
            break
        elif play_again.lower() == "n":
            play_again = False
        else:
            print("Please, provide a correct imput")




# Computer dealer
# Human player
# Has a bankroll
# Will place a bet and indicate if he will win or not that hand
# THe player starts with 2 cards face up
# The dealer starts with 1 card face up and 1 face down
# The human goes first and the goal is to get closer to 21 than the dealer
# Total value of the sum is the sum of the current cards
# You can hit (get one more card) or stay (stop receiving cards)
# If the player card value <21; dealer hits until he will to the player or bust (sum >21)
# Ways for the game to end:
# The player bust before the dealer's turn , the dealer colects the money
# The computer beats the human - the computer either gets a sum higher than the player or hits until it get a higher value + under 21
# The computer hits until he bust, going over 21
# Special rules: Face cards (Jack, Queen, King) count as a value of 10
# Aces can count as either 1 or 11 (whatever value is preferable to the player)