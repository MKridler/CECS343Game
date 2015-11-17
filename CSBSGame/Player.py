class Player(object):

    def __init__(self, name, location, ai, QP, integrity, learning, craft):
        self.name = name
        self.location = location
        self.ai = ai
        self.QP = QP
        self.integrity = integrity
        self.learning = learning
        self.craft = craft
        #self.hand1 = hand1
        #self.hand()

    def getLocation(self):
        return self.location

    def getName(self):
        return self.name

    def getQP(self):
        return self.QP

    def getIntegrity(self):
        return self.integrity

    def getLearning(self):
        return self.learning

    def getCraft(self):
        return self.craft

    def setLearning(self,learning):
        self.learning = self.learning + learning

    def setCraft(self,craft):
        self.craft = self.craft + craft

    def setIntegrity(self,integrity):
        self.integrity = self.integrity + integrity

    def setQP(self, QP):
        self.QP = self.QP + QP

    def setLocation(self, location):
        self.location = location

    def getAI(self):
        return self.ai

    def setAI(self, ai):
        self.ai = ai

