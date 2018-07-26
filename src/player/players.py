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

    def __player_exist(self, player_to_add):

        player_with_same_id = [player for player in self.get_all_players() if player_to_add == player]

        return bool(player_with_same_id)

class PlayerExistException(Exception):
    pass