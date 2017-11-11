"""
Player controller module
"""

#TODO: Add update method
#TODO: Add comment
#TODO: Unit test
#TODO: Add search feature + Unit test
#TODO: Add filter for removing + Unit test
#TODO: Try locust load testing
#TODO: Add Travis
#TODO: Add Heroku deployment
#TODO: Add real DB DAO (SQL Lite)
#TODO: Add readme

import json

from flask import request
from flask_api import status

from player import app
from player.dao.BasicDAO import BasicDAO
from player.checker import Checker

from player.exception.exception import AddPlayerException
from player.exception.exception import RemovePlayerException
from player.exception.exception import InvalidFormatException, EmptyDataExcpetion


@app.route('/delete', methods=['DELETE'])
def delete():
    dao = BasicDAO()

    player = {'last_name': 'Gratata', 'first_name': 'Pull up'}

    try:
        dao.delete_player(player)
    except RemovePlayerException:
        return {'msg': 'Error during player creation'}, status.HTTP_500_INTERNAL_SERVER_ERROR
    else:
        return index()


@app.route(rule='/player/attributes', methods=['GET'])
def get_attributes():
    checker = Checker()
    return checker.data_description

@app.route(rule='/create', methods=['POST'])
def create():
    #TODO: Use post data to get creation player infos
    """
    Create a player
    :return:
    """

    checker = Checker()
    try:
        checker.check_post_datas(request.json)
    except EmptyDataExcpetion as e:
        return {"msg": "Empty data"}, status.HTTP_204_NO_CONTENT
    except InvalidFormatException as e:
        return checker.missing_attributes, status.HTTP_500_INTERNAL_SERVER_ERROR
    else:
        return {"infos": request.json}


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