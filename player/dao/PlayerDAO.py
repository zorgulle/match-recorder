"""
Players DAO
"""

class PlayerDAO:
    def __init__(self):
        host = ''
        port = ''

    def get_connection(self):
        return NotImplementedError

    def close_connection(self):
        return NotImplementedError

    def get_all_players(self):
        raise NotImplementedError

    def add_player(self, player):
        raise NotImplementedError

    def delete_player(self, player):
        raise NotImplementedError