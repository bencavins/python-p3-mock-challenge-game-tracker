class Game:
    def __init__(self, title):
        self.title = title
        self.results = []
    
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, new_title):
        if isinstance(new_title, str) and len(new_title) > 0:
            self._title = new_title
        else:
            raise Exception(f'invalid title: {new_title}')
    
    def get_players(self):
        return [result.player for result in self.results]
    
    def average_score(self, player):
        # player_results = [result for result in self.results if result.player == player]
        total = 0
        result_count = 0
        for result in self.results:
            if result.player == player:
                total += result.score
                result_count += 1

        return total / result_count