from player import Player
from playing_cards import Deck
import terminal_ui

class Game:
    def __init__(self, player1_name, player2_name):
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)
        self.deck = Deck()

    def deal_cards(self):
        self.deck.shuffle()
        while self.deck.has_cards():
            self.player1.add_card(self.deck.deal_card())
            if self.deck.has_cards():
                self.player2.add_card(self.deck.deal_card())

    def play_round(self):
        print('\033c')
        card1 = self.player1.play_card()
        card2 = self.player2.play_card()

        if card1 is None or card2 is None:
            return None, None, "Game Over"

        try:
            card1.print_card()
        except KeyError:
            print("Card art not found for", card1)
        print(f"{self.player1.name} plays {card1}")

        try:
            card2.print_card()
        except KeyError:
            print("Card art not found for", card2)
        print(f"{self.player2.name} plays {card2}")

        if card1 > card2:
            print(f"{self.player1.name} wins the round")
            self.player1.add_card(card1)
            self.player1.add_card(card2)
            return card1, card2, self.player1.name
        elif card2 > card1:
            print(f"{self.player2.name} wins the round")
            self.player2.add_card(card2)
            self.player2.add_card(card1)
            return card1, card2, self.player2.name
        else:
            print("War!")
            war_cards1 = []
            war_cards2 = []

            for _ in range(3):
                if self.player1.has_cards():
                    card = self.player1.play_card()
                    if card:
                        war_cards1.append(card)
                    else:
                        return None, None, "Game Over"
                else:
                    return None, None, "Game Over"

                if self.player2.has_cards():
                    card = self.player2.play_card()
                    if card:
                        war_cards2.append(card)
                    else:
                        return None, None, "Game Over"
                else:
                    return None, None, "Game Over"

            if not war_cards1 or not war_cards2:
                return None, None, "Game Over"

            card1 = self.player1.play_card()
            card2 = self.player2.play_card()

            if not card1 or not card2:
                return None, None, "Game Over"

            if card1 > card2:
                print(f"{self.player1.name} wins the war")
                self.player1.add_card(card1)
                self.player1.add_card(card2)
                while war_cards1:
                    self.player1.add_card(war_cards1.pop(0))
                while war_cards2:
                    self.player1.add_card(war_cards2.pop(0))
                return card1, card2, self.player1.name
            elif card2 > card1:
                print(f"{self.player2.name} wins the war")
                self.player2.add_card(card2)
                self.player2.add_card(card1)
                while war_cards2:
                    self.player2.add_card(war_cards2.pop(0))
                while war_cards1:
                    self.player2.add_card(war_cards1.pop(0))
                return card1, card2, self.player2.name
            else:
                print("Double War!")
                war_cards1_2 = []
                war_cards2_2 = []

                for _ in range(3):
                    if self.player1.has_cards():
                        card = self.player1.play_card()
                        if card:
                            war_cards1_2.append(card)
                        else:
                            return None, None, "Game Over"
                    else:
                        return None, None, "Game Over"

                    if self.player2.has_cards():
                        card = self.player2.play_card()
                        if card:
                            war_cards2_2.append(card)
                        else:
                            return None, None, "Game Over"
                    else:
                        return None, None, "Game Over"

                if not war_cards1_2 or not war_cards2_2:
                    return None, None, "Game Over"

                card1 = self.player1.play_card()
                card2 = self.player2.play_card()

                if not card1 or not card2:
                    return None, None, "Game Over"

                if card1 > card2:
                    print(f"{self.player1.name} wins the double war")
                    self.player1.add_card(card1)
                    self.player1.add_card(card2)
                    while war_cards1:
                        self.player1.add_card(war_cards1.pop(0))
                    while war_cards2:
                        self.player1.add_card(war_cards2.pop(0))
                    while war_cards1_2:
                        self.player1.add_card(war_cards1_2.pop(0))
                    while war_cards2_2:
                        self.player1.add_card(war_cards2_2.pop(0))
                    return card1, card2, self.player1.name
                elif card2 > card1:
                    print(f"{self.player2.name} wins the double war")
                    self.player2.add_card(card2)
                    self.player2.add_card(card1)
                    while war_cards2:
                        self.player2.add_card(war_cards2.pop(0))
                    while war_cards1:
                        self.player2.add_card(war_cards1.pop(0))
                    while war_cards2_2:
                        self.player2.add_card(war_cards2_2.pop(0))
                    while war_cards1_2:
                        self.player2.add_card(war_cards1_2.pop(0))
                    return card1, card2, self.player2.name
                else:
                    print("Triple War!")
                    war_cards1_3 = []
                    war_cards2_3 = []

                    for _ in range(3):
                        if self.player1.has_cards():
                            card = self.player1.play_card()
                            if card:
                                war_cards1_3.append(card)
                            else:
                                return None, None, "Game Over"
                        else:
                            return None, None, "Game Over"

                        if self.player2.has_cards():
                            card = self.player2.play_card()
                            if card:
                                war_cards2_3.append(card)
                            else:
                                return None, None, "Game Over"
                        else:
                            return None, None, "Game Over"

                    if not war_cards1_3 or not war_cards2_3:
                        return None, None, "Game Over"

                    card1 = self.player1.play_card()
                    card2 = self.player2.play_card()

                    if not card1 or not card2:
                        return None, None, "Game Over"

                    if card1 > card2:
                        print(f"{self.player1.name} wins the triple war")
                        self.player1.add_card(card1)
                        self.player1.add_card(card2)
                        while war_cards1:
                            self.player1.add_card(war_cards1.pop(0))
                        while war_cards2:
                            self.player1.add_card(war_cards2.pop(0))
                        while war_cards1_2:
                            self.player1.add_card(war_cards1_2.pop(0))
                        while war_cards2_2:
                            self.player1.add_card(war_cards2_2.pop(0))
                        while war_cards1_3:
                            self.player1.add_card(war_cards1_3.pop(0))
                        while war_cards2_3:
                            self.player1.add_card(war_cards2_3.pop(0))
                        return card1, card2, self.player1.name
                    elif card2 > card1:
                        print(f"{self.player2.name} wins the triple war")
                        self.player2.add_card(card2)
                        self.player2.add_card(card1)
                        while war_cards2:
                            self.player2.add_card(war_cards2.pop(0))
                        while war_cards1:
                            self.player2.add_card(war_cards1.pop(0))
                        while war_cards2_2:
                            self.player2.add_card(war_cards2_2.pop(0))
                        while war_cards1_2:
                            self.player2.add_card(war_cards1_2.pop(0))
                        while war_cards2_3:
                            self.player2.add_card(war_cards2_3.pop(0))
                        while war_cards1_3:
                            self.player2.add_card(war_cards1_3.pop(0))
                        return card1, card2, self.player2.name
                    else:
                        print("Quadruple War! This is not implemented yet, Player 1 wins")
                        self.player1.add_card(card1)
                        self.player1.add_card(card2)
                        while war_cards1:
                            self.player1.add_card(war_cards1.pop(0))
                        while war_cards2:
                            self.player1.add_card(war_cards2.pop(0))
                        while war_cards1_2:
                            self.player1.add_card(war_cards1_2.pop(0))
                        while war_cards2_2:
                            self.player1.add_card(war_cards2_2.pop(0))
                        while war_cards1_3:
                            self.player1.add_card(war_cards1_3.pop(0))
                        while war_cards2_3:
                            self.player1.add_card(war_cards2_3.pop(0))
                        return card1, card2, self.player1.name

    def play_game(self):
        self.deal_cards()

        while self.player1.has_cards() and self.player2.has_cards():
            input("Press Enter to play the next round...")
            card1, card2, winner = self.play_round()
            if winner == "Game Over":
                break

        if not self.player1.has_cards():
            print(f"{self.player2.name} wins the game!")
        elif not self.player2.has_cards():
            print(f"{self.player1.name} wins the game!")
        else:
            print("Game ended due to a lack of cards to play!")

if __name__ == "__main__":
    player1_name = terminal_ui.run_game()
    if player1_name:
        game = Game(player1_name, "Computer")
        game.play_game()
