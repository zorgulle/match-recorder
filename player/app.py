from flask.ext.api import status
from player import app
from player.dao.BasicDAO import BasicDAO

@app.route('/delete', methods=['DELETE'])
def delete():
    dao = BasicDAO()

    player = {'last_name': 'Gratata', 'first_name': 'Pull up'}

    if dao.delete_player(player):
        return index()
    else:
        return {'msg': 'Error during player creation'}, status.HTTP_500_INTERNAL_SERVER_ERROR

@app.route(rule='/create', methods=['PUT'])
def create():
    """
    Create a player
    :return:
    """

    player_dao = BasicDAO()

    player = {'last_name': 'Gratata', 'first_name': 'Pull up'}

    if player_dao.add_player(player):
        return index()
    else:
        return {'msg': 'Error during player creation'}, status.HTTP_500_INTERNAL_SERVER_ERROR


@app.route(rule='/', methods=['GET'])
def index():
    """
    List of players
    :return:
    """
    dao = BasicDAO()
    try:
        players = dao.get_all_players()
        return {"players": players}, status.HTTP_200_OK
    except Exception:
        return {'msg': 'Error during players listing'}, status.HTTP_500_INTERNAL_SERVER_ERROR

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)