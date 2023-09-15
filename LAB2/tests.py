import unittest
from player import Player
from factory import PlayerFactory
import xml.etree.ElementTree as ET

class TestToJSON(unittest.TestCase):

    def test_to_json_single_player(self):
        player = Player("Alpha", "alpha@gmail.com", "2000-04-04", 455, "Berserk")
        factory = PlayerFactory()

        result = [
            {
                "nickname" : "Alpha",
                "email" : "alpha@gmail.com",
                "date_of_birth" : "2000-04-04",
                "xp" : 455,
                "class" : "Berserk"
            }
        ]

        res = factory.to_json([player])
        self.assertEqual(res, result, "To JSON: The test for a single player failed")

    def test_to_json_multiple_players(self):
        players = [
            Player("Alpha", "alpha@gmail.com", "2000-04-04", 455, "Berserk"),
            Player("Beta", "beta@gmail.com", "2001-06-10", 657, "Tank")
        ]
        factory = PlayerFactory()

        results = [
            {
                "nickname": "Alpha",
                "email": "alpha@gmail.com",
                "date_of_birth": "2000-04-04",
                "xp": 455,
                "class": "Berserk"
            },
            {
                "nickname" : "Beta",
                "email" : "beta@gmail.com",
                "date_of_birth" : "2001-06-10",
                "xp" : 657,
                "class" : "Tank"
            }
        ]

        res = factory.to_json(players)
        self.assertEqual(res, results, "From JSON: The test for a multiple players failed")


class TestFromJSON(unittest.TestCase):
    def test_from_json_single_player(self):
        player = [Player("Alpha", "alpha@gmail.com", "2000-04-04", 455, "Berserk")]
        factory = PlayerFactory()

        result = [
            {
                "nickname" : "Alpha",
                "email" : "alpha@gmail.com",
                "date_of_birth" : "2000-04-04",
                "xp" : 455,
                "class" : "Berserk"
            }
        ]

        res = factory.from_json(result)
        for i in range(len(res)):
            self.assertEqual(res[i].nickname, player[i].nickname, "From single JSON: Nicknames are different")
            self.assertEqual(res[i].email, player[i].email, "From single JSON: Emails are different")
            self.assertEqual(res[i].date_of_birth, player[i].date_of_birth, "From single JSON: Dates of birth are different")
            self.assertEqual(res[i].xp, player[i].xp, "From single JSON: XP are different")
            self.assertEqual(res[i].cls, player[i].cls, "From single JSON: Classes are different")

    def test_from_json_multiple_player(self):
        players = [
            Player("Alpha", "alpha@gmail.com", "2000-04-04", 455, "Berserk"),
            Player("Beta", "beta@gmail.com", "2001-06-10", 657, "Tank")
        ]
        factory = PlayerFactory()

        results = [
            {
                "nickname": "Alpha",
                "email": "alpha@gmail.com",
                "date_of_birth": "2000-04-04",
                "xp": 455,
                "class": "Berserk"
            },
            {
                "nickname": "Beta",
                "email": "beta@gmail.com",
                "date_of_birth": "2001-06-10",
                "xp": 657,
                "class": "Tank"
            }
        ]

        res = factory.from_json(results)
        for i in range(len(res)):
            self.assertEqual(res[i].nickname, players[i].nickname, "From multiple JSON: Nicknames are different")
            self.assertEqual(res[i].email, players[i].email, "From multiple JSON: Emails are different")
            self.assertEqual(res[i].date_of_birth, players[i].date_of_birth, "From multiple JSON: Dates of birth are different")
            self.assertEqual(res[i].xp, players[i].xp, "From multiple JSON: XP are different")
            self.assertEqual(res[i].cls, players[i].cls, "From multiple JSON: Classes are different")

