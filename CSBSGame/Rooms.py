

class Rooms(object):
    def __init__(self):
        self.data = []
        self.popRooms()

    def popRooms(self):
        rooms = ['George Allen Field', 'Japanese Garden', 'Student Parking', 'The Pyramid', 'West Walkway',
                 'Rec Center', 'Forbidden Parking', 'Library', 'LA 5' , 'Bratwurst Hall', 'East Walkway',
        'Computer Lab', 'North Hall', 'Room of Retirement', 'ECS 302', 'South Hall', 'Elevators', 'ECS 308',
                 'Eat Club', 'CECS Conference Room', 'Lactation Lounge']
        return rooms

    def roomConnections(self, value):
        dict = {
            'South Hall': ['ECS 302','Eat Club', 'CECS Conference Room', 'Lactation Lounge','ECS 308','East Walkway',
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
            'South Hall':  [840,1170],
            'ECS 308':	[825,1350],
            'Lactation Lounge': [1220,1350],
            'George Allen Field':  [50,50],
            'Japanese Garden':	[450,50],
            'Pyramid':	[435,290],
            'Rec Center':	[450,570],
            'Student Parking':	[950,50],
            'Forbidden Parking':	[1050,520],
            'East Walkway':	[1470,1110],
            'Bratwurst Hall':	[1090,1670],
            'LA 5':		[480,1670],
            'Library':		[50,1670],
            'West Walkway':	[50,660],
            'Computer Lab':	[190,900],
            'ECS 302':		[620,900],
            'Eat Club':		[1050,900],
            'CECS Conference Room':[1260,900],
            'Elevators':	[620,1350],
            'North Hall':	[200,1170],
            'Room of Retirement': [190,1350]
        }
        return dict[key]