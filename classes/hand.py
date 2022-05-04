from final_black_jack.classes.card import Card


# Hand Class
class Hand:

    # Default constructor for hand class
    def __init__(self):
        self.player_hand_values = []
        self.player_hand = []
        self.dealer_hand_values = []
        self.dealer_hand = []

    # Gets the total value of the player's hand
    def get_player_hand_total(self):
        player_total = 0
        for i in self.player_hand_values:
            player_total += i
        return player_total

    # Gets the total value of the dealer's hand
    def get_dealer_hand_total(self):
        dealer_total = 0
        for i in self.dealer_hand_values:
            dealer_total += i
        return dealer_total

    # Gives the player's hand a new card
    def deal_card_to_player(self):
        card = Card()
        self.player_hand_values.append(card.get_count_value())
        self.player_hand.append(card.get_string_value())

    # Gives the dealer's hand a new card
    def deal_card_to_dealer(self):
        card = Card()
        self.dealer_hand_values.append(card.get_count_value())
        self.dealer_hand.append(card.get_string_value())

    # Puts the player's hand into a more readable string
    def show_player_hand(self):
        player_hand_string = ''
        if len(self.player_hand) > 0:
            for i in self.player_hand:
                player_hand_string += i + " "
        return player_hand_string

    # Puts the dealer's hand into a more readable string
    def show_dealer_hand(self):
        dealer_hand_string = ''
        if len(self.dealer_hand) > 0:
            for i in self.dealer_hand:
                dealer_hand_string += i + " "
        return dealer_hand_string
