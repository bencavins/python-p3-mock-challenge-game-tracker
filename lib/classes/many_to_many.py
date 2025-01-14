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
        game_results = []
        for result in Result.all:
            if result.game is self:
                game_results.append(result)
        return game_results
        # return [result for result in Result.all if result.game is self]

    def players(self):
        players_list = []
        for result in self.results():
            players_list.append(result.player)
        return list(set(players_list))
        # return list(set([result.player for result in self.results()]))

    def average_score(self, player):
        total = 0
        count = 0
        for result in self.results():
            if result.player is player:
                total += result.score
                count += 1
        return total / count

    def all_player_avgs(self):
        avgs = {}
        for player in self.players():
            avg = self.average_score(player)
            avgs[player] = avg
        return avgs

    def __repr__(self):
        return f'<Game {self.title}>'

class Player:

    @classmethod
    def highest_scored(cls, game):
        avgs = game.all_player_avgs()
        max_player = None
        max_score = -1
        for player in avgs:
            score = avgs[player]
            if score > max_score:
                max_score = score
                max_player = player
        return max_player, max_score
        # return max([(player, score) for player, score in game.all_player_avgs().items()], key=lambda x: x[1])

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
        player_results = []
        for result in Result.all:
            if result.player is self:
                player_results.append(result)
        return player_results
        # [(thing to append) (for loop definition) (optional if condition)]
        # return [result for result in Result.all if result.player is self]

    def games_played(self):
        games = []
        for result in self.results():
            games.append(result.game)
        return list(set(games))
        # return list(set([result.game for result in self.results()]))

    def played_game(self, game):
        return game in self.games_played()

    def num_times_played(self, game):
        count = 0
        for result in self.results():
            if result.game is game:
                count += 1
        return count
        # return sum([1 for result in self.results() if result.game is game])

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