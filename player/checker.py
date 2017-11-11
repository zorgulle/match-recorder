import logging

from player.exception.exception import InvalidFormatException
from player.exception.exception import EmptyDataExcpetion


class Checker:
    def __init__(self):
        self.data_description = {
            "name": {
                "type": "string",
                "max_length": 120,
                "min_length": 4,
                "allow_numbers": False,
                "allow_special_char": False,
                "requiered": True
            },
            "last_name": {
                "type": "string",
                "max_length": 120,
                "min_length": 4,
                "allow_numbers": False,
                "allow_special_char": False,
                "requiered": True
            },

        }

        self.missing_attributes = {}


    def __check_requierements(self, request_data, requiered):
        if requiered:
            return (request_data is not None) and requiered
        else:
            return True

    def check_post_datas(self, datas):
        """
        :param datas:
        :return:
        """
        if not datas:
            raise EmptyDataExcpetion("post data is empty")

        for field_name, description in self.data_description.items():
            if not self.__check_requierements(datas.get(field_name, None), description.get("requiered", False)):
                self.missing_attributes[field_name] = "requiered"



        if self.missing_attributes:
            raise InvalidFormatException("Invalid data format")
