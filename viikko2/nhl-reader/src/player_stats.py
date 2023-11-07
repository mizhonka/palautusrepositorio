class PlayerStats:
    def __init__(self, reader):
        self.players=reader.get_players()

    def sort_by_points(self, player):
        return player.points

    def top_scorers_by_nationality(self, nationality):
        scorers=[]
        for p in self.players:
            if p.nationality==nationality:
                scorers.append(p)
        scorers.sort(key=self.sort_by_points, reverse=True)
        return scorers
