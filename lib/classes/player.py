class Player:

    def __init__(self, username):
        self.username = username
        self.results = []

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, new_username):
        if 2 <= len(new_username) <= 16:
            self._username = new_username
        else:
            raise Exception(f'invalid username: {new_username}')
    
    def games_played(self):
        return [r.game for r in self.results]
    
    def has_played_game(self, game):
        return game in self.games_played()
    
    def num_times_played(self, game):
        return self.games_played().count(game)
        
