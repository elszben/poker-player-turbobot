import urllib2

class Player:
    VERSION = "TurboBot 2"

    def betRequest(self, game_state):
        print "Game state:", game_state
        current_buy_in = game_state["current_buy_in"]
        players = game_state["players"]
        own_id = game_state["in_action"]
        for player in players:
            if player["id"] == own_id:
                result = current_buy_in - player["bet"]
                own_cards = player["hole_cards"]
        table_cards = game_state["community_cards"]
        all_cards = own_cards + table_cards
        try:
            contents = urllib2.urlopen("http://rainman.leanpoker.org/rank", "cards=%s" % all_cards).read()
            print "Ranking result", contents
        except Exception as e:
            print "jaj", e
        return result

    def showdown(self, game_state):
        pass

