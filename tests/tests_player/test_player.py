from pytest import raises
from src.player.player import Player
from src.player.players import PlayersInMemory
from src.player.players import PlayerExistException


class TestCasePlayers:
    def test_get_players(self):
        players = PlayersInMemory()
        assert players.get_all_players() == []

    def test_add_player(self):
        player = Player(1, "Player")
        players = PlayersInMemory()
        players.add_player(player)
        assert players.get_all_players() == [player]

    def test_add_two_player_with_same_id(self):
        player1 = Player(1, "Player")
        player2 = Player(1, "Player2")
        players = PlayersInMemory()
        players.add_player(player1)

        with raises(PlayerExistException):
            players.add_player(player2)

class TestCasePlayer:
    def test_player_construction(self):
        player_name = "Name"
        player_id = 1
        player = Player(player_id, player_name)
        assert player.get_name() == player_name
        assert player.get_id() == player_id