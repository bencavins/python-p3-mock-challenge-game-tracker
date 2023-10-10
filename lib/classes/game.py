class Game:
    def __init__(self, title):
        self.title = title
        self.results = []
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, new_title):
        if len(new_title) <= 0:
            raise ValueError(f"Title cannot have 0 chars")
        else:
            self._title = new_title
    
    def get_players(self):
        players = []
        for result in self.results:
            players.append(result.player)
        return players
    
    # def average_score(self):
    #     total = 0
    #     for result in self.results:
    #         total += result.score
    #     return total / len(self.results)

    def average_score(self, player):
        total = 0
        count = 0
        for result in self.results:
            if result.player == player:
                total += result.score
                count += 1
        return total / count


    def __repr__(self) -> str:
        return f"<Game {self.title}>"