import urllib2
import json

class Player:
    VERSION = "TurboBot 4"

    def get_ranking(own_cards, community_cards):
        all_cards = own_cards + community_cards
        try:
            data = "cards=%s" % json.dumps(all_cards)
            #print "data:", data
            contents = urllib2.urlopen("http://rainman.leanpoker.org/rank", "%s" % data).read()
            #print "Ranking result", contents
            response = json.loads(contents)
            best_hand = response["cards_used"]
            return best_hand
        except Exception as e:
            print "jaj", e
            return None

    def betRequest(self, game_state):
        print "Game state:", game_state
        current_buy_in = game_state["current_buy_in"]
        players = game_state["players"]
        own_id = game_state["in_action"]
        own_cards = []
        community_cards = []
        for player in players:
            if player["id"] == own_id:
                result = current_buy_in - player["bet"]
                own_cards = player["hole_cards"]
        community_cards = game_state["community_cards"]
        best_hand = get_ranking(own_cards, community_cards)
        if best_hand:
            print "best_hand", best_hand
        return result

    def showdown(self, game_state):
        pass

