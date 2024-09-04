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
        result_objs = []
        for r in Result.all:
            if r.game is self:
                result_objs.append(r)
        return result_objs
        # [(thing to append) (for loop def) (conditional statement)]
        # return [r for r in Result.all if r.game is self]

    def players(self):
        players_set = set()
        for r in self.results():
            players_set.add(r.player)
        return players_set
        # return set([r.player for r in self.results()])

    def average_score(self, player):
        total = 0
        count = 0
        for r in self.results():
            if r.player is player:
                total += r.score
                count += 1

        if count == 0:
            return None
        
        return total / count

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
        result_objs = []
        for r in Result.all:
            if r.player is self:
                result_objs.append(r)
        return result_objs
        # return [r for r in Result.all if r.player is self]

    def games_played(self):
        games = set()
        for r in self.results():
            games.add(r.game)
        return games
        # return set([r.game for r in self.results()])

    def played_game(self, game):
        return game in self.games_played()

    def num_times_played(self, game):
        count = 0
        for r in self.results():
            if r.game is game:
                count += 1
        return count
        # return [r.game for r in self.results()].count(game)

    @classmethod
    def highest_scored(cls, game):
        players = list(game.players())

        # all the players who played this game
        max_player = players[0]
        max_player_avg = game.average_score(players[0])

        for player in players:
            # the avg score for the players who played this game
            avg = game.average_score(player)
            if avg > max_player_avg:
                max_player_avg = avg
                max_player = player
        
        return max_player, max_player_avg
        # return max(players, key=lambda player: game.average_score(player))


    def __repr__(self) -> str:
        return f'<Player {self.username}>'

class Result:
    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        Result.all.append(self)
    
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
    g2 = Game('donkey kong')

    p1 = Player('bob123')
    p2 = Player('anon')

    r1 = Result(p1, g1, 5000)
    r1 = Result(p1, g1, 4000)
    r1 = Result(p1, g1, 3000)
    r1 = Result(p1, g2, 123)
    r1 = Result(p2, g1, 999)
    
    print(Player.highest_scored(g1))
