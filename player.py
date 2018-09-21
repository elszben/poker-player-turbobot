
class Player:
    VERSION = "TurboBot 1"

    def betRequest(self, game_state):
        print "Game state:", game_state
        current_buy_in = game_state["current_buy_in"]
        players = game_state["players"]
        own_id = game_state["in_action"]
        for player in players:
            if player["id"] == own_id:
                call_value = current_buy_in - player["bet"]
                return call_value
        return 0

    def showdown(self, game_state):
        pass

