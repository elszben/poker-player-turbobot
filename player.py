import urllib2
import json

class Player:
    VERSION = "TurboBot 3"

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
            data = "cards=%s" % json.dumps(all_cards)
            print "data:", data
            contents = urllib2.urlopen("http://rainman.leanpoker.org/rank", "%s" % data).read()
            print "Ranking result", contents
        except Exception as e:
            print "jaj", e
        return result

    def showdown(self, game_state):
        pass

