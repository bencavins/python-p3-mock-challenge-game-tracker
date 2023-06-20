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
            raise Exception(f'invalid username: {new_username}')
    
    def games_played(self):
        # answer = []
        # for result in self.results:
        #     answer.append(result.game)
        # return answer
        return [result.game for result in self.results]
    
    def has_played_game(self, game):
        return game in self.games_played()
    
    def num_times_played(self, game):
        # answer = []
        # for result in self.results:
        #     if result.game == game:
        #         answer.append(result)
        # return len(answer)
    
        return len([result for result in self.results if result.game == game])
