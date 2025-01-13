class Game:
    def __init__(self, title):
        self.title = title
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, new_title):
        if not isinstance(new_title, str):
            # raise ValueError('title must be a string')
            print('title must be a string')
        elif not len(new_title) > 0:
            # raise ValueError('title must be > 0 chars')
            print('title must be > 0 chars')
        elif hasattr(self, '_title'):
            # raise ValueError('title is constant')
            print('title is constant')
        else:
            self._title = new_title

    def results(self):
        pass

    def players(self):
        pass

    def average_score(self, player):
        pass

    def __repr__(self):
        return f'<Game {self.title}>'

class Player:
    def __init__(self, username):
        self.username = username

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, new_username):
        if not isinstance(new_username, str):
            print('username must be a string')
        elif not 2 <= len(new_username) <= 16:
            print('username must be between 2 and 16 chars')
        else:
            self._username = new_username

    def results(self):
        pass

    def games_played(self):
        pass

    def played_game(self, game):
        pass

    def num_times_played(self, game):
        pass

    def __repr__(self):
        return f'<Player {self.username}>'

class Result:  # middle class
    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        # append the Result object to Result.all
        Result.all.append(self)

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, new_score):
        if not isinstance(new_score, int):
            print('score must be an int')
        elif not 1 <= new_score <= 5000:
            print('score must be between 1 and 5000')
        elif hasattr(self, '_score'):
            print('score is a constant')
        else:
            self._score = new_score
    
    @property
    def player(self):
        return self._player
    
    @player.setter
    def player(self, new_player):
        if not isinstance(new_player, Player):
            print('player must be a Player object')
        else:
            self._player = new_player

    @property
    def game(self):
        return self._game
    
    @game.setter
    def game(self, new_game):
        if not isinstance(new_game, Game):
            print('game must be a Game object')
        else:
            self._game = new_game

    def __repr__(self):
        return f'<Result {self.player}, {self.game}, {self.score}>'


g1 = Game(title='pacman')
g2 = Game(title='mario')

p1 = Player(username='bob123')
p2 = Player(username='alicerules!')

r1 = Result(player=p1, game=g1, score=1000)
r2 = Result(player=p1, game=g1, score=500)
r3 = Result(player=p2, game=g1, score=4444)
r4 = Result(player=p2, game=g2, score=690)
r5 = Result(player=p1, game=g2, score=888)