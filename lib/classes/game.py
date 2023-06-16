class Game:
    def __init__(self, title):
        self.title = title
        self.results = []

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, new_title):
        if len(new_title) > 0:
            self._title = new_title
        else:
            raise Exception(f'invalid title: "{new_title}"')

    def get_players(self):
        return [r.player for r in self.results]
    
    def average_score(self, player):
        return sum([r.score for r in self.results if r.player == player]) / len(self.results)