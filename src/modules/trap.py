from action import Action


class Trap(Action):
    def __init__(self, name='', description=''):
        super(Trap, self).__init__()

        self.name = name
        self.description = description