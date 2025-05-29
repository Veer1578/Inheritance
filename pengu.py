class bird():
    def __init__(self):
        print('Bird is ready')

    def who(self):
        print('Bird')

    def swin(self):
        print('Swim faster')


class penguin(bird):
    def __init__(self):
        super().__init__()
        print('Penguin is ready')

    def who(self):
        print('Penguin')

    def run(self):
        print('Run faster')


peggy = penguin()
peggy.who()
peggy.run()
peggy.swin()