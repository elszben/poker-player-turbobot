
class Player:
    VERSION = "TurboBot 1"

    def betRequest(self, game_state):
        print "Game state:", game_state
        current_buy_in = game_state["current_buy_in"]
        players = game_state["players"]
        print current_buy_in, players
        return 0

    def showdown(self, game_state):
        pass

