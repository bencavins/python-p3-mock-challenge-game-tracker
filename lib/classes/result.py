class Result:
    def __init__(self, player, game, score):
        self.player = player  # link result.player
        player.results.append(self)  # link player.results
        self.game = game
        game.results.append(self)
        self.score = score
    
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, new_score):
        if new_score >= 1 and new_score <= 5000:
            self._score = new_score
        else:
            raise ValueError('score must be between 1 and 5000')
        
    @property
    def player(self):
        return self._player
    
    @player.setter
    def player(self, new_player):
        from classes.player import Player
        if isinstance(new_player, Player):
            self._player = new_player
        else:
            raise ValueError('player must be of type Player')
    
    def __repr__(self) -> str:
        return f'<Result {self.game} {self.player} {self.score}'
