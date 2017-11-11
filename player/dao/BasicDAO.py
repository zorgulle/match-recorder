"""
Basic DAO
"""
import logging

from player.utils.decorator import singleton
from player.dao.PlayerDAO import PlayerDAO

from player.exception.exception import AddPlayerException
from player.exception.exception import RemovePlayerException


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
        players = []
        try:
            players = self.players
        except Exception:
            logging.error(msg="Error while getting players")
            players = []
        finally:
            return players

    def add_player(self, player):
        try:
            self.players.append(player)
        except Exception:
            logging.error(msg="Error during add player")
            raise AddPlayerException()

    def delete_player(self, player):
        try:
            self.players.remove(player)
        except Exception:
            logging.error(msg="Error while deleting player")
            raise RemovePlayerException()