class TestToXML(unittest.TestCase):
    def test_to_xml_single_player(self):
        string = '''<?xml version="1.0"?>
            <data>
                <player>
                    <nickname>Alpha</nickname>
                    <email>alpha@gmail.com</email>
                    <date_of_birth>2000-04-04</date_of_birth>
                    <xp>455</xp>
                    <class>Berserk</class>
                </player>
            </data>
        '''
        players = [Player(nickname="Alpha", email="alpha@gmail.com", date_of_birth="2000-04-04", xp=455, cls="Berserk")]
        factory = PlayerFactory()

        gen_players_xml = factory.to_xml(players)

        self.assertEqual(ET.canonicalize(string, strip_text=True),
                         ET.canonicalize(gen_players_xml, strip_text=True), "To single XML: The test for a single player has failed")

    def test_to_xml_multople_player(self):
        string = '''<?xml version="1.0"?>
            <data>
                <player>
                    <nickname>Alpha</nickname>
                    <email>alpha@gmail.com</email>
                    <date_of_birth>2000-04-04</date_of_birth>
                    <xp>455</xp>
                    <class>Berserk</class>
                </player>
                <player>
                    <nickname>Beta</nickname>
                    <email>beta@gmail.com</email>
                    <date_of_birth>2001-06-10</date_of_birth>
                    <xp>657</xp>
                    <class>Tank</class>
                </player>
            </data>
        '''


        players = [
            Player("Alpha", "alpha@gmail.com", "2000-04-04", 455, "Berserk"),
            Player("Beta", "beta@gmail.com", "2001-06-10", 657, "Tank")
        ]
        factory = PlayerFactory()

        gen_players_xml = factory.to_xml(players)

        self.assertEqual(ET.canonicalize(string, strip_text=True),
                         ET.canonicalize(gen_players_xml, strip_text=True),
                         "To multiple XML: The test for multiple players has failed")

class TestFromXML(unittest.TestCase):
    def test_from_xml_single_player(self):
        string = '''<?xml version="1.0"?>
                    <data>
                        <player>
                            <nickname>Alpha</nickname>
                            <email>alpha@gmail.com</email>
                            <date_of_birth>2000-04-04</date_of_birth>
                            <xp>455</xp>
                            <class>Berserk</class>
                        </player>
                    </data>
                '''
        players = [Player(nickname="Alpha", email="alpha@gmail.com", date_of_birth="2000-04-04", xp=455, cls="Berserk")]
        factory = PlayerFactory()

        gen_players = factory.from_xml(string)

        for i in range(len(gen_players)):
            self.assertEqual(gen_players[i].nickname, players[i].nickname, "From single XML: Nicknames are different")
            self.assertEqual(gen_players[i].email, players[i].email, "From single XML: Emails are different")
            self.assertEqual(gen_players[i].date_of_birth, players[i].date_of_birth, "From single XML: Dates of birth are different")
            self.assertEqual(gen_players[i].xp, players[i].xp, "From single XML: XP are different")
            self.assertEqual(gen_players[i].cls, players[i].cls, "From single XML: Classes are different")

    def test_from_xml_multiple_plauers(self):
        string = '''<?xml version="1.0"?>
                    <data>
                        <player>
                            <nickname>Alpha</nickname>
                            <email>alpha@gmail.com</email>
                            <date_of_birth>2000-04-04</date_of_birth>
                            <xp>455</xp>
                            <class>Berserk</class>
                        </player>
                        <player>
                            <nickname>Beta</nickname>
                            <email>beta@gmail.com</email>
                            <date_of_birth>2001-06-10</date_of_birth>
                            <xp>657</xp>
                            <class>Tank</class>
                        </player>
                    </data>
                '''

        players = [
            Player("Alpha", "alpha@gmail.com", "2000-04-04", 455, "Berserk"),
            Player("Beta", "beta@gmail.com", "2001-06-10", 657, "Tank")
        ]
        factory = PlayerFactory()

        gen_players = factory.from_xml(string)

        for i in range(len(gen_players)):
            self.assertEqual(gen_players[i].nickname, players[i].nickname, "From multiple XML: Nicknames are different")
            self.assertEqual(gen_players[i].email, players[i].email, "From multiple XML: Emails are different")
            self.assertEqual(gen_players[i].date_of_birth, players[i].date_of_birth, "From multiple XML: Dates of birth are different")
            self.assertEqual(gen_players[i].xp, players[i].xp, "From multiple XML: XP are different")
            self.assertEqual(gen_players[i].cls, players[i].cls, "From multiple XML: Classes are different")

if __name__ == "__main__":
    unittest.main()
