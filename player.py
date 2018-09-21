import urllib2
import json
import strategy

class Player:
    VERSION = "TurboBot 5"

    def get_ranking(self, own_cards, community_cards):
        all_cards = own_cards + community_cards
        try:
            data = "cards=%s" % json.dumps(all_cards)
            #print "Ranking request:", data
            contents = urllib2.urlopen("http://rainman.leanpoker.org/rank", "%s" % data).read()
            #print "Ranking result", contents
            response = json.loads(contents)
            best_hand = response["cards_used"]
            rank = response["rank"]
            return (best_hand, rank)
        except Exception as e:
            print "jaj", e
            return (None, 0)

    def get_data(self, game_state):
        print "Game state:", game_state
        current_buy_in = game_state["current_buy_in"]
        players = game_state["players"]
        own_id = game_state["in_action"]
        minimum_raise = game_state["minimum_raise"]
        own_cards = []
        community_cards = []
        current_money = 0
        bet = 0
        for player in players:
            if player["id"] == own_id:
                bet = player["bet"]
                current_money = player["stack"]
                own_cards = player["hole_cards"]
        community_cards = game_state["community_cards"]
        return (current_buy_in, bet, own_cards, community_cards, minimum_raise, current_money)

    def betRequest(self, game_state):
        (current_buy_in, bet, own_cards, community_cards, minimum_raise, current_money) = self.get_data(game_state)
        (best_hand, rank) = self.get_ranking(own_cards, community_cards)
        bet = current_buy_in - bet
        if best_hand:
            bet = strategy.get_bet(current_money, current_buy_in - bet, best_hand, rank, minimum_raise)
        elif bet>50:
            bet = 0
        print "Final bet:", bet
        return bet

    def showdown(self, game_state):
        pass

