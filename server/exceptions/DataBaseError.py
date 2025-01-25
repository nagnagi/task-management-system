from exceptions.SystemError import SystemError

class DataBaseError(SystemError):
    def __init__(self, msg: str | None = None):
        if msg is None:
            super().__init__('DataBase error')
        else:
            super().__init__(msg)
