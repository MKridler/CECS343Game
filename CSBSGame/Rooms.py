from CSBSGame import *

class Rooms(object):
    def __init__(self):
        self.data = []
        self.popRooms()

    def popRooms(self):
        rooms = ['George Allen Field', 'Japanese Garden', 'Student Parking', 'The Pyramid', 'West Walkway',
                 'Rec Center', 'Forbidden Parking', 'Library', 'LA 5' , 'Bratwurst Hall', 'East Walkway',
        'Computer Lab', 'North Hall', 'Room of Retirement', 'ECS 302', 'South Hall', 'Elevators', 'ECS 308',
                 'EAT Club', 'CECS Conference Room', 'Lactation Lounge']
        return rooms

    def roomConnections(self, value):
        dict = {
            'South Hall': ['ECS 302','EAT Club', 'CECS Conference Room', 'Lactation Lounge','ECS 308','East Walkway',
                           'North Hall'],
            'ECS 308': ['South Hall'],
            'Lactation Lounge': ['South Hall'],
            'George Allen Field':['Japanese Garden','Pyramid','Rec Center','West Walkway'],
            'Japanese Garden':['George Allen Field','Pyramid','Student Parking'],
            'Pyramid':['George Allen Field','Japanese Garden','Rec Center','Student Parking'],
            'Rec Center':['George Allen Field','West Walkway','Pyramid','Student Parking','Forbidden Parking'],
            'Student Parking':['Japanese Garden','Pyramid','Rec Center','Forbidden Parking'],
            'Forbidden Parking':['Rec Center','Student Parking','East Walkway'],
            'East Walkway':['Forbidden Parking','Bratwurst Hall','South Hall'],
            'Bratwurst Hall':['East Walkway','LA 5'],
            'LA 5':['Bratwurst Hall','Library','Elevators'],
            'Library':['LA 5','West Walkway'],
            'West Walkway':['Library','Rec Center','George Allen Field','North Hall'],
            'Computer Lab':['North Hall'],
            'ECS 302':['North Hall','South Hall'],
            'EAT Club':['South Hall'],
            'CECS Conference Room':['South Hall'],
            'Elevators':['North Hall','LA 5'],
            'North Hall':['West Walkway','Computer Lab','Room of Retirement','ECS 302','Elevators','South Hall'],
            'Room of Retirement':['North Hall']
	    }
        return dict[value]

    def roomCoords(self, key):
        dict = {
            'South Hall':  [850,1170],
            'ECS 308':	[850,1350],
            'Lactation Lounge': [1230,1350],
            'George Allen Field':  [60,50],
            'Japanese Garden':	[460,50],
            'Pyramid':	[445,290],
            'Rec Center':	[460,570],
            'Student Parking':	[960,50],
            'Forbidden Parking':	[1060,520],
            'East Walkway':	[1480,1110],
            'Bratwurst Hall':	[1100,1670],
            'LA 5':		[490,1670],
            'Library':		[60,1670],
            'West Walkway':	[60,660],
            'Computer Lab':	[200,900],
            'ECS 302':		[630,900],
            'EAT Club':		[1060,900],
            'CECS Conference Room':[1270,900],
            'Elevators':	[630,1350],
            'North Hall':	[210,1170],
            'Room of Retirement': [200,1350]
        }
        return dict[key]