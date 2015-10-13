
class Player(object):

    def __init__(self, name, location):
        self.name = name
        self.location = location

    def getLocation(self):
        return self.location

    def getName(self):
        return self.name

    def setLocation(self, location):
        self.location = location
