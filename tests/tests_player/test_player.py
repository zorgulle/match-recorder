from src.player.player import Player
class TestCasePlayer:
    def test_player_construction(self):
        player_name = "Name"
        player_id = 1
        player = Player(player_id, player_name)
        assert player.get_name() == player_name
        assert player.get_id() == player_id