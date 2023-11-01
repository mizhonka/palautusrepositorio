import unittest
from statistics_service import StatisticsService
from player import Player
from sortBy import SortBy

def ComparePlayers(p1, p2):
    if not p1.name==p2.name:
        return False
    if not p1.team==p2.team:
        return False
    if not p1.goals==p2.goals:
        return False
    if not p1.assists==p2.assists:
        return False
    return True


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticService(unittest.TestCase):
    def setUp(self):
        self.stub=PlayerReaderStub()
        self.stats=StatisticsService(self.stub)

    def test_no_player_returns_none(self):
        player=self.stats.search("X")
        self.assertEqual(player, None)

    def test_search_returns_correct_player(self):
        player=self.stub.get_players()[0]
        r=self.stats.search("Semenko")
        self.assertTrue(ComparePlayers(player, r))

    def test_correct_team_players(self):
        players=self.stub.get_players()
        team=[players[0], players[2], players[4]]
        r=self.stats.team("EDM")
        if not len(team)==len(r):
            self.assertTrue(False)
        for i in range(0, 3):
            if not ComparePlayers(team[i], r[i]):
                self.assertTrue(False)
        self.assertTrue(True)

    def sort(self, sortBy, sorted):
        r=self.stats.top(4, sortBy)
        for i in range(0, 5):
            if not ComparePlayers(sorted[i], r[i]):
                self.assertTrue(False)
        self.assertTrue(True)

    def test_sorted_by_points(self):
        players=self.stub.get_players()
        sorted=[players[4], players[1],players[3],players[2],players[0]]
        self.sort(SortBy.POINTS, sorted)

    def test_sorted_by_goals(self):
        players=self.stub.get_players()
        sorted=[players[1], players[3],players[2],players[4],players[0]]
        self.sort(SortBy.GOALS, sorted)

    def test_sorted_by_assists(self):
        players=self.stub.get_players()
        sorted=[players[4], players[3],players[1],players[2],players[0]]
        self.sort(SortBy.ASSISTS, sorted)
