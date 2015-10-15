
class Player(object):

    def __init__(self, name, location, ai):
        self.name = name
        self.location = location
        self.ai = ai
    def getLocation(self):
        return self.location

    def getName(self):
        return self.name

    def setLocation(self, location):
        self.location = location

    def getAI(self):
        return self.ai

    def setAI(self, ai):
        self.ai = ai
