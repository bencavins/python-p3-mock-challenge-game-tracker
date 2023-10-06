class Player:
    def __init__(self, username):
        self.username = username
        self.results = []
    
    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, new_username):
        if len(new_username) >= 2 and len(new_username) <= 16:
            self._username = new_username
        else:
            raise ValueError('username must be between 2 and 16 chars')
    
    def games_played(self):
        # we'll go over this again on Tue
        games = []
        for result in self.results:
            games.append(result.game)
        return games
    
    def has_played_game(self, game):
        # we'll go over this again on Tue
        return game in self.games_played()
    
    def num_times_played(self, game):
        pass

