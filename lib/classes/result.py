from classes.player import Player
from classes.game import Game

class Result:
    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score

        # can also do player.results.append(self)
        self.player.results.append(self)
        self.game.results.append(self)

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, new_score):
        if 1 <= new_score <= 5000:
            self._score = new_score
        else:
            raise Exception(f'invalid score: {new_score}')

    @property
    def player(self):
        return self._player
    
    @player.setter
    def player(self, new_player):
        if isinstance(new_player, Player):
            self._player = new_player
        else:
            raise Exception('invalid player')
    
    @property
    def game(self):
        return self._game
    
    @game.setter
    def game(self, new_game):
        if isinstance(new_game, Game):
            self._game = new_game
        else:
            raise Exception('invalid game')
    
    def __repr__(self) -> str:
        return f'<Result {self.player.username} {self.game.title}>'
