import uuid
import datetime


class Chapter:
    def __init__(self, name):
        self.name = name
        self.id = uuid.uuid4()
        self.date = datetime.datetime.now().date()
