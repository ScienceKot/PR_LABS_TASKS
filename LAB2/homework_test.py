import unittest
from player import Player
from factory import PlayerFactory

class TestToProtobuf(unittest.TestCase):
    def test_to_protobuf_single_player(self):
        player = Player("Alpha", "alpha@gmail.com", "2000-04-04", 345, "Berserk")
        factory = PlayerFactory()

        result = b'\n)\n\x05Alpha\x12\x0falpha@gmail.com\x1a\n2000-04-04 \xd9\x02(\x00'

        res = factory.to_protobuf([player])

        self.assertEqual(res, result, "To Protobuf: The test for a single player failed")

    def test_to_protobuf_multiple_players(self):
        players = [
            Player("Alpha", "alpha@gmail.com", "2000-04-04", 345, "Berserk"),
            Player("Beta", "beta@gmail.com", "2001-06-10", 657, "Tank")
        ]
        factory = PlayerFactory()

        result = b"\n)\n\x05Alpha\x12\x0falpha@gmail.com\x1a\n2000-04-04 \xd9\x02(\x00\n'\n\x04Beta\x12\x0ebeta@gmail.com\x1a\n2001-06-10 \x91\x05(\x01"

        res = factory.to_protobuf(players)

        self.assertEqual(res, result, "To Protobuf: The test for multiple plauers failed")

class TestFromProtobuf(unittest.TestCase):
    def test_from_protobuf_single_player(self):
        player = [Player("Alpha", "alpha@gmail.com", "2000-04-04", 345, "Berserk")]
        factory = PlayerFactory()

        result = b'\n)\n\x05Alpha\x12\x0falpha@gmail.com\x1a\n2000-04-04 \xd9\x02(\x00'

        gen_players = factory.from_protobuf(result)

        for i in range(len(gen_players)):
            self.assertEqual(gen_players[i].nickname, player[i].nickname, "From multiple XML: Nicknames are different")
            self.assertEqual(gen_players[i].email, player[i].email, "From multiple XML: Emails are different")
            self.assertEqual(gen_players[i].date_of_birth, player[i].date_of_birth,
                             "From multiple XML: Dates of birth are different")
            self.assertEqual(gen_players[i].xp, player[i].xp, "From multiple XML: XP are different")
            self.assertEqual(gen_players[i].cls, player[i].cls, "From multiple XML: Classes are different")

    def test_from_protobuf_multiple_player(self):
        players = [
            Player("Alpha", "alpha@gmail.com", "2000-04-04", 345, "Berserk"),
            Player("Beta", "beta@gmail.com", "2001-06-10", 657, "Tank")
        ]
        factory = PlayerFactory()

        result = b"\n)\n\x05Alpha\x12\x0falpha@gmail.com\x1a\n2000-04-04 \xd9\x02(\x00\n'\n\x04Beta\x12\x0ebeta@gmail.com\x1a\n2001-06-10 \x91\x05(\x01"

        gen_players = factory.from_protobuf(result)

        for i in range(len(gen_players)):
            self.assertEqual(gen_players[i].nickname, players[i].nickname, "From multiple XML: Nicknames are different")
            self.assertEqual(gen_players[i].email, players[i].email, "From multiple XML: Emails are different")
            self.assertEqual(gen_players[i].date_of_birth, players[i].date_of_birth,
                             "From multiple XML: Dates of birth are different")
            self.assertEqual(gen_players[i].xp, players[i].xp, "From multiple XML: XP are different")
            self.assertEqual(gen_players[i].cls, players[i].cls, "From multiple XML: Classes are different")


if __name__ == "__main__":
    unittest.main()