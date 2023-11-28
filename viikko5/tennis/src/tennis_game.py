class TennisGame:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == self.player1:
            self.player1_score = self.player1_score + 1
        else:
            self.player2_score = self.player2_score + 1

    def get_equal_score(self):
        if self.player1_score == 0:
            return "Love-All"
        elif self.player1_score == 1:
            return "Fifteen-All"
        elif self.player1_score == 2:
            return "Thirty-All"
        elif self.player1_score == 3:
            return "Forty-All"
        else:
            return "Deuce"

    def get_advantage_score(self):
        minus_result = self.player1_score - self. player2_score

        if minus_result == 1:
            return f"Advantage {self.player1}"
        elif minus_result == -1:
            return f"Advantage {self.player2}"
        elif minus_result >= 2:
            return f"Win for {self.player1}"
        else:
            return f"Win for {self.player2}"

    def get_temp_score(self, temp_score, score):
        if temp_score == 0:
            return score + "Love"
        elif temp_score == 1:
            return score + "Fifteen"
        elif temp_score == 2:
            return score + "Thirty"
        elif temp_score == 3:
            return score + "Forty"

    def get_score(self):
        score = ""
        temp_score = 0

        if self.player1_score == self.player2_score:
            score=self.get_equal_score()
        elif self.player1_score >= 4 or self.player2_score >= 4:
            score=self.get_advantage_score()
        else:
            for i in range(1, 3):
                if i == 1:
                    temp_score = self.player1_score
                else:
                    score = score + "-"
                    temp_score = self.player2_score

                score=self.get_temp_score(temp_score, score)


        return score
