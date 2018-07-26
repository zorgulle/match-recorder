class Players:

    def add_player(self, player):
        raise NotImplementedError

    def remove_player(self, player):
        raise NotImplementedError

    def modify_player(self, player):
        raise NotImplementedError

    def get_all_players(self, player):
        raise NotImplementedError

class PlayersInMemory(Players):

    def __init__(self):
        self.__players = []

    def get_all_players(self):
        return self.__players

    def add_player(self, player):
        if self.__player_exist(player):
            raise PlayerExistException()
        self.__players.append(player)

    def __player_exist(self, player):
        filter_by_id = lambda x: x.get_id() == player.get_id()
        player_with_same_id = list(filter(filter_by_id, self.get_all_players()))

        if player_with_same_id:
            return True
        return False

class PlayerExistException(Exception):
    pass