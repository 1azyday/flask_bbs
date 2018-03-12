from models import Model

class Board(Model):
    @classmethod
    def valid_names(cls):
        names = super().valid_names()
        names = names + [
            ('name', str, ''),
        ]
        return names


