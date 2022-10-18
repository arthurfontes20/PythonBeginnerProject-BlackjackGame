import random
from replit import clear
from art import logo

user_hand = []
computer_hand = []
is_game_over = False

def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards:
        if sum(cards) > 21:
            cards.remove(11)
            cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw!"
    elif computer_score == 0:
        return "Lose, opponent has blackjack!"
    elif user_score == 0:
        return "Win with a blackjack!"
    elif user_score > 21:
        return "You went over. You win!"
    elif computer_score > 21:
        return "Opponent went over. You win!"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose!"

def play_game():
  print(logo)


for _ in range(2):
    user_hand.append(deal_card())
    computer_hand.append(deal_card())

while is_game_over == False:

    user_score = calculate_score(user_hand)
    computer_score = calculate_score(computer_hand)
    print(f"Your cards: {user_hand}, current score: {user_score}")
    print(f"Computer first card: {computer_hand[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True
        print("The game is over!")
    else:
        user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
        if user_should_deal == "y":
            user_hand.append(deal_card())
        else:
            is_game_over = True

while computer_score != 0 and computer_score < 17:
    computer_hand.append(deal_card())
    computer_score = calculate_score(computer_hand)
print(f"   Your final hand: {user_hand}, final score: {user_score}")
print(f"   Computer's final hand: {computer_hand}, final score: {computer_score}")
print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play_game()
