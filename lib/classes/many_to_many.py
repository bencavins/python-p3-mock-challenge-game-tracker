class Game:
    def __init__(self, title):
        self.title = title
    
    @property
    def title(self):  # getter for title
        return self._title
    
    @title.setter
    def title(self, new_title):  # setter for title
        if isinstance(new_title, str) \
                and len(new_title) > 0 \
                and not hasattr(self, '_title'):
            self._title = new_title
        # else:
        #     raise ValueError()

    def results(self):
        pass

    def players(self):
        pass

    def average_score(self, player):
        pass

    def __repr__(self) -> str:
        return f'<Game {self.title}>'

class Player:
    def __init__(self, username):
        self.username = username

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, new_username):
        if isinstance(new_username, str) and 2 <= len(new_username) <= 16:
        # if isinstance(new_username, str) and len(new_username) >= 2 and len(new_username) <= 16:
            self._username = new_username

    def results(self):
        pass

    def games_played(self):
        pass

    def played_game(self, game):
        pass

    def num_times_played(self, game):
        pass

    def __repr__(self) -> str:
        return f'<Player {self.username}>'

class Result:
    # all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        # Result.all.append(self)
    
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, new_score):
        if isinstance(new_score, int) \
                and 1 <= new_score <= 5000 \
                and not hasattr(self, '_score'):  # test score hasn't been set
            self._score = new_score
    
    @property
    def player(self):
        return self._player
    
    @player.setter
    def player(self, new_player):
        if isinstance(new_player, Player):
            self._player = new_player

    @property
    def game(self):
        return self._game
    
    @game.setter
    def game(self, new_game):
        if isinstance(new_game, Game):
            self._game = new_game
    
    def __repr__(self) -> str:
        return f'<Result {self.player.username} {self.game.title} {self.score}>'


if __name__ == '__main__':  # only run this code if this file is executed directly
    g1 = Game('pacman')

    p1 = Player('bob123')

    r1 = Result(p1, g1, 5000)
    
    print(g1)
    print(p1)
    print(r1)
