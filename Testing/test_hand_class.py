import unittest
from final_black_jack.classes.hand import Hand


class test_hand_class(unittest.TestCase):

    def setUp(self):
        self.hand = Hand()

    def tearDown(self):
        del self.hand

    def test_constructor(self):
        self.assertFalse(self.hand.player_hand)
        self.assertFalse(self.hand.dealer_hand)
        self.assertFalse(self.hand.player_hand_values)
        self.assertFalse(self.hand.dealer_hand_values)

    def test_deal_card_to_player(self):
        self.hand.deal_card_to_player()
        self.assertEqual(len(self.hand.player_hand), 1)
        self.hand.deal_card_to_player()
        self.assertEqual(len(self.hand.player_hand), 2)

    def test_deal_card_to_dealer(self):
        self.hand.deal_card_to_dealer()
        self.assertEqual(len(self.hand.dealer_hand), 1)
        self.hand.deal_card_to_dealer()
        self.assertEqual(len(self.hand.dealer_hand), 2)

    def test_get_player_hand_total(self):
        self.hand = Hand()
        self.assertEqual(self.hand.get_player_hand_total(), 0)
        self.hand.deal_card_to_player()
        self.assertGreater(self.hand.get_player_hand_total(), 0)

    def test_get_dealer_hand_total(self):
        self.hand = Hand()
        self.assertEqual(self.hand.get_dealer_hand_total(), 0)
        self.hand.deal_card_to_dealer()
        self.assertGreater(self.hand.get_dealer_hand_total(), 0)
