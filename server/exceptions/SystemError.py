class SystemError(Exception):
    def __init__(self, msg: str | None = None):
        super().__init__()
        if msg is None:
            self.msg = 'System error'
        else:
            self.msg = msg

    def __str__(self):
        return self.msg
