"""Custom exception
"""

class AddPlayerException(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)

class RemovePlayerException(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
