"""
Basic DAO
"""
from player.utils.decorator import singleton
from player.dao.PlayerDAO import PlayerDAO



@singleton
class BasicDAO(PlayerDAO):
    def __init__(self):
        self.players = [
            {
                'first_name': 'Bernard',
                'last_name': 'Foo'
            },
            {
                'first_name': 'Ga',
                'last_name': 'Bar'
            },
            {
                'first_name': 'Foo',
                'last_name': 'Zoo'
            },
            {
                'first_name': 'Me',
                'last_name': 'Me'
            },
        ]

    def get_all_players(self):
        raise Exception
        return self.players

    def add_player(self, player):
        try:
            self.players.append(player)
            return True
        except Exception:
            if player in self.players:
                return True
            else:
                return False

    def delete_player(self, player):
        self.players.remove(player)
        return True