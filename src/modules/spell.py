from action import Action


class Spell(Action):
    def __init__(self, name='', description=''):
        self.name = name
        self.description = description

    @staticmethod
    def run(s):
        return s()